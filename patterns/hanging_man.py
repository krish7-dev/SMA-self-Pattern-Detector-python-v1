def is_hanging_man(candle: dict) -> bool:
    open_ = candle['open']
    close = candle['close']
    high = candle['high']
    low = candle['low']

    body = abs(open_ - close)
    lower = min(open_, close)
    lower_wick = lower - low
    upper_wick = high - max(open_, close)
    total_range = high - low

    return (
            body < 0.3 * total_range and
            lower_wick > 2 * body and
            upper_wick < body
    )
