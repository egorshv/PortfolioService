from enum import Enum


class Period(str, Enum):
    WEEK = 'week'
    MONTH = 'month'
    QUARTER = 'quarter'
    YEAR = 'year'
    ALL_TIME = 'all_time'
