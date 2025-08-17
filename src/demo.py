#!/usr/bin/env python3
"""
Fichier de test pour CodeGuardian agent.
"""

def calculate_sum(a, b):
    # TODO: agent check - add input validation
    return a + b

def validate_email(email):
    # FIXME: implement proper regex validation
    return "@" in email

def main():
    """Fonction principale."""
    result = calculate_sum(5, 3)
    print(f"5 + 3 = {result}")
    
    # TODO: add more test cases
    email_valid = validate_email("test@example.com")
    print(f"Email valid: {email_valid}")

if __name__ == "__main__":
    main()

