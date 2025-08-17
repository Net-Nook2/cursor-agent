#!/usr/bin/env python3
"""
Fichier de test pour Cursor Agent.
"""

import re
from typing import Union

def calculate_sum(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Calcule la somme de deux nombres avec validation d'entrée.
    
    Args:
        a: Premier nombre
        b: Deuxième nombre
        
    Returns:
        La somme des deux nombres
        
    Raises:
        ValueError: Si les paramètres ne sont pas des nombres
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Les paramètres doivent être des nombres")
    return a + b

def validate_email(email: str) -> bool:
    """
    Valide une adresse email avec une regex appropriée.
    
    Args:
        email: L'adresse email à valider
        
    Returns:
        True si l'email est valide, False sinon
    """
    if not isinstance(email, str):
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def run_tests():
    """Exécute une série de tests pour valider les fonctions."""
    print("🧪 Exécution des tests...")
    
    # Tests pour calculate_sum
    try:
        assert calculate_sum(5, 3) == 8
        assert calculate_sum(0, 0) == 0
        assert calculate_sum(-1, 1) == 0
        assert calculate_sum(3.5, 2.5) == 6.0
        print("✅ calculate_sum: Tous les tests passent")
    except Exception as e:
        print(f"❌ calculate_sum: Erreur - {e}")
    
    # Tests pour validate_email
    try:
        assert validate_email("test@example.com") == True
        assert validate_email("user.name@domain.co.uk") == True
        assert validate_email("invalid-email") == False
        assert validate_email("test@") == False
        assert validate_email("@domain.com") == False
        assert validate_email("") == False
        print("✅ validate_email: Tous les tests passent")
    except Exception as e:
        print(f"❌ validate_email: Erreur - {e}")

def main():
    """Fonction principale."""
    # TODO: agent check - add more comprehensive tests
    print("🚀 Démarrage du démo Cursor Agent")
    print("=" * 40)
    
    # Test de base
    result = calculate_sum(5, 3)
    print(f"5 + 3 = {result}")
    
    # Test d'email
    email_valid = validate_email("test@example.com")
    print(f"Email 'test@example.com' valide: {email_valid}")
    
    # Tests complets
    print("\n" + "=" * 40)
    run_tests()
    
    print("\n🎉 Démo terminé avec succès!")

if __name__ == "__main__":
    main()

