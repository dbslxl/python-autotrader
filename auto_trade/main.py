
from time import sleep
from binance.client import Client
from binance.helpers import round_step_size
from operator import index
import requests  
import datetime as dt
from datetime import datetime
import pandas as kunfu
import numpy as dragon
import pylab as p
import statsmodels
import matplotlib.pyplot as plot
from collections import Counter
import re
import statsmodels as sm
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
import warnings
from sqlalchemy.ext.declarative import declarative_base

import pandas as pd
import binance
from binance.client import Client
import json
import requests
import datetime as dt

warnings.filterwarnings("ignore")
from datetime import datetime
import math
from sklearn.metrics import mean_squared_error, mean_absolute_error
from pmdarima.arima import auto_arima

from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import pandas as pd

import warnings
from pandas.plotting import scatter_matrix
from math import floor, sqrt
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sqlalchemy import true, types 
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey
import talib as ta
from sqlalchemy import inspect, create_engine
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

import BTC_ETH
import altcoins
from apscheduler.schedulers.background import BackgroundScheduler
from waitress import serve




def bot():
    # items.item("BTCUSDT")
    #https://www.binance.com/en/futures/ YoYoHub
    api_key = '5eD1LQCYKEdOyYuOeZWavfFWzhecoDMFBxBoUniBCXHRqBPECawXEU1JTeAVZllB' 
    api_secret = 'DdRzV1XKoZAPlzpjALQzjNlh8uuYuoFqr6OAsK8jIqF9NmCAk7iEIJvRItOHx3E7'

    #https://testnet.binancefuture.com/
    # api_key = 'e4760d9d23b3ae2d6ba2c2e6b978062d81dfaed9b1537fb863bc00ac3ed1ac0a' 
    # api_secret = '37643ce71797fb76208a3446546ea45183bdab868dac1ef25df83c8589a33532'

    #testnet
    client = Client(api_key, api_secret, testnet=False)
    # print("------------------------------------------------")
    # print(BTC_ETH.item("BTCUSDT"))
    # print("------------------------------------------------")
    # print(BTC_ETH.item("ETHUSDT"))
    print("------------------------------------------------")
    print(altcoins.item("BNBUSDT"))
    print("------------------------------------------------")
    print(altcoins.item("ATOMUSDT"))
    print("------------------------------------------------")
    print(altcoins.item("ADAUSDT"))
    print("------------------------------------------------")
    print(altcoins.item("AAVEUSDT"))
    print("------------------------------------------------")
    
    # balance
    balance = client.futures_account_balance()[6]['balance']
    print("Balance:", round((float(balance)), 2), "USDT")
    # the percentage of the Avbl balance
    print("10% of Balance:", round((float(balance)) * 10 / 100, 2), "USDT")
    
    # Avbl balance
    Avbl = client.futures_account_balance()[6]['withdrawAvailable']
    print("Avbl balance:", round((float(Avbl)), 2), "USDT")

    # the percentage of the Avbl balance
    invest_5 = round((float(Avbl)) * 10 / 100, 2)
    print("10% of Avbl:", invest_5, "USDT")
    print("20x:", round(invest_5*20, 2), "USDT")
    today = datetime.today().strftime('%Y-%m-%d %H %M %S') 
    print("Datetime:", today)

scheduler = BackgroundScheduler(daemon=True, timezone = 'Asia/Seoul')
scheduler.add_job(bot,'cron', hour='0-23', minute='4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59', second='55')
scheduler.start()  

while true:
    sleep(10)


