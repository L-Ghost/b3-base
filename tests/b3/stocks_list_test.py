import pytest
from b3.stocks_list import StocksList


def test_parse_list_into_dict():
    first_stock = [
            '2020-07-24', 'PETR3', 'BRPETRACNOR9', 'CASH',
            '23,05', '23,69', '23,4', '23,33', '', '', '21458', '11202000'
        ]
    second_stock = [
            '2020-07-24', 'PETR4', 'BRPETRACNPR6', 'CASH',
            '22,42', '23,06', '22,75', '22,73', '', '', '45405', '43380300'
        ]
    trade_information_stocks = [first_stock, second_stock]

    stocks_list = StocksList(trade_information_stocks)

    assert stocks_list.to_dict() == {
            'PETR3': {
                'minimum_price': '23,05',
                'maximum_price': '23,69',
                'average_price': '23,4',
                'last_price': '23,33'
            },
            'PETR4': {
                'minimum_price': '22,42',
                'maximum_price': '23,06',
                'average_price': '22,75',
                'last_price': '22,73'
            }
        }


