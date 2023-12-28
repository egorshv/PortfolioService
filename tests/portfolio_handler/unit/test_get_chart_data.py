from datetime import datetime

from services.PortfolioHandler import PortfolioHandler


def test_get_chart_data(test_portfolio_states, test_currency):
    portfolio_handler = PortfolioHandler()
    chart_data = portfolio_handler.get_chart_data(test_portfolio_states, test_currency)
    print(chart_data)
    assert len(chart_data) == len(test_portfolio_states)
    for value, dt in chart_data:
        assert isinstance(value, float)
        assert isinstance(dt, datetime)


def test_get_chart_data_with_no_states(test_empty_portfolio_states, test_currency):
    portfolio_handler = PortfolioHandler()
    chart_data = portfolio_handler.get_chart_data(test_empty_portfolio_states, test_currency)
    assert len(chart_data) == 0
