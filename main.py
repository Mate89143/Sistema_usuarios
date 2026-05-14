#!/usr/bin/env python
"""
Sistema de Gestión de Usuarios - Aplicación de consola.
"""
import sys
from app import APP_NAME, APP_VERSION, ADMIN_USER
from app import registrar_usuario, listar_usuarios, buscar_usuario, eliminar_usuario

def mostrar_menu():
    """Muestra el menú principal."""
    print(f"\n--- {APP_NAME} v{APP_VERSION} ---")
    print(f"Usuario admin: {ADMIN_USER}")
    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")

def registrar_usuario_interactivo():
    """Pide datos por consola y registra un usuario."""
    print("\n--- Registrar nuevo usuario ---")
    try:
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        email = input("Email: ")
        usuario = registrar_usuario(nombre, edad, email)
        print(f"✅ Usuario registrado con ID {usuario['id']}")
    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

def listar_usuarios_interactivo():
    """Muestra todos los usuarios."""
    usuarios = listar_usuarios()
    if not usuarios:
        print("📭 No hay usuarios registrados.")
    else:
        print("\n--- Lista de usuarios ---")
        for u in usuarios:
            print(f"ID:{u['id']} | {u['nombre']} | {u['edad']} años | {u['email']}")

def buscar_usuario_interactivo():
    """Busca por término."""
    termino = input("Ingrese nombre o email a buscar: ")
    resultados = buscar_usuario(termino)
    if not resultados:
        print("🔍 No se encontraron coincidencias.")
    else:
        print(f"\n--- Resultados para '{termino}' ---")
        for u in resultados:
            print(f"ID:{u['id']} | {u['nombre']} | {u['edad']} años | {u['email']}")

def eliminar_usuario_interactivo():
    """Elimina por ID."""
    try:
        uid = int(input("Ingrese el ID del usuario a eliminar: "))
        if eliminar_usuario(uid):
            print("🗑️ Usuario eliminado correctamente.")
        else:
            print("⚠️ No se encontró un usuario con ese ID.")
    except ValueError:
        print("❌ El ID debe ser un número entero.")

def main():
    """Bucle principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_usuario_interactivo()
        elif opcion == "2":
            listar_usuarios_interactivo()
        elif opcion == "3":
            buscar_usuario_interactivo()
        elif opcion == "4":
            eliminar_usuario_interactivo()
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            sys.exit(0)
        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()