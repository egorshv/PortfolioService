from services.PortfolioHandler import PortfolioHandler


def test_precision_evaluation(test_precision_list, test_precision_answer):
    portfolio_handler = PortfolioHandler()
    precision = portfolio_handler.eval_precision(test_precision_list)
    assert precision == test_precision_answer


def test_zero_division_precision_evaluation(test_precision_zero_division):
    portfolio_handler = PortfolioHandler()
    precision = portfolio_handler.eval_precision(test_precision_zero_division)
    assert precision is None
