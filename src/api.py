"""
API FastAPI pour l'agent Cursor.
"""

import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import uvicorn
from agent import CursorAgent
from utils import Config, setup_logging

# Configuration
config = Config()
logger = setup_logging(config.log_level)

# Création de l'application FastAPI
app = FastAPI(
    title="Cursor Agent API",
    description="API pour l'agent intelligent Cursor",
    version="1.0.0"
)

# Instance de l'agent
agent = CursorAgent()

# Modèles Pydantic
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    agent_name: str

class CodeAnalysisRequest(BaseModel):
    code: str

class CodeAnalysisResponse(BaseModel):
    issues: List[str]
    suggestions: List[str]
    complexity: str

class TestResponse(BaseModel):
    passed: int
    failed: int
    tests: List[Dict[str, Any]]

@app.get("/")
async def root():
    """Point d'entrée principal."""
    return {
        "message": f"Bienvenue sur l'API {config.agent_name}",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Vérification de l'état de santé de l'API."""
    return {"status": "healthy", "agent": config.agent_name}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Endpoint pour discuter avec l'agent."""
    try:
        response = await agent.chat(request.message)
        return ChatResponse(
            response=response,
            agent_name=config.agent_name
        )
    except Exception as e:
        logger.error(f"Erreur lors du chat: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze", response_model=CodeAnalysisResponse)
async def analyze_code(request: CodeAnalysisRequest):
    """Endpoint pour analyser du code."""
    try:
        analysis = agent.analyze_code(request.code)
        return CodeAnalysisResponse(
            issues=analysis["issues"],
            suggestions=analysis["suggestions"],
            complexity=analysis["complexity"]
        )
    except Exception as e:
        logger.error(f"Erreur lors de l'analyse: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/test", response_model=TestResponse)
async def run_tests():
    """Endpoint pour exécuter les tests."""
    try:
        results = agent.run_tests()
        return TestResponse(
            passed=results["passed"],
            failed=results["failed"],
            tests=results["tests"]
        )
    except Exception as e:
        logger.error(f"Erreur lors des tests: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/config")
async def get_config():
    """Endpoint pour récupérer la configuration (sans les clés sensibles)."""
    return {
        "model_name": config.model_name,
        "temperature": config.temperature,
        "max_tokens": config.max_tokens,
        "agent_name": config.agent_name,
        "log_level": config.log_level
    }

if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", "8000"))
    debug = os.getenv("DEBUG", "False").lower() == "true"
    
    logger.info(f"Démarrage de l'API sur {host}:{port}")
    uvicorn.run(
        "api:app",
        host=host,
        port=port,
        reload=debug,
        log_level=config.log_level.lower()
    )
