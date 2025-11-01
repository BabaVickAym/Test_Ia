# success_example.py

def calculate_area(length: float, width: float) -> float:
    """Calcule l'aire d'un rectangle."""
    return length * width

def greet_user(name: str) -> str:
    """Retourne un message de salutation."""
    return f"Bonjour, {name}!"

# Utilisation correcte des types
area: float = calculate_area(10.5, 5.0)
greeting: str = greet_user("Alice")

print(f"Area: {area}")
print(f"Greeting: {greeting}")
