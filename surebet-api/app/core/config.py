import os
from functools import lru_cache


class Settings:
    """
    Configuraciones globales del proyecto.
    """

    def __init__(self):
        self.ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
        self.DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"
        self.PORT: int = int(os.getenv("PORT", "8000"))
        self.TIMEOUT: int = int(os.getenv("TIMEOUT", "30"))


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

