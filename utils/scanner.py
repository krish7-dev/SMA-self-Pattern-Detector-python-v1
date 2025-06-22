from patterns.hammer import is_hammer
from patterns.doji import is_doji
from patterns.engulfing import is_bullish_engulfing, is_bearish_engulfing
from patterns.shooting_star import is_shooting_star
from patterns.hanging_man import is_hanging_man

previous_candle = None

def scan_patterns(candle: dict) -> list[str]:
    global previous_candle
    patterns = []

    if is_hammer(candle):
        patterns.append("hammer")
    if is_doji(candle):
        patterns.append("doji")
    if is_shooting_star(candle):
        patterns.append("shooting_star")
    if is_hanging_man(candle):
        patterns.append("hanging_man")
    if previous_candle:
        if is_bullish_engulfing(previous_candle, candle):
            patterns.append("bullish_engulfing")
        if is_bearish_engulfing(previous_candle, candle):
            patterns.append("bearish_engulfing")

    previous_candle = candle
    return patterns
