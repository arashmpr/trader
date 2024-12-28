import numpy as np
import yfinance as yf
import json

from ta import TechnicalAnalysis

class DataLoader:
    def __init__(self, params):
        self._fetch_data(params["tickers"], params["interval"], params["start_date"], params["end_date"])
        self._preprocess()
    
    def _fetch_data(self, tickers, interval, start, end):
        self.data = yf.download(tickers=tickers[0], interval=interval, start=start, end=end)
        self.data.columns = [col[0] for col in self.data.columns]
    
    def _preprocess(self):
        self.data.dropna(inplace=True)

        self.ta = TechnicalAnalysis(self.data)
        
        self.ta.apply()
        self.data['return'] = self._add_return()
        self.data['trend'] = self._add_trend()
        

        self.data.dropna(inplace=True)
        self.n_data = (self.data - self.data.mean()) / self.data.std()

    def _add_return(self):
        return np.log(self.data['Close'] / self.data['Close'].shift(1))

    def _add_trend(self):
        return np.where(self.data['return']>0, 1, 0)

    def _add_vol_trend(self):
        return np.where(np.log(self.data['Volume'] / self.data['Volume'].shift(1)) > 0, 1, 0)
    
    def save(self, filename):
        self.data.to_csv(filename)
    
    def show(self):
        print(self.data.head())
    
    def get_data(self):
        return self.data
    