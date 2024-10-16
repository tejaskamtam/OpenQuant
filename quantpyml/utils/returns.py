from quantpyml.common import StockChart
from quantpyml.common import Line

class Returns:
    @classmethod
    def calculate_returns(cls, series: Line | list[float], period: int = 1) -> Line:
        pass


    @classmethod
    def calculate_returns_chart(cls, prices: list[float]) -> StockChart:
        pass
    
    