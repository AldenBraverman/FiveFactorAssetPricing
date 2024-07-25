import yfinance as yf
import pandas as pd

def calculate_dividend_growth_rate(ticker, start_date='2010-01-01', end_date='2024-01-01'):
    """
    Calculate the historical dividend growth rate for a given stock.

    :param ticker: The ticker symbol of the stock (e.g., 'AAPL').
    :param start_date: The start date for historical data.
    :param end_date: The end date for historical data.
    :return: The historical annual dividend growth rate.
    """
    # Fetch historical dividend data
    stock = yf.Ticker(ticker)
    dividends = stock.dividends.loc[start_date:end_date]
    
    if dividends.empty:
        raise ValueError("No dividend data available for this stock.")
    
    # Resample dividends to annual frequency and calculate annual dividend sums
    annual_dividends = dividends.resample('Y').sum()
    
    if len(annual_dividends) < 2:
        raise ValueError("Not enough annual dividend data to calculate growth rate.")
    
    # Calculate annual dividend growth rates
    dividend_growth_rates = annual_dividends.pct_change().dropna()
    
    # Calculate average annual dividend growth rate
    avg_growth_rate = dividend_growth_rates.mean()
    
    return avg_growth_rate

# Example usage
try:
    growth_rate = calculate_dividend_growth_rate('AAPL')
    print(f"The historical annual dividend growth rate for AAPL is: {growth_rate:.2%}")
except ValueError as e:
    print(e)
