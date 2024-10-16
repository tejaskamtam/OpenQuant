from dotenv import load_dotenv
import os
import requests
from pandas import DataFrame
import json
from quantpyml.common import StockChart, Interval

load_dotenv()
ALPHA_VANTAGE_KEY = os.environ.get('ALPHA_VANTAGE_KEY') # options, longterm historical data
TWELVE_DATA_KEY = os.environ.get('TWELVE_DATA_KEY') # stocks, etfs, forex, crypto

class Market:
    EXCHANGES = ('BVC', 'XETR', 'NZX', 'JSE', 'OTC', 'FSX', 'NSE', 'BCBA', 'BME', 'XBER', 'BVS', 'LSE', 'JPX', 'EGX', 'MYX', 'MTA', 'KOSDAQ', 'OMX', 'ISE', 'SSME', 'ICEX', 'PSX', 'BSE', 'PSE', 'IDX', 'XKUW', 'Tadawul', 'DFM', 'Euronext', 'KONEX', 'TSX', 'TPEX', 'NASDAQ', 'QE', 'OSE', 'SSE', 'CBOE', 'BVL', 'VSE', 'SET', 'ADX', 'OMXV', 'OMXC', 'XESM', 'BVCC', 'Bovespa', 'TASE', 'ASE', 'XHAN', 'SGX', 'BIST', 'SZSE', 'BVB', 'NYSE', 'OMXT', 'Spotlight Stock Market', 'KRX', 'MOEX', 'TWSE', 'XDUS', 'NEO', 'XSAP', 'ICE', 'HKEX', 'XSTU', 'ASX', 'XHAM', 'XMSM', 'BMV', 'OMXH', 'CSE', 'SIX', 'GPW', 'TSXV', 'CXA', 'Munich', 'OMXR')

    @classmethod
    def get_stock_chart(cls, symbol: str, interval: Interval = Interval.DAILY, exchange: str = '') -> StockChart:
        # mock while testing:
        with open('data.json') as f:
            stock_chart = StockChart(**json.load(f))
        return stock_chart
    
        url = f'https://api.twelvedata.com/time_series?symbol={symbol}:{exchange}&interval={interval.value}&apikey={TWELVE_DATA_KEY}&outputsize=5000'
        try:
            response = requests.get(url).json()
        except Exception as e:
            raise Exception(f'Error fetching stock chart data: {e}. Exchange may be incorrect, supported exchanges:{cls.EXCHANGES}')
        
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
