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

warnings.simplefilter('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow.python.framework.ops import disable_eager_execution
disable_eager_execution()

random.seed(100)
os.environ['PYTHONHASHSEED'] = '0'