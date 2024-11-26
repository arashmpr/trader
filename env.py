import os
import random
import warnings
import numpy as np
import pandas as pd
import tensorflow as tf
import yfinance as yf

from tensorflow import keras
from collections import deque
from keras.layers import Dense
from keras.models import Sequential

class Enviornment:
    def __init__(self, tickers, target, min_acc=0.485, n_features=10):
        self.tickers = tickers
        self.target = target 
        self.min_acc = min_acc
        self.n_features = n_features
        self.action_space = ActionSpace()

        self._get_data()
        self._prep_data()

    def _get_data(self, interval='1h', start='2023-01-01', end='2024-11-15'):
        self.data = yf.download(self.tickers, interval=interval, start=start, end=end)

    def _prep_data(self):
        self.data.dropna(inplace=True)
        self.data['return'] = np.log(self.data['Close'] / self.data['Close'].shift(1))
        self.data['trend'] = np.where(self.data['return']>0, 1, 0)
        self.data.dropna(inplace=True)
        self.data_ = (self.data - self.data.mean()) / self.data.std()

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
