"""
Agent principal Cursor.
"""

import asyncio
from typing import List, Dict, Any
from openai import OpenAI
from utils import Config, setup_logging, validate_email, calculate_sum

class CursorAgent:
    """Agent intelligent pour l'assistance au développement."""
    
    def __init__(self):
        self.config = Config()
        self.logger = setup_logging(self.config.log_level)
        self.client = OpenAI(api_key=self.config.openai_api_key)
        self.conversation_history = []
        
    async def chat(self, message: str) -> str:
        """Envoie un message à l'agent et retourne sa réponse."""
        try:
            # Ajouter le message à l'historique
            self.conversation_history.append({"role": "user", "content": message})
            
            # Préparer les messages pour l'API
            messages = [
                {"role": "system", "content": f"Tu es {self.config.agent_name}, un assistant IA spécialisé dans l'aide au développement."}
            ] + self.conversation_history[-10:]  # Garder les 10 derniers messages
            
            # Appeler l'API OpenAI
            response = await asyncio.to_thread(
                self.client.chat.completions.create,
                model=self.config.model_name,
                messages=messages,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens
            )
            
            # Extraire la réponse
            assistant_message = response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": assistant_message})
            
            self.logger.info(f"Réponse générée: {assistant_message[:100]}...")
            return assistant_message
            
        except Exception as e:
            self.logger.error(f"Erreur lors de la génération de la réponse: {e}")
            return f"Erreur: {str(e)}"
    
    def analyze_code(self, code: str) -> Dict[str, Any]:
        """Analyse du code et suggestions d'amélioration."""
        analysis = {
            "issues": [],
            "suggestions": [],
            "complexity": "low"
        }
        
        # Détection de problèmes basiques
        if "TODO" in code:
            analysis["issues"].append("TODOs non résolus détectés")
        if "FIXME" in code:
            analysis["issues"].append("FIXMEs non résolus détectés")
        if "print(" in code:
            analysis["suggestions"].append("Considérer l'utilisation d'un logger au lieu de print()")
        
        # Estimation de la complexité
        lines = code.split('\n')
        if len(lines) > 50:
            analysis["complexity"] = "high"
        elif len(lines) > 20:
            analysis["complexity"] = "medium"
            
        return analysis
    
    def run_tests(self) -> Dict[str, Any]:
        """Exécute les tests de base."""
        results = {
            "passed": 0,
            "failed": 0,
            "tests": []
        }
        
        # Test de calculate_sum
        try:
            result = calculate_sum(5, 3)
            if result == 8:
                results["passed"] += 1
                results["tests"].append({"name": "calculate_sum", "status": "passed"})
            else:
                results["failed"] += 1
                results["tests"].append({"name": "calculate_sum", "status": "failed"})
        except Exception as e:
            results["failed"] += 1
            results["tests"].append({"name": "calculate_sum", "status": "failed", "error": str(e)})
        
        # Test de validate_email
        try:
            if validate_email("test@example.com"):
                results["passed"] += 1
                results["tests"].append({"name": "validate_email_valid", "status": "passed"})
            else:
                results["failed"] += 1
                results["tests"].append({"name": "validate_email_valid", "status": "failed"})
                
            if not validate_email("invalid-email"):
                results["passed"] += 1
                results["tests"].append({"name": "validate_email_invalid", "status": "passed"})
            else:
                results["failed"] += 1
                results["tests"].append({"name": "validate_email_invalid", "status": "failed"})
        except Exception as e:
            results["failed"] += 1
            results["tests"].append({"name": "validate_email", "status": "failed", "error": str(e)})
        
        return results

async def main():
    """Fonction principale pour l'interface interactive."""
    agent = CursorAgent()
    print(f"🤖 {agent.config.agent_name} est prêt!")
    print("Tapez 'quit' pour quitter, 'test' pour exécuter les tests, 'analyze' pour analyser le code.")
    
    while True:
        try:
            user_input = input("\nVous: ").strip()
            
            if user_input.lower() == 'quit':
                print("Au revoir!")
                break
            elif user_input.lower() == 'test':
                results = agent.run_tests()
                print(f"\n📊 Résultats des tests:")
                print(f"Passés: {results['passed']}, Échoués: {results['failed']}")
                for test in results['tests']:
                    status = "✅" if test['status'] == 'passed' else "❌"
                    print(f"{status} {test['name']}")
            elif user_input.lower() == 'analyze':
                with open('src/demo.py', 'r') as f:
                    code = f.read()
                analysis = agent.analyze_code(code)
                print(f"\n🔍 Analyse du code:")
                print(f"Complexité: {analysis['complexity']}")
                if analysis['issues']:
                    print("Problèmes détectés:")
                    for issue in analysis['issues']:
                        print(f"  ⚠️  {issue}")
                if analysis['suggestions']:
                    print("Suggestions:")
                    for suggestion in analysis['suggestions']:
                        print(f"  💡 {suggestion}")
            else:
                response = await agent.chat(user_input)
                print(f"\n{agent.config.agent_name}: {response}")
                
        except KeyboardInterrupt:
            print("\nAu revoir!")
            break
        except Exception as e:
            print(f"Erreur: {e}")

if __name__ == "__main__":
    asyncio.run(main())
