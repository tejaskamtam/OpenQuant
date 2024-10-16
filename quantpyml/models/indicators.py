import talipp
from talipp.ohlcv import OHLCVFactory
from talipp.indicator_util import composite_to_lists
from dataclasses import dataclass
from quantpyml.common import Line, StockChart

# Using talipp indicators: https://nardew.github.io/talipp/latest/indicator-catalogue/
# this file maps the talipp indicators to the quantpyml indicators

@dataclass
class BB:
    period: int
    stdev_multiplier: float
    top: Line
    mid: Line
    bot: Line

@dataclass
class Ichimoku:
    base: Line
    conversion: Line
    lag: Line
    cloud_fast: Line
    cloud_slow: Line

class Indicators:
    SUPPORTED = ('SMA', 'EMA', 'HMA', 'BollingerBands', 'RSI', 'Ichimoku')

    @classmethod
    def _generate_ohlcv(cls, stock_chart: StockChart):
        ohlcv = {
            'open': stock_chart.opens,
            'high': stock_chart.highs,
            'low': stock_chart.lows,
            'close': stock_chart.closes,
        }
        return OHLCVFactory.from_dict(ohlcv)
    
    @classmethod
    def SMA(cls, series: list[float], period: int = 14) -> Line:
        """
        Simple Moving Average
        https://www.investopedia.com/terms/s/sma.asp
        """
        sma = talipp.SMA(period=period, input_values=series).output_values
        return Line(period=period, values=sma)

    @classmethod
    def EMA(cls, series: list[float], period: int = 14) -> Line:
        """
        Exponential Moving Average
        https://www.investopedia.com/terms/e/ema.asp
        """
        ema = talipp.EMA(period=period, input_values=series).output_values
        return Line(period=period, values=ema)

    @classmethod
    def HMA(cls, series: list[float], period: int = 14) -> Line:
        """
        Hull Moving Average
        https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-overlays/hull-moving-average-hma
        """
        hma = talipp.HMA(period=period, input_values=series).output_values
        return Line(period=period, values=hma)

    @classmethod
    def BollingerBands(cls, series: list[float], period: int = 14, stdev_multiplier: float = 2.0) -> BB:
        """
        Bollinger Bands
        https://www.investopedia.com/terms/b/bollingerbands.asp
        """
        bb = talipp.BB(period=period, std_dev_mult=stdev_multiplier, input_values=series)
        bb = composite_to_lists(bb)
        return BB(
            period=period,
            stdev_multiplier=stdev_multiplier,
            top=Line(period, bb['ub']),
            mid=Line(period, bb['cb']),
            bot=Line(period, bb['lb'])
        )   

    @classmethod
    def RSI(cls, series: list[float], period: int = 14) -> Line:
        """
        Relative Strength Index
        https://www.investopedia.com/terms/r/rsi.asp
        """
        rsi = talipp.RSI(period=period, input_values=series).output_values
        return Line(period=period, values=rsi)

    @classmethod
    def Ichimoku(cls, series: list[float], kijun_period: int = 26, tenkan_period: int = 9, chikou_period: int = 26, senkou_fast_period: int = 52, senkou_slow_period: int = 26) -> Ichimoku:
        """
        Ichimoku Cloud
        https://www.investopedia.com/terms/i/ichimoku-cloud.asp
        """
        ohlcv = cls._generate_ohlcv(series)
        ichimoku = talipp.Ichimoku(
            kijun_period = kijun_period,
            tenkan_period = tenkan_period,
            chikou_lag_period = chikou_period,
            senkou_slow_period = senkou_fast_period,
            senkou_lookup_period = senkou_slow_period,
            input_values = ohlcv
        )
        ichimoku = composite_to_lists(ichimoku)
        return Ichimoku(
            base = Line(period=kijun_period, values=ichimoku['kijun_sen']),
            conversion = Line(period=tenkan_period, values=ichimoku['tenkan_sen']),
            lag = Line(period=chikou_period, values=ichimoku['chikou_span']),
            cloud_fast = Line(period=senkou_fast_period, values=ichimoku['senkou_span_a']),
            cloud_slow = Line(period=senkou_slow_period, values=ichimoku['senkou_span_b'])
        )

