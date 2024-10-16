from enum import Enum

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