"""
Utilitaires pour l'agent Cursor.
"""

import os
import logging
from typing import Optional
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

def setup_logging(level: str = "INFO") -> logging.Logger:
    """Configure le système de logging."""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

def get_env_var(key: str, default: Optional[str] = None) -> str:
    """Récupère une variable d'environnement."""
    value = os.getenv(key, default)
    if value is None:
        raise ValueError(f"Variable d'environnement {key} non définie")
    return value

def validate_email(email: str) -> bool:
    """Valide une adresse email avec une regex appropriée."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def calculate_sum(a: float, b: float) -> float:
    """Calcule la somme de deux nombres avec validation."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Les paramètres doivent être des nombres")
    return a + b

class Config:
    """Configuration de l'agent."""
    
    def __init__(self):
        self.openai_api_key = get_env_var("OPENAI_API_KEY")
        self.model_name = get_env_var("MODEL_NAME", "gpt-4")
        self.temperature = float(get_env_var("TEMPERATURE", "0.7"))
        self.max_tokens = int(get_env_var("MAX_TOKENS", "2000"))
        self.agent_name = get_env_var("AGENT_NAME", "CursorAgent")
        self.log_level = get_env_var("LOG_LEVEL", "INFO")
