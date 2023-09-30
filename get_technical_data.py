import yfinance as yf
import pandas as pd
import pickle
from get_snp_ticker_data import get_tickers


def get_technical_data():
    tickers = get_tickers()
    technical_data = {}
    for ticker in tickers:
        technical_data[ticker] = pd.DataFrame(yf.download(tickers=ticker, period="10y"))

    with open("saved_dictionary.pkl", "wb") as f:
        pickle.dump(technical_data, f)

