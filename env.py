import numpy as np
import pandas as pd
import yfinance as yf

from agent import ActionSpace
from ta import TechnicalAnalysis

class Enviornment:
    def __init__(self, tickers, target, min_acc=0.485, n_features=10):
        self.tickers = tickers
        self.target = target 
        self.min_acc = min_acc
        self.n_features = n_features
        self.action_space = ActionSpace()
        self.technical_indicators = TechnicalAnalysis()

        self._get_data()
        self._prep_data()
        self._save_data("crypto.csv")
        self._repr_data()

    def _get_data(self, interval='1h', start='2023-01-01', end='2024-11-15'):
        self.data = yf.download(self.tickers[0], interval=interval, start=start, end=end)
        self.data.columns = [col[0] for col in self.data.columns]

    def _prep_data(self):
        self.data.dropna(inplace=True)
        self.technical_indicators.set_data(self.data)

        self.data['return'] = self._add_return()
        self.data['trend'] = self._add_trend()
        self.data['vol_trend'] = self._add_vol_trend()

        self.data = self.technical_indicators.compute()

        self.data.dropna(inplace=True)
        self.n_data = (self.data - self.data.mean()) / self.data.std()
    
    def _repr_data(self):
        print("head")
        print(self.data.head())

        print("info")
        print(self.data.info())

        print("description")
        print(self.data.describe())
    
    def _save_data(self, filename):
        self.data.to_csv(filename)

    def _add_return(self):
        return np.log(self.data['Close'] / self.data['Close'].shift(1))

    def _add_trend(self):
        return np.where(self.data['return']>0, 1, 0)

    def _add_vol_trend(self):
        return np.where(np.log(self.data['Volume'] / self.data['Volume'].shift(1)) > 0, 1, 0)

    def reset(self):
        self.bar = self.n_features
        self.total_reward = 0
        state = self.data_.drop(columns=[self.target]).iloc[
            self.bar - self.n_features:self.bar
        ].values
        return state, {}
    
    def step(self, action):
        if action == self.data['trend'].iloc[self.bar]:
            correct = True
        else:
            correct = False
        
        reward = 1 if correct else 0
        self.total_reward += reward

        self.bar += 1
        self.acc = self.total_reward / (self.bar - self.n_features)

        if self.bar >= len(self.data):
            done = True
        elif reward == 1:
            done = False
        elif (self.acc < self.min_acc) and (self.bar > 20):
            done = True
        else:
            done = False
        
        next_state = self.data_.drop(columns=[self.target]).iloc[
            self.bar - self.n_features:self.bar
        ].values
        return next_state, reward, done, False, {}
