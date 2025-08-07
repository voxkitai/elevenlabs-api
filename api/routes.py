"""
API Routes for ElevenLabs Conversational AI
"""
import time
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from services.agent_service import agent_service
from config.settings import settings

# Create router
router = APIRouter()

@router.get("/")
def root():
    """Root endpoint with API information"""
    return {
        "message": "ElevenLabs Conversational AI API",
        "version": settings.API_VERSION,
        "endpoints": {
            "start_conversation": "POST /start-conversation",
            "stop_conversation": "POST /stop-conversation", 
            "status": "GET /status",
            "health": "GET /health",
            "docs": "GET /docs"
        }
    }

@router.post("/start-conversation")
def start_conversation():
    """Start the conversational AI agent"""
    result = agent_service.start_conversation()
    
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    
    return result

@router.post("/stop-conversation")
def stop_conversation():
    """Stop the conversational AI agent"""
    result = agent_service.stop_conversation()
    
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result["message"])
    
    return result

@router.get("/status")
def get_status():
    """Get the current status of the conversation"""
    return agent_service.get_status()

@router.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy" if agent_service.is_healthy() else "unhealthy",
        "timestamp": time.time(),
        "agent_configured": agent_service.is_healthy(),
        "conversation_running": agent_service.running
    } 