import yfinance as yf

# Define the stock ticker
ticker = 'AAPL'

# Fetch stock data
stock = yf.Ticker(ticker)

# Get dividend info
dividends = stock.dividends
if dividends.empty:
    raise ValueError("No dividend data available for this stock.")

# Get the last dividend
last_dividend = dividends[-1]

# Define the Dividend Discount Model function
def calculate_stock_price(dividend_next_year, required_rate_of_return, dividend_growth_rate):
    """
    Calculate the stock price using the Gordon Growth Model.
    
    :param dividend_next_year: The expected dividend for the next year
    :param required_rate_of_return: The required rate of return (as a decimal)
    :param dividend_growth_rate: The growth rate of dividends (as a decimal)
    :return: The estimated stock price
    """
    if required_rate_of_return <= dividend_growth_rate:
        raise ValueError("Required rate of return must be greater than the dividend growth rate.")
    
    stock_price = dividend_next_year / (required_rate_of_return - dividend_growth_rate)
    return stock_price

# Define assumptions for required rate of return and dividend growth rate
required_rate_of_return = 0.07  # Example: 7%
dividend_growth_rate = 0.05    # Example: 5%

# Calculate the next year's dividend (assuming a constant dividend for simplicity)
dividend_next_year = last_dividend * (1 + dividend_growth_rate)

# Calculate and print the stock price
try:
    stock_price = calculate_stock_price(dividend_next_year, required_rate_of_return, dividend_growth_rate)
    print(f"The estimated stock price for {ticker} is: ${stock_price:.2f}")
except ValueError as e:
    print(e)
