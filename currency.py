import currencies as cur

class Currency:
    def __init__(self) -> None:
        self.first_currency = None
        self.second_currency = None

    def set_first_currency(self, text):
        self.first_currency = text

    def set_second_currency(self, text):
        self.second_currency = text

    def reset(self):
        self.first_currency = None
        self.second_currency = None

    def get_url(self):
        first = self.first_currency
        second = self.second_currency
        return "http://economia.awesomeapi.com.br/json/last/{}-{}".format(first, second)

    def get_long_name(self, text):
        for item in cur.CURRENCIES:
            if text in item[1]:
                return item[0]
        return False
    
    def get_short_name(self, text):
        for item in cur.CURRENCIES:
            if text in item[0]:
                return item[1]
        return False