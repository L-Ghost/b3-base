
class StocksList:
    def __init__(self, stocks):
        self.stocks = stocks

    def to_dict(self):
        return {
            stock_info[1]: {
                'minimum_price': stock_info[4],
                'maximum_price': stock_info[5],
                'average_price': stock_info[6],
                'last_price': stock_info[7]
            } for stock_info in self.stocks
        }

