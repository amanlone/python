import numpy as np
import pandas as pd
import yfinance as yf
from yfinance import tickers

data = yf.download(tickers = ["BTC-USD", "ETH-USD", "DOGE-USD"], period = "1d", interval = "1h")

print(data)
input("exit: ")