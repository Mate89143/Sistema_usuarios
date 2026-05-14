"""
Módulo gestor: administra la lista de usuarios (CRUD básico).
"""
from .validaciones import validar_nombre, validar_edad, validar_email

# Almacenamiento en memoria (lista de diccionarios)
_usuarios = []
_id_counter = 1

def registrar_usuario(nombre: str, edad: int, email: str) -> dict:
    """
    Registra un nuevo usuario después de validar los datos.
    Retorna el usuario creado.
    """
    global _id_counter
    # Validar
    validar_nombre(nombre)
    validar_edad(edad)
    validar_email(email)

    # Crear usuario
    usuario = {
        "id": _id_counter,
        "nombre": nombre.strip(),
        "edad": edad,
        "email": email.strip()
    }
    _usuarios.append(usuario)
    _id_counter += 1
    return usuario

def listar_usuarios() -> list:
    """Retorna la lista completa de usuarios."""
    return _usuarios.copy()

def buscar_usuario(termino: str) -> list:
    """
    Busca usuarios por nombre o email (coincidencia parcial, insensible a mayúsculas).
    """
    termino = termino.lower()
    resultados = []
    for u in _usuarios:
        if termino in u["nombre"].lower() or termino in u["email"].lower():
            resultados.append(u)
    return resultados

def eliminar_usuario(usuario_id: int) -> bool:
    """Elimina un usuario por su ID. Retorna True si se eliminó."""
    global _usuarios
    for i, u in enumerate(_usuarios):
        if u["id"] == usuario_id:
            del _usuarios[i]
            return True
    return False