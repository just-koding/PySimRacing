class Price:

    def __init__(self, symbol, price, daily_change, time):
        self.symbol = str(symbol)
        self.price = str(price)
        self.daily_change = str(daily_change)
        self.time = str(time)

    @property
    def out(self):
        return self.symbol + " " + self.price + " " + self.daily_change + " " + self.time
