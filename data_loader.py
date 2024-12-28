import numpy as np
import yfinance as yf
import json

from ta import TechnicalAnalysis

class DataLoader:
    def __init__(self):
        config = self._load_config()
        self._fetch_data(config["tickers"], config["interval"], config["start_date"], config["end_date"])
        self._preprocess()
    
    def _load_config(self):
        with open("config.json", 'r') as file:
            config = json.load(file)
        
        return config
    
    def _preprocess(self):
        self.data.dropna(inplace=True)

        self.ta = TechnicalAnalysis(self.data)
        
        self.ta.apply()
        self.data['return'] = self._add_return()
        self.data['trend'] = self._add_trend()
        

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
    
    def _fetch_data(self, tickers, interval, start, end):
        self.data = yf.download(tickers[0], interval=interval, start=start, end=end)
        self.data.columns = [col[0] for col in self.data.columns]

    def _add_return(self):
        return np.log(self.data['Close'] / self.data['Close'].shift(1))

    def _add_trend(self):
        return np.where(self.data['return']>0, 1, 0)

    def _add_vol_trend(self):
        return np.where(np.log(self.data['Volume'] / self.data['Volume'].shift(1)) > 0, 1, 0)
    