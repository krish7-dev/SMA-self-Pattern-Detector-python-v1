import asyncio
import websockets
import json
from schema.candle import Candle
from scanner import scan_patterns

async def consume_ticks():
    uri = "ws://localhost:7070/ws/marketdata"

    async with websockets.connect(uri) as websocket:
        print("✅ Connected to Java WebSocket")
        while True:
            try:
                msg = await websocket.recv()
                print("📩 Raw message:", msg)

                data = json.loads(msg)

                # 🔍 Filter out non-candle messages
                if "timestamp" not in data or "open" not in data:
                    print("⚠️ Skipping non-candle message")
                    continue

                candle = Candle(**data)
                patterns = scan_patterns(candle.dict())

                if patterns:
                    print(f"✅ Pattern(s) detected at {candle.timestamp}: {patterns}")

            except Exception as e:
                print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(consume_ticks())
