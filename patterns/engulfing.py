def is_bullish_engulfing(prev: dict, curr: dict) -> bool:
    return (prev['close'] < prev['open'] and  # previous red
            curr['close'] > curr['open'] and  # current green
            curr['open'] < prev['close'] and
            curr['close'] > prev['open'])

def is_bearish_engulfing(prev: dict, curr: dict) -> bool:
    return (prev['close'] > prev['open'] and  # previous green
            curr['close'] < curr['open'] and  # current red
            curr['open'] > prev['close'] and
            curr['close'] < prev['open'])
