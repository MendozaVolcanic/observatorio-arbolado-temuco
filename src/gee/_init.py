"""Inicialización de Google Earth Engine.

Usar init_ee() en todos los módulos en vez de ee.Initialize() directo,
para que el Cloud Project se lea siempre desde .env (GEE_PROJECT).
"""
import os
import ee
from dotenv import load_dotenv

load_dotenv()

_INITIALIZED = False


def init_ee() -> None:
    """Inicializa GEE con el proyecto de .env. Idempotente."""
    global _INITIALIZED
    if _INITIALIZED:
        return
    project = os.getenv("GEE_PROJECT")
    if not project:
        raise RuntimeError(
            "Falta GEE_PROJECT en .env. Copiá .env.example a .env y poné tu Cloud Project ID."
        )
    ee.Initialize(project=project)
    _INITIALIZED = True
