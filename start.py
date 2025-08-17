#!/usr/bin/env python3
"""
Script de démarrage pour Cursor Agent.
"""

import sys
import os
import subprocess
from pathlib import Path

def check_dependencies():
    """Vérifie si les dépendances sont installées."""
    try:
        import openai
        import fastapi
        import uvicorn
        import pydantic
        print("✅ Toutes les dépendances sont installées")
        return True
    except ImportError as e:
        print(f"❌ Dépendance manquante: {e}")
        print("Installez les dépendances avec: pip install -r requirements.txt")
        return False

def check_env_file():
    """Vérifie si le fichier .env existe."""
    env_file = Path(".env")
    if not env_file.exists():
        print("⚠️  Fichier .env non trouvé")
        print("Copiez env.example vers .env et configurez vos clés API:")
        print("cp env.example .env")
        return False
    return True

def run_demo():
    """Exécute le démo."""
    print("🚀 Lancement du démo...")
    subprocess.run([sys.executable, "src/demo.py"])

def run_agent():
    """Lance l'agent interactif."""
    print("🤖 Lancement de l'agent interactif...")
    subprocess.run([sys.executable, "src/agent.py"])

def run_api():
    """Lance l'API."""
    print("🌐 Lancement de l'API...")
    subprocess.run([sys.executable, "src/api.py"])

def install_dependencies():
    """Installe les dépendances."""
    print("📦 Installation des dépendances...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def main():
    """Fonction principale."""
    print("🎯 Cursor Agent - Script de démarrage")
    print("=" * 40)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python start.py demo     - Lancer le démo")
        print("  python start.py agent    - Lancer l'agent interactif")
        print("  python start.py api      - Lancer l'API")
        print("  python start.py install  - Installer les dépendances")
        print("  python start.py check    - Vérifier la configuration")
        return
    
    command = sys.argv[1].lower()
    
    if command == "install":
        install_dependencies()
    elif command == "check":
        print("🔍 Vérification de la configuration...")
        deps_ok = check_dependencies()
        env_ok = check_env_file()
        if deps_ok and env_ok:
            print("✅ Configuration OK")
        else:
            print("❌ Configuration incomplète")
    elif command == "demo":
        if check_dependencies():
            run_demo()
    elif command == "agent":
        if check_dependencies() and check_env_file():
            run_agent()
    elif command == "api":
        if check_dependencies() and check_env_file():
            run_api()
    else:
        print(f"❌ Commande inconnue: {command}")

if __name__ == "__main__":
    main()
