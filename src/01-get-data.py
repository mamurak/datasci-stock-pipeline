#
# Read stock market data from Yahoo and save to a csv file.
#

import os

import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd


def get_stock_data(ticker, start_date, end_date, filename):

    yf.pdr_override()
    df = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)

    print(f"Count = {df.count()}")
    print(f"Saving as {filename}")

    df.to_csv(filename)


if __name__ == "__main__":

    ticker = "IBM"
    filename = "../data/" + ticker + "-sample.csv"
    
    get_stock_data(ticker, start_date="2023-01-01", end_date="2023-06-01", filename=filename)
