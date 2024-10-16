from dataclasses import dataclass
from quantpyml.common import Line

@dataclass
class StockChart:
    symbol: str
    interval: str
    currency: str
    timezone: str
    exchange: str
    mic: str
    asset_type: str
    timestamp: Line
    volume: Line
    opens: Line
    highs: Line
    lows: Line
    closes: Line
