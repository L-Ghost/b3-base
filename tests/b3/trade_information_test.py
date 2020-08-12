import pytest
import os
from b3.trade_information import TradeInformation

TEST_FILE = 'trade_information_test/TradeInformationConsolidatedFile_sample.csv'

def test_read_file_and_return_stocks_list():
    test_dir = os.path.dirname(__file__)
    test_file_path = os.path.join(test_dir, TEST_FILE)
    trade_information = TradeInformation(test_file_path)
    stocks_list = trade_information.parse()
    first_stock = stocks_list[0]
    second_stock = stocks_list[1]

    assert first_stock[1] == 'PETR3'
    assert second_stock[1] == 'PETR3F'
    assert len(stocks_list) == 4
