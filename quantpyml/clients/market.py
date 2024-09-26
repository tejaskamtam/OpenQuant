from enum import Enum
from dotenv import load_dotenv
import os
import requests
from pandas import DataFrame
from dataclasses import dataclass, asdict
import json

load_dotenv()
ALPHA_VANTAGE_KEY = os.environ.get('ALPHA_VANTAGE_KEY') # options, longterm historical data
TWELVE_DATA_KEY = os.environ.get('TWELVE_DATA_KEY') # stocks, etfs, forex, crypto

@dataclass
class StockChart:
    symbol: str
    interval: str
    currency: str
    timezone: str
    exchange: str
    mic: str
    asset_type: str
    timestamp: list[str]
    volume: list[float]
    opens: list[float]
    highs: list[float]
    lows: list[float]
    closes: list[float]

class Interval(Enum):
    MINUTELY = '1min'
    FIVE_MINUTELY = '5min'
    FIFTEEN_MINUTELY = '15min'
    THIRTY_MINUTELY = '30min'
    FORTY_FIVE_MINUTELY = '45min'
    HOURLY = '1h'
    TWO_HOURLY = '2h'
    FOUR_HOURLY = '4h'
    DAILY = '1day'
    WEEKLY = '1week'
    MONTHLY = '1month'


class Market:
    EXCHANGES = ('BVC', 'XETR', 'NZX', 'JSE', 'OTC', 'FSX', 'NSE', 'BCBA', 'BME', 'XBER', 'BVS', 'LSE', 'JPX', 'EGX', 'MYX', 'MTA', 'KOSDAQ', 'OMX', 'ISE', 'SSME', 'ICEX', 'PSX', 'BSE', 'PSE', 'IDX', 'XKUW', 'Tadawul', 'DFM', 'Euronext', 'KONEX', 'TSX', 'TPEX', 'NASDAQ', 'QE', 'OSE', 'SSE', 'CBOE', 'BVL', 'VSE', 'SET', 'ADX', 'OMXV', 'OMXC', 'XESM', 'BVCC', 'Bovespa', 'TASE', 'ASE', 'XHAN', 'SGX', 'BIST', 'SZSE', 'BVB', 'NYSE', 'OMXT', 'Spotlight Stock Market', 'KRX', 'MOEX', 'TWSE', 'XDUS', 'NEO', 'XSAP', 'ICE', 'HKEX', 'XSTU', 'ASX', 'XHAM', 'XMSM', 'BMV', 'OMXH', 'CSE', 'SIX', 'GPW', 'TSXV', 'CXA', 'Munich', 'OMXR')

    @classmethod
    def get_stock_chart(cls, symbol: str, interval: Interval = Interval.DAILY, exchange: str = '') -> StockChart:
        # mock while testing:
        # with open('data.json') as f:
        #     stock_chart = StockChart(**json.load(f))
        # return stock_chart
    
        url = f'https://api.twelvedata.com/time_series?symbol={symbol}:{exchange}&interval={interval.value}&apikey={TWELVE_DATA_KEY}&outputsize=5000'
        try:
            response = requests.get(url).json()
        except Exception as e:
            raise Exception(f'Error fetching stock chart data: {e}. Exchange may be incorrect, supported exchanges:{Market.EXCHANGES}')
        
        metadata = response["meta"]
        values = DataFrame(response["values"])

        return StockChart(
            symbol=metadata["symbol"],
            interval=metadata["interval"],
            currency=metadata["currency"],
            timezone=metadata["exchange_timezone"],
            exchange=metadata["exchange"],
            mic=metadata["mic_code"],
            asset_type=metadata["type"],
            timestamp=values["datetime"].tolist()[::-1],
            volume=values["volume"].astype(float).tolist()[::-1],
            opens=values["open"].astype(float).tolist()[::-1],
            highs=values["high"].astype(float).tolist()[::-1],
            lows=values["low"].astype(float).tolist()[::-1],
            closes=values["close"].astype(float).tolist()[::-1]
        )


