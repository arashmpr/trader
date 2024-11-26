import numpy as np
import yfinance as yf

from ta import TechnicalAnalysis

class Preprocess:
    def __init__(self, tickers):
        self.tickers = tickers
        self._get_data()
        self._preprocess()
    
    def _preprocess(self):
        self.data.dropna(inplace=True)
        self.ta = TechnicalAnalysis(self.data)

        self.data['return'] = self._add_return()
        self.data['trend'] = self._add_trend()
        self.data['vol_trend'] = self._add_vol_trend()

        self.data = self.ta.compute()

        self.data.dropna(inplace=True)
        self.n_data = (self.data - self.data.mean()) / self.data.std()
    
    def show(self):
        print("head")
        print(self.data.head())
        print("\n\n")

        print("info")
        print(self.data.info())
        print("\n\n")

        print("description")
        print(self.data.describe())
        print()
    
    def save(self, filename):
        self.data.to_csv(filename)
    
    def get_data(self):
        return self.data
    
    def _get_data(self, interval='1h', start='2023-01-01', end='2024-11-15'):
        self.data = yf.download(self.tickers[0], interval=interval, start=start, end=end)
        self.data.columns = [col[0] for col in self.data.columns]

    def _add_return(self):
        return np.log(self.data['Close'] / self.data['Close'].shift(1))

    def _add_trend(self):
        return np.where(self.data['return']>0, 1, 0)

    def _add_vol_trend(self):
        return np.where(np.log(self.data['Volume'] / self.data['Volume'].shift(1)) > 0, 1, 0)
    