# Cursor Agent

Un agent intelligent basé sur Python pour l'assistance au développement.

## Installation

1. Cloner le repository :
```bash
git clone <repository-url>
cd cursor-agent
```

2. Créer un environnement virtuel :
```bash
python -m venv venv
```

3. Activer l'environnement virtuel :
- Windows :
```bash
venv\Scripts\activate
```
- Linux/Mac :
```bash
source venv/bin/activate
```

4. Installer les dépendances :
```bash
pip install -r requirements.txt
```

5. Configurer les variables d'environnement :
```bash
cp .env.example .env
```
Puis éditer le fichier `.env` avec vos clés API.

## Utilisation

### Exécuter le démo
```bash
python src/demo.py
```

### Lancer l'API
```bash
python src/api.py
```

### Lancer l'agent interactif
```bash
python src/agent.py
```

## Configuration

Créez un fichier `.env` avec les variables suivantes :
```
OPENAI_API_KEY=your_openai_api_key_here
MODEL_NAME=gpt-4
TEMPERATURE=0.7
```

## Structure du projet

```
cursor-agent/
├── src/
│   ├── demo.py          # Démonstration de base
│   ├── agent.py         # Agent principal
│   ├── api.py           # API FastAPI
│   └── utils.py         # Utilitaires
├── requirements.txt     # Dépendances Python
├── README.md           # Documentation
└── .env.example        # Exemple de configuration
```
