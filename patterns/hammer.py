def is_hammer(candle: dict) -> bool:
    open_ = candle['open']
    close = candle['close']
    high = candle['high']
    low = candle['low']

    body = abs(open_ - close)
    lower = min(open_, close)
    lower_wick = lower - low
    total_range = high - low

    result = body < 0.3 * total_range and lower_wick > 2 * body

    if result:
        print(f"🔍 Hammer Detected: {candle}", flush=True)

    return result
