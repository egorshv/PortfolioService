from services.PortfolioHandler import PortfolioHandler


def test_recall_evaluation(test_trade_set1, test_recall_answer1):
    portfolio_handler = PortfolioHandler()
    recall = portfolio_handler.eval_recall(test_trade_set1)
    assert recall == test_recall_answer1


def test_zero_division_recall_evaluation(test_trade_set2):
    portfolio_handler = PortfolioHandler()
    recall = portfolio_handler.eval_recall(test_trade_set2)
    assert recall is None
