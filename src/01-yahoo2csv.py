#
# Read stock market data from Yahoo and save to a csv file.
#

from pandas_datareader import data as pdr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import os

if __name__ == '__main__':
    ticker = 'IBM'
    filename = ticker + '.csv'
    yf.pdr_override()
    df = pdr.get_data_yahoo(ticker, start='2023-01-01', end='2023-06-01')
    print(f'******* Env BOB = {os.getenv("BOB")}')
    print(f'******* Env ACCESS_KEY = {os.getenv("ACCESS_KEY")}')
    print(f'******* Env ACCESS_SECRET = {os.getenv("ACCESS_SECRET")}')
    print(f'******* Env S3_ENDPOINT = {os.getenv("S3_ENDPOINT")}')

    print(f'Count = {df.count()}')
    print(f'Saving as {filename}')
    df.to_csv(filename)
