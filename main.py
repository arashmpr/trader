import os
import random
import warnings

from config_parser import ConfigParser
from env import Enviornment
from data_loader import DataLoader

warnings.simplefilter('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

random.seed(100)
os.environ['PYTHONHASHSEED'] = '0'

CONFIG_FILENAME = "config.json"
config = ConfigParser(CONFIG_FILENAME).get_config()

tickers = config['tickers']
target = config['target']

data_loader = DataLoader(config)
data = data_loader.get_data()
data_loader.show()
data_loader.save(config['filenames']['BTC'])

env = Enviornment(tickers, target, data)