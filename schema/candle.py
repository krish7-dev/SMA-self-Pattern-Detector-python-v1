from pydantic import BaseModel
from datetime import datetime

class Candle(BaseModel):
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float
