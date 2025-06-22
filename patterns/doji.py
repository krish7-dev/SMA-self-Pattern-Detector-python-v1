def is_doji(candle: dict) -> bool:
    open_ = candle['open']
    close = candle['close']
    high = candle['high']
    low = candle['low']

    body = abs(open_ - close)
    range_ = high - low

    return body < 0.1 * range_
