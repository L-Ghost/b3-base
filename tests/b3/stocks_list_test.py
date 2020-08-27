import pytest
from b3 import StocksList


@pytest.fixture
def stocks_list():
    '''Retrieves a list with stocks data'''
    trade_information_stocks = [
        [
            '2020-07-24', 'PETR3', 'BRPETRACNOR9', 'CASH',
            '23,05', '23,69', '23,4', '23,33', '', '', '21458', '11202000'
        ],
        [
            '2020-07-24', 'PETR4', 'BRPETRACNPR6', 'CASH',
            '22,42', '23,06', '22,75', '22,73', '', '', '45405', '43380300'
        ]
    ]

    return StocksList(trade_information_stocks)

@pytest.fixture
def stocks_tickers_list():
    '''Retrieves a list with tickers stocks data only'''
    return StocksList([
        ['2020-08-26', 'PETR3'],
        ['2020-08-26', 'PETR4'],
        ['2020-08-26', 'BBAS3'],
        ['2020-08-26', 'ELET3'],
        ['2020-08-26', 'ELET6'],
        ['2020-08-26', 'KLBN4'],
        ['2020-08-26', 'KLBN11'],
        ['2020-08-26', 'SNSY5'],
        ['2020-08-26', 'AMZO34'],
    ])


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

def test_retrieve_common_shares(stocks_tickers_list):
    assert stocks_tickers_list.common_shares() == ['PETR3', 'BBAS3', 'ELET3']

def test_retrieve_preferred_shares(stocks_tickers_list):
    assert stocks_tickers_list.preferred_shares() == ['PETR4', 'KLBN4']

