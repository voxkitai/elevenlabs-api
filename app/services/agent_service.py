"""
ElevenLabs Agent Service
Handles all agent-related operations
"""
import time
import threading
from typing import Optional, Dict, Any
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from ..config.settings import settings

class AgentService:
    """Service class for managing ElevenLabs conversational agent"""
    
    def __init__(self):
        self.running = False
        self.conversation: Optional[Conversation] = None
        self.thread: Optional[threading.Thread] = None
        self.error: Optional[str] = None
        self.elevenlabs: Optional[ElevenLabs] = None
    
    def agent_response_callback(self, response: str) -> None:
        """Callback for agent responses"""
        print(f"\n🤖 Agent: {response}")
    
    def user_transcript_callback(self, transcript: str) -> None:
        """Callback for user transcripts"""
        print(f"\n👤 You: {transcript}")
    
    def _run_conversation(self) -> None:
        """Run the conversation in a separate thread"""
        try:
            print("🔧 Initializing ElevenLabs client...")
            self.elevenlabs = ElevenLabs(api_key=settings.get_api_key())
            
            print("🎯 Setting up conversation...")
            
            # Use full audio interface for Railway
            audio_interface = DefaultAudioInterface()
            
            self.conversation = Conversation(
                self.elevenlabs,
                settings.get_agent_id(),
                requires_auth=bool(settings.get_api_key()),
                audio_interface=audio_interface,
                callback_agent_response=self.agent_response_callback,
                callback_user_transcript=self.user_transcript_callback,
            )
            
            self.running = True
            self.error = None
            
            print("✅ Conversation setup complete!")
            self.conversation.start_session()
            
            while self.running:
                time.sleep(0.1)
                
        except Exception as e:
            print(f"\n⚠️ Conversation error: {e}")
            self.running = False
            self.error = str(e)
    
    def start_conversation(self) -> Dict[str, Any]:
        """Start the conversational AI agent"""
        if self.running:
            return {
                "success": False,
                "message": "Conversation already running",
                "status": "running"
            }
        
        if self.thread and self.thread.is_alive():
            return {
                "success": False,
                "message": "Conversation thread already active",
                "status": "running"
            }
        
        try:
            self.thread = threading.Thread(target=self._run_conversation, daemon=True)
            self.thread.start()
            
            # Wait a moment to ensure the thread starts properly
            time.sleep(0.5)
            
            if self.error:
                return {
                    "success": False,
                    "message": f"Failed to start conversation: {self.error}",
                    "status": "error"
                }
            
            return {
                "success": True,
                "message": "Conversation started successfully",
                "status": "started"
            }
            
        except Exception as e:
            self.running = False
            self.error = str(e)
            return {
                "success": False,
                "message": f"Failed to start conversation: {str(e)}",
                "status": "error"
            }
    
    def stop_conversation(self) -> Dict[str, Any]:
        """Stop the conversational AI agent"""
        if not self.running:
            return {
                "success": True,
                "message": "No conversation is currently running",
                "status": "stopped"
            }
        
        try:
            self.running = False
            
            # Wait for thread to finish
            if self.thread and self.thread.is_alive():
                self.thread.join(timeout=5)
            
            # End session gracefully
            if self.conversation:
                try:
                    self.conversation.end_session()
                except Exception as e:
                    print(f"Warning: Error ending session: {e}")
            
            self.conversation = None
            self.thread = None
            self.error = None
            
            return {
                "success": True,
                "message": "Conversation stopped successfully",
                "status": "stopped"
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"Failed to stop conversation: {str(e)}",
                "status": "error"
            }
    
    def get_status(self) -> Dict[str, Any]:
        """Get the current status of the conversation"""
        return {
            "running": self.running,
            "thread_alive": self.thread.is_alive() if self.thread else False,
            "error": self.error,
            "agent_id": settings.get_agent_id()
        }
    
    def is_healthy(self) -> bool:
        """Check if the service is healthy"""
        return bool(settings.get_agent_id() and settings.get_api_key())

# Global agent service instance
agent_service = AgentService() 