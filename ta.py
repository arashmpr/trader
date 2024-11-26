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

class TechnicalAnalysis:
    def __init__(self):
        