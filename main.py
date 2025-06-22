from fastapi import FastAPI, WebSocket, Query
from schema.candle import Candle
from utils.scanner import scan_patterns
import json
from datetime import date
import httpx
import urllib.parse
import sys

app = FastAPI()
print("✅ main.py is being executed")

@app.get("/")
def root():
    return {"status": "scanner running ✅"}

@app.websocket("/ws/patterns")
async def pattern_stream(websocket: WebSocket):
    await websocket.accept()
    print("✅ WebSocket connected for pattern scan")

    while True:
        try:
            data = await websocket.receive_text()
            candle_dict = json.loads(data)
            candle = Candle(**candle_dict)
            patterns = scan_patterns(candle.dict())

            response = {
                "timestamp": candle.timestamp.isoformat(),
                "patterns": patterns
            }

            await websocket.send_text(json.dumps(response))

        except Exception as e:
            await websocket.send_text(json.dumps({"error": str(e)}))


@app.get("/scan_from_data_engine")
async def scan_from_data_engine(
        symbol: str,
        from_date: date = Query(..., alias="from"),
        to_date: date = Query(..., alias="to")
):
    params = {
        "symbol": symbol,
        "from": from_date.isoformat(),
        "to": to_date.isoformat()
    }

    query_string = urllib.parse.urlencode(params)
    url = f"http://localhost:7070/api/history?{query_string}"
    print(f"🔍 Requesting: {url}", file=sys.stdout, flush=True)

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(url)

    if response.status_code != 200:
        return {"error": f"Failed to fetch from data engine: {response.text}"}

    raw_candles = response.json()
    results = []

    print(f"🕯️ Total candles received: {len(raw_candles)}", flush=True)

    for candle_dict in raw_candles:
        patterns = scan_patterns(candle_dict)
        if patterns:
            print(f"✅ Match @ {candle_dict['timestamp']} → {patterns}", flush=True)
            results.append({
                "timestamp": candle_dict["timestamp"],
                "patterns": patterns
            })

    return results
