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

class ActionSpace:
    def sample(self):
        """
        Chooses randomly between 0 (Sell), 1 (Hold), 2 (Buy) for action.

        Returns:
            int: Action as int
        """
        return random.choice([0, 1, 2])

class 