import httpx
from typing import List, Dict, Any, Optional
from app.providers.provider import Provider
from app.core.config import settings


class BetplayProvider(Provider):
    """
    Proveedor para conectarse con la API de Betplay.
    """

    def __init__(self, timeout: int = 30):
        super().__init__(timeout=timeout)
        self.url = settings.BETPLAY_URL

    async def get_odds(self, event_id: Optional[str] = None) -> List[Any]:
        pass

    async def get_events(self, sport: Optional[str] = None) -> List[Any]:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(self.url)
            data = response.json()
            return data

    async def get_markets(self, event_id: str) -> List[Dict[str, Any]]:
        pass

    async def health_check(self) -> bool:
        pass

    def normalize_odds(self, raw_odds: Dict[str, Any]) -> Any:
        pass
