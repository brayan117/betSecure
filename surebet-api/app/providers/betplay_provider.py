from typing import List, Dict, Any, Optional
from app.providers.provider import Provider


class BetplayProvider(Provider):
    """
    Proveedor para conectarse con la API de Betplay.
    """

    def __init__(self, timeout: int = 30):
        super().__init__(timeout=timeout)

    def get_odds(self, event_id: Optional[str] = None) -> List[Any]:
        pass

    def get_events(self, sport: Optional[str] = None) -> List[Any]:
        pass

    def get_markets(self, event_id: str) -> List[Dict[str, Any]]:
        pass

    def health_check(self) -> bool:
        pass

    def normalize_odds(self, raw_odds: Dict[str, Any]) -> Any:
        pass
