def is_shooting_star(candle: dict) -> bool:
    open_ = candle['open']
    close = candle['close']
    high = candle['high']
    low = candle['low']

    body = abs(close - open_)
    upper_wick = high - max(open_, close)
    lower_wick = min(open_, close) - low
    total_range = high - low

    return body < 0.3 * total_range and upper_wick > 2 * body and lower_wick < body
