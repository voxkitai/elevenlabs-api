"""
Vercel serverless handler for ElevenLabs API
"""
from mangum import Mangum
from app.main import app

# Create handler for Vercel
handler = Mangum(app) 