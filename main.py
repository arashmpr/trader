import os
import random
import warnings

from env import Enviornment
from preprocess import Preprocess

warnings.simplefilter('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

random.seed(100)
os.environ['PYTHONHASHSEED'] = '0'

tickers = ['BTC-USD']
target = 'return'

preprocess = Preprocess(tickers)
data = preprocess.get_data()
preprocess.show()
preprocess.save('crypto.csv')

env = Enviornment(tickers, target, data)