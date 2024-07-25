import yfinance as yf
import numpy as np

def calculate_beta(stock_ticker, market_ticker='^GSPC', start_date='2020-01-01', end_date='2024-01-01'):
    """
    Calculate the beta of a stock compared to a market index.

    :param stock_ticker: The ticker symbol of the stock (e.g., 'AAPL').
    :param market_ticker: The ticker symbol of the market index (e.g., '^GSPC' for S&P 500).
    :param start_date: The start date for the historical data.
    :param end_date: The end date for the historical data.
    :return: The beta of the stock.
    """
    # Fetch historical data
    stock_data = yf.download(stock_ticker, start=start_date, end=end_date)
    market_data = yf.download(market_ticker, start=start_date, end=end_date)

    # Calculate daily returns
    stock_returns = stock_data['Adj Close'].pct_change().dropna()
    market_returns = market_data['Adj Close'].pct_change().dropna()

    # Check if lengths match
    if len(stock_returns) != len(market_returns):
        raise ValueError("The length of stock and market returns data does not match.")

    # Calculate covariance and variance
    covariance = np.cov(stock_returns, market_returns)[0, 1]
    variance = np.var(market_returns)

    # Calculate beta
    beta = covariance / variance
    return beta

# Example usage
try:
    stock_beta = calculate_beta('AAPL')
    print(f"The beta of AAPL is: {stock_beta:.2f}")
except ValueError as e:
    print(e)
