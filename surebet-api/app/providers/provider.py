from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional


class Provider(ABC):
    """
    Clase base abstracta que define la interfaz que deben implementar
    todos los proveedores de casas de apuestas.
    """

    def __init__(self, timeout: int = 30):
        self.timeout = timeout

    @abstractmethod
    async def get_odds(self, event_id: Optional[str] = None) -> List[Any]:
        pass

    @abstractmethod
    async def get_events(self, sport: Optional[str] = None) -> List[Any]:
        pass

    @abstractmethod
    async def get_markets(self, event_id: str) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        pass

    @abstractmethod
    def normalize_odds(self, raw_odds: Dict[str, Any]) -> Any:
        pass
