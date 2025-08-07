"""
Configuration settings for the ElevenLabs API
"""
import os
from typing import Optional

class Settings:
    """Application settings"""
    
    # ElevenLabs Configuration
    AGENT_ID: str = "agent_01jyejwedvegpshenkr440gp0h"
    API_KEY: str = "sk_dc0a0b1a0d4f60609225986d0dbbfabfb5574d14e569aa88"
    
    # API Configuration
    API_TITLE: str = "ElevenLabs Conversational AI API"
    API_DESCRIPTION: str = "API for controlling ElevenLabs conversational AI agent"
    API_VERSION: str = "1.0.0"
    
    # Server Configuration
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    RELOAD: bool = True
    
    # CORS Configuration
    CORS_ORIGINS: list = ["*"]
    CORS_CREDENTIALS: bool = True
    CORS_METHODS: list = ["*"]
    CORS_HEADERS: list = ["*"]
    
    @classmethod
    def get_api_key(cls) -> str:
        """Get API key from environment or use default"""
        return os.getenv("ELEVENLABS_API_KEY", cls.API_KEY)
    
    @classmethod
    def get_agent_id(cls) -> str:
        """Get agent ID from environment or use default"""
        return os.getenv("ELEVENLABS_AGENT_ID", cls.AGENT_ID)

# Global settings instance
settings = Settings() 