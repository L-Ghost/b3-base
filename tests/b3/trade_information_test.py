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

    assert first_stock == [
            '2020-07-24', 'PETR3', 'BRPETRACNOR9', 'CASH',
            '23,05', '23,69', '23,4', '23,33', '', '', '21458', '11202000'
        ]
    assert second_stock == [
            '2020-07-24', 'PETR3F', 'BRPETRACNOR9', 'ODD LOT',
            '23,06', '23,67', '23,38', '23,45', '', '', '945', '17609'
        ]
    assert len(stocks_list) == 4
