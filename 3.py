def average(stock_data, symbol, start_date, end_date):
    closing_prices = []
    for data in stock_data:
        stock_symbol, date, closing_price = data
        if stock_symbol == symbol and start_date <= date <= end_date:
            closing_prices.append(closing_price)
    if closing_prices:
        average_price = sum(closing_prices) / len(closing_prices)
        return average_price
    else:
        return None
    

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
]

symbol = "AAPL"
start_date = "2021-01-01"
end_date = "2021-01-02"
average_price = average(stock_data, symbol, start_date, end_date)
if average_price is not None:
    print(f"Average closing price of {symbol} from {start_date} to {end_date}: {average_price}")
else:
    print(f"No data found for {symbol} from {start_date} to {end_date}")