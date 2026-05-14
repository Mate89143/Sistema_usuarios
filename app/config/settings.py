"""
Módulo de configuración - Carga variables de entorno.
"""
import os
from pathlib import Path


def load_dotenv() -> None:
    env_path = Path(".env")
    if not env_path.exists():
        return

    with env_path.open(encoding="utf-8") as env_file:
        for line in env_file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, sep, value = line.partition("=")
            if sep:
                os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))

# Cargar variables desde .env
load_dotenv()

# Leer variables con valores por defecto por seguridad
APP_NAME = os.getenv("APP_NAME", "Sistema Usuarios")
APP_VERSION = os.getenv("APP_VERSION", "0.0")
ADMIN_USER = os.getenv("ADMIN_USER", "admin")

# Variable opcional: modo debug (por si la agregas después)
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")