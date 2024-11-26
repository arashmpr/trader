import os
import random
import warnings

from env import Enviornment

warnings.simplefilter('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

random.seed(100)
os.environ['PYTHONHASHSEED'] = '0'

tickers = ['BTC-USD']
target = 'return'
env = Enviornment(tickers, target)