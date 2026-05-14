"""
Módulo de validaciones para datos de usuarios.
"""

def validar_nombre(nombre: str) -> bool:
    """Valida que el nombre no esté vacío y tenga al menos 3 caracteres."""
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    if len(nombre.strip()) < 3:
        raise ValueError("El nombre debe tener al menos 3 caracteres.")
    return True

def validar_edad(edad: int) -> bool:
    """Valida que la edad sea un número entre 1 y 120."""
    if not isinstance(edad, int):
        raise ValueError("La edad debe ser un número entero.")
    if edad < 1 or edad > 120:
        raise ValueError("La edad debe estar entre 1 y 120 años.")
    return True

def validar_email(email: str) -> bool:
    """Validación muy simple de email (contiene @ y .)."""
    if not email or "@" not in email or "." not in email:
        raise ValueError("El email no tiene un formato válido.")
    return True