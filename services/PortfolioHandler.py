import abc
from datetime import datetime
from typing import List

import numpy as np

from schemas.operation import OperationSchema
from schemas.portfolio import PortfolioSchema
from schemas.state import StateSchema
from schemas.trade import TradeMark
from schemas.currency import Currency
from schemas.period import Period


class AbstractPortfolioHandler(abc.ABC):

    def __init__(self, portfolio: PortfolioSchema):
        self.portfolio = portfolio

    @abc.abstractmethod
    async def eval_precision(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    async def eval_recall(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    async def eval_general_profitability_by_period(self, period: Period, currency: Currency) -> float:
        """Вычисляется как отношение полученной доходности (итоговый размер портфеля - внесенные средства)
         к средней сумме на счете в течение периода"""
        raise NotImplementedError

    @abc.abstractmethod
    async def eval_stock_profitability_by_period(self, period: Period, current_value: float) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    async def eval_sectors_ratio(self):
        raise NotImplementedError

    @abc.abstractmethod
    async def eval_stock_type_ratio(self):
        raise NotImplementedError

    @abc.abstractmethod
    async def eval_chart_data(self, period: Period):
        raise NotImplementedError

    @abc.abstractmethod
    async def export_portfolio_data(self):
        raise NotImplementedError


class PortfolioHandler(AbstractPortfolioHandler):
    def __init__(self, portfolio: PortfolioSchema):
        super().__init__(portfolio)

    def _get_mark_count(self, mark: TradeMark):
        mark_count = len(list(filter(lambda trade: trade.mark == mark, self.portfolio.trades)))
        return mark_count

    def eval_recall(self) -> float:
        true_positive_count = self._get_mark_count(TradeMark.TP)
        false_negative_count = self._get_mark_count(TradeMark.FN)

        recall = true_positive_count / (true_positive_count + false_negative_count)
        return recall

    def eval_precision(self) -> float:
        true_positive_count = self._get_mark_count(TradeMark.TP)
        false_positive_count = self._get_mark_count(TradeMark.FP)

        precision = true_positive_count / (true_positive_count + false_positive_count)
        return precision

    def _eval_start_datetime(self, period: Period) -> datetime:
        pass

    @staticmethod
    def _eval_mean_deposited_money(period_operations: List[OperationSchema]) -> datetime:
        deposited_money: List[float] = list(map(lambda operation: operation.value, period_operations))
        mean_deposited_money = np.mean(deposited_money)

        return mean_deposited_money

    def _get_operations_by_period(self, period: Period, operations: List[OperationSchema]):
        start_datetime: datetime = self._eval_start_datetime(period)
        period_operations: List[OperationSchema] = list(
            filter(lambda operation: operation.created_at > start_datetime, operations))

        return period_operations

    @staticmethod
    def _get_state_value_by_currency(state: StateSchema, currency: Currency) -> float:
        state_values = {currency.RUB: state.RUB_result, currency.USD: state.USD_result}
        return state_values.get(currency)

    def eval_general_profitability_by_period_and_currency(self, period: Period, currency: Currency) -> float:
        period_operations = self._get_operations_by_period(period, self.portfolio.operations)

        mean_deposited_money = self._eval_mean_deposited_money(period_operations)
        last_state = self.portfolio.states[-1]
        last_state_value = self._get_state_value_by_currency(last_state, currency)
