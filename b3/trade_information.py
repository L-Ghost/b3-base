import csv

class TradeInformation:
    def __init__(self, data_file):
        self.data_file = data_file

    def parse(self):
        with open(self.data_file) as content:
            reader = csv.reader(content, delimiter=';')
            stocks_data = list(reader)

        return self.filter_stocks(stocks_data)

    def filter_stocks(self, stocks_data):
        return list(filter(
            lambda row: row[3] in ['CASH', 'ODD LOT'], stocks_data
        ))

