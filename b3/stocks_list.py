import re


class StocksList:
    COMMON_SHARES_REGEX = "^\w{4}3$"
    PREFERRED_SHARES_REGEX = "^\w{4}4$"

    def __init__(self, stocks):
        self.stocks = stocks

    def tickers(self):
        return [stock_info[1] for stock_info in self.stocks]

    def common_shares(self):
        return list(filter(
            lambda ticker: self.__common_share_ticker(ticker), self.tickers()
        ))

    def preferred_shares(self):
        return list(filter(
            lambda ticker: self.__preferred_share_ticker(ticker), self.tickers()
        ))

    def to_dict(self):
        return {
            stock_info[1]: {
                'minimum_price': stock_info[4],
                'maximum_price': stock_info[5],
                'average_price': stock_info[6],
                'last_price': stock_info[7]
            } for stock_info in self.stocks
        }

    def __common_share_ticker(self, ticker):
        return re.search(self.COMMON_SHARES_REGEX, ticker)

    def __preferred_share_ticker(self, ticker):
        return re.search(self.PREFERRED_SHARES_REGEX, ticker)

