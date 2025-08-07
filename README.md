# ElevenLabs Conversational AI API

A professional FastAPI application for controlling ElevenLabs conversational AI agents.

## 🏗️ Project Structure

```
11Labs_API/
├── main.py              # FastAPI app entry point
├── config/
│   ├── __init__.py
│   └── settings.py      # Configuration management
├── services/
│   ├── __init__.py
│   └── agent_service.py # ElevenLabs agent logic
├── api/
│   ├── __init__.py
│   └── routes.py        # API endpoints
├── utils/
│   ├── __init__.py
│   └── helpers.py       # Utility functions
├── requirements.txt
└── README.md
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the API
```bash
# Using uvicorn directly
uvicorn main:app --reload

# Or using Python
python main.py
```

### 3. Access the API
- **API Documentation**: http://127.0.0.1:8000/docs
- **Health Check**: http://127.0.0.1:8000/health
- **Status**: http://127.0.0.1:8000/status

## 📋 API Endpoints

### Start Conversation
```http
POST /start-conversation
```

### Stop Conversation
```http
POST /stop-conversation
```

### Get Status
```http
GET /status
```

### Health Check
```http
GET /health
```

## 🔧 Configuration

Edit `config/settings.py` to customize:
- API keys and agent IDs
- Server settings
- CORS configuration

## 🏛️ Architecture

### Modular Design
- **Config**: Centralized configuration management
- **Services**: Business logic and agent operations
- **API**: HTTP endpoints and request handling
- **Utils**: Common utility functions

### Key Features
- ✅ Professional modular structure
- ✅ Clean separation of concerns
- ✅ Easy to maintain and extend
- ✅ Comprehensive error handling
- ✅ Health checks and monitoring
- ✅ CORS support for web integration
- ✅ Auto-generated API documentation

## 🛠️ Development

### Adding New Features
1. **New API endpoints**: Add to `api/routes.py`
2. **New services**: Create in `services/` directory
3. **Configuration**: Update `config/settings.py`
4. **Utilities**: Add to `utils/helpers.py`

### Environment Variables
```bash
ELEVENLABS_API_KEY=your_api_key_here
ELEVENLABS_AGENT_ID=your_agent_id_here
```

## 📦 Dependencies

- **FastAPI**: Modern web framework
- **Uvicorn**: ASGI server
- **ElevenLabs**: AI voice and conversation
- **PyAudio**: Audio processing
- **Python-dotenv**: Environment management

## 🤝 Contributing

1. Follow the modular structure
2. Add proper error handling
3. Include docstrings for functions
4. Test your changes thoroughly

## 📄 License

This project is for educational and development purposes. 