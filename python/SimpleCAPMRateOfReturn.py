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

    # Calculate covariance and variance
    covariance = np.cov(stock_returns, market_returns)[0, 1]
    variance = np.var(market_returns)

    # Calculate beta
    beta = covariance / variance
    return beta

def calculate_required_rate_of_return(risk_free_rate, market_return, stock_beta):
    """
    Calculate the required rate of return using the CAPM formula.

    :param risk_free_rate: The risk-free rate (as a decimal).
    :param market_return: The expected market return (as a decimal).
    :param stock_beta: The beta of the stock.
    :return: The required rate of return.
    """
    return risk_free_rate + stock_beta * (market_return - risk_free_rate)

# Example usage
try:
    # Define inputs
    stock_ticker = 'AAPL'
    market_ticker = '^GSPC'  # S&P 500 index
    risk_free_rate = 0.04  # 4% risk-free rate
    market_return = 0.08  # 8% expected market return
    start_date = '2020-01-01'
    end_date = '2024-01-01'
    
    # Calculate beta
    stock_beta = calculate_beta(stock_ticker, market_ticker, start_date, end_date)
    
    # Calculate required rate of return
    required_return = calculate_required_rate_of_return(risk_free_rate, market_return, stock_beta)
    
    print(f"The beta of {stock_ticker} is: {stock_beta:.2f}")
    print(f"The required rate of return for {stock_ticker} is: {required_return:.2%}")
except ValueError as e:
    print(e)
