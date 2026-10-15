import asyncio
import sys
from app.providers.betplay_provider import BetplayProvider


async def main():
    provider = BetplayProvider()
    data = await provider.get_events()
    live_events = data.get('liveEvents', [])
    print(f"\nRecibidos {len(live_events)} eventos en vivo")
    print(f"{live_events}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    asyncio.run(main())
