import pytest
from b3 import StocksList


@pytest.fixture
def stocks_list():
    '''Retrieves a list with stocks data'''
    first_stock = [
            '2020-07-24', 'PETR3', 'BRPETRACNOR9', 'CASH',
            '23,05', '23,69', '23,4', '23,33', '', '', '21458', '11202000'
        ]
    second_stock = [
            '2020-07-24', 'PETR4', 'BRPETRACNPR6', 'CASH',
            '22,42', '23,06', '22,75', '22,73', '', '', '45405', '43380300'
        ]
    trade_information_stocks = [first_stock, second_stock]

    return StocksList(trade_information_stocks)

def test_parse_list_into_dict(stocks_list):
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

def test_retrieve_tickers_from_list(stocks_list):
    assert stocks_list.tickers() == ['PETR3', 'PETR4']

