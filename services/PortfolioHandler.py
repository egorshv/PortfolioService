import abc
from datetime import datetime
from typing import List, Tuple, Optional

from schemas.currency import Currency
from schemas.period import Period
from schemas.portfolio import PortfolioSchema
from schemas.state import StateSchema
from schemas.trade import TradeMark, TradeSchema


class AbstractPortfolioHandler(abc.ABC):

    @abc.abstractmethod
    async def eval_precision(self, trades: List[TradeSchema]) -> Optional[float]:
        raise NotImplementedError

    @abc.abstractmethod
    async def eval_recall(self, trades: List[TradeSchema]) -> Optional[float]:
        raise NotImplementedError

    @abc.abstractmethod
    async def get_chart_data(self, states: StateSchema, currency: Currency) -> List[Tuple[float, datetime]]:
        raise NotImplementedError


class PortfolioHandler(AbstractPortfolioHandler):
    def __init__(self):
        pass

    @staticmethod
    def _get_mark_count(trades: List[TradeSchema], mark: TradeMark) -> int:
        mark_count = len(list(filter(lambda trade: trade.mark == mark, trades)))
        return mark_count

    def eval_recall(self, trades: List[TradeSchema]) -> Optional[float]:
        true_positive_count = self._get_mark_count(trades, TradeMark.TP)
        false_negative_count = self._get_mark_count(trades, TradeMark.FN)

        if true_positive_count + false_negative_count > 0:
            recall = true_positive_count / (true_positive_count + false_negative_count)
            return recall

    def eval_precision(self, trades: List[TradeSchema]) -> Optional[float]:
        true_positive_count = self._get_mark_count(trades, TradeMark.TP)
        false_positive_count = self._get_mark_count(trades, TradeMark.FP)

        if true_positive_count + false_positive_count > 0:
            precision = true_positive_count / (true_positive_count + false_positive_count)
            return precision

    @staticmethod
    def _get_states_result(states: List[StateSchema], currency: Currency) -> List[Tuple[float, datetime]]:
        states_result = None
        if currency == Currency.USD:
            states_result = [(state.usd_result, state.created_at) for state in states]
        elif currency == Currency.RUB:
            states_result = [(state.rub_result, state.created_at) for state in states]
        return states_result

    def get_chart_data(self, states: List[StateSchema], currency: Currency) -> List[Tuple[float, datetime]]:
        states_result: List[Tuple[float, datetime]] = self._get_states_result(states, currency)
        return states_result
