

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

from sqlalchemy import inspect, create_engine
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

def OBV(price, volume):
    obv = pd.Series(index=price.index)
    obv.iloc[0] = volume.iloc[0]

    for i in range (1, len(price)):
        if price.iloc[i] > price.iloc[i-1]:
            obv.iloc[i] = obv.iloc[i-1] + volume[i]
        
        elif price.iloc[i] < price.iloc[i-1]:
            obv.iloc[i] = obv.iloc[i-1] - volume[i]
        else: obv.iloc[i] = obv.iloc[i-1] 
    return obv

def hour_8(market):
    interval = '8h'
    yesterday = datetime.today()- timedelta(days = 30)
    today = datetime.today().strftime('%Y-%m-%d %H') 
    startTime=  str(round(datetime.strptime(yesterday.strftime('%Y-%m-%d %H') ,'%Y-%m-%d %H').timestamp()* 1000))
    endTime = str(round(datetime.strptime(today,'%Y-%m-%d %H').timestamp()* 1000))

    url = 'https://fapi.binance.com/fapi/v1/klines?symbol='+market+'&interval='+interval+'&startTime='+startTime+'&endTime='+ endTime
    data = requests.get(url)
    df = pd.DataFrame(data.json(), columns = ['datetime', 'open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades','taker_base_vol', 'taker_quote_vol', 'ignore'])
    df.index = [dt.datetime.fromtimestamp(x/1000.0) for x in df.datetime]
    df = df.drop(['qav', 'close_time' , 'num_trades','taker_base_vol', 'taker_quote_vol', 'ignore'], axis=1)
    df=df.astype(float)

    obv = OBV(df['close'], df['volume'])
    df['OBV'] = obv.round(4)
    df['OBV_SMA'] = df['OBV'].rolling(window=10).mean()


    df.loc[(df['OBV'] > df['OBV_SMA']),'OBVV'] = 1
    df.loc[ (df['OBV'] < df['OBV_SMA']),'OBVV'] = 0
    
    return df


def min_15(market):   
    yesterday = datetime.today()- timedelta(hours = 24)
    today = datetime.today().strftime('%Y-%m-%d %H%M') 
    startTime=  str(round(datetime.strptime(yesterday.strftime('%Y-%m-%d %H%M') ,'%Y-%m-%d %H%M').timestamp()* 1000))
    endTime = str(round(datetime.strptime(today,'%Y-%m-%d %H%M').timestamp()* 1000))

    df3=pd.DataFrame(columns = ['datetime', 'open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades','taker_base_vol', 'taker_quote_vol', 'ignore'])

    interval2 = '15m'
    url2 = 'https://fapi.binance.com/fapi/v1/klines?symbol='+ market +'&interval='+interval2+'&startTime='+startTime+'&endTime='+ endTime
    data2 = requests.get(url2)
    df2 = pd.DataFrame( data2.json(), columns = ['datetime', 'open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades','taker_base_vol', 'taker_quote_vol', 'ignore'])
    df3=pd.concat([df3,df2])
    df3.index = [dt.datetime.fromtimestamp(x/1000.0) for x in df3.datetime]
    df3 = df3.drop(['datetime','qav','close_time' , 'num_trades','taker_base_vol', 'taker_quote_vol', 'ignore'], axis=1)
    df3 = df3.astype(float)

    obv_5m = OBV(df3['close'], df3['volume'])
    df3['OBV'] = obv_5m.round(4)
    df3['OBV_SMA'] = df3['OBV'].rolling(window=10).mean()
    df3.loc[(df3['OBV'] > df3['OBV_SMA']),'OBVV'] = 1
    df3.loc[ (df3['OBV'] < df3['OBV_SMA']),'OBVV'] = 0

    # buy_5m= df3[(df3['OBV'] > df3['OBV_SMA'])] 
    # buy_5m['datetime'] = buy_5m.index
    # buy_5m = buy_5m.groupby(pd.to_datetime(buy_5m.index).strftime('%Y-%m-%d')).agg('last')

    # sell_5m= df3[(df3['OBV'] < df3['OBV_SMA'])] 
    # sell_5m['datetime'] = sell_5m.index
    # sell_5m = sell_5m.groupby(pd.to_datetime(sell_5m.index).strftime('%Y-%m-%d')).agg('last')
    return df3


def min_5(market):   
    yesterday = datetime.today()- timedelta(hours = 24)
    today = datetime.today().strftime('%Y-%m-%d %H%M') 
    startTime=  str(round(datetime.strptime(yesterday.strftime('%Y-%m-%d %H%M') ,'%Y-%m-%d %H%M').timestamp()* 1000))
    endTime = str(round(datetime.strptime(today,'%Y-%m-%d %H%M').timestamp()* 1000))

    df3=pd.DataFrame(columns = ['datetime', 'open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades','taker_base_vol', 'taker_quote_vol', 'ignore'])
    interval2 = '5m'
    url2 = 'https://fapi.binance.com/fapi/v1/klines?symbol='+ market +'&interval='+interval2+'&startTime='+startTime+'&endTime='+ endTime
    data2 = requests.get(url2)
    df2 = pd.DataFrame( data2.json(), columns = ['datetime', 'open', 'high', 'low', 'close', 'volume','close_time', 'qav', 'num_trades','taker_base_vol', 'taker_quote_vol', 'ignore'])
    df3=pd.concat([df3,df2])
    df3.index = [dt.datetime.fromtimestamp(x/1000.0) for x in df3.datetime]
    df3 = df3.drop(['datetime','qav','close_time' , 'num_trades','taker_base_vol', 'taker_quote_vol', 'ignore'], axis=1)
    df3 = df3.astype(float)

    obv_5m = OBV(df3['close'], df3['volume'])
    df3['OBV'] = obv_5m.round(4)
    df3['OBV_SMA'] = df3['OBV'].rolling(window=10).mean()
    df3.loc[(df3['OBV'] > df3['OBV_SMA']),'OBVV'] = 1
    df3.loc[ (df3['OBV'] < df3['OBV_SMA']),'OBVV'] = 0

    # buy_5m= df3[(df3['OBV'] > df3['OBV_SMA'])] 
    # buy_5m['datetime'] = buy_5m.index
    # buy_5m = buy_5m.groupby(pd.to_datetime(buy_5m.index).strftime('%Y-%m-%d')).agg('last')

    # sell_5m= df3[(df3['OBV'] < df3['OBV_SMA'])] 
    # sell_5m['datetime'] = sell_5m.index
    # sell_5m = sell_5m.groupby(pd.to_datetime(sell_5m.index).strftime('%Y-%m-%d')).agg('last')
    return df3


#https://www.binance.com/en/futures/ YoYoHub
api_key = '5eD1LQCYKEdOyYuOeZWavfFWzhecoDMFBxBoUniBCXHRqBPECawXEU1JTeAVZllB' 
api_secret = 'DdRzV1XKoZAPlzpjALQzjNlh8uuYuoFqr6OAsK8jIqF9NmCAk7iEIJvRItOHx3E7'

client = Client(api_key, api_secret, testnet=False)


def item(market):

    OBV_5min = min_5(market)
    OBV_15min = min_15(market)
    OBV_1d = hour_8(market)
    print(market)
    print('8hour', OBV_1d['OBVV'][-1])
    print('5min', OBV_5min['OBVV'][-1])
    print('15min', OBV_15min['OBVV'][-1])

    def get_account_balance():
        balance = client.futures_account_balance()[6]['withdrawAvailable']
        return float(balance)

    # the percentage of the balance
    invest_30 = round((get_account_balance()) * 30 / 100, 2)

    symbol_info = client.get_ticker(symbol=market)
    symbol_price = float(symbol_info['lastPrice'])
    quantity = float(round( (invest_30*20) / symbol_price, 1))
    
    k=client.futures_position_information(symbol=market)
    df1 = pd.DataFrame(k) 
    df1.updateTime = [dt.datetime.fromtimestamp(x/1000.0) for x in df1.updateTime]
    df1 = df1.drop(['marginType', 'isolatedMargin', 'liquidationPrice', 'maxNotionalValue','positionSide', 'notional', 'isolatedWallet', 'isAutoAddMargin','updateTime', 'leverage'], axis=1)
    # #PNL-ROE
    # if((float(df1["unRealizedProfit"][2]) ) != 0):
    #     iM =  float(df1["positionAmt"][2])*(-1) * float(df1["markPrice"][2]) * 1/20 
    #     print("SHORT", "PNL:", round((float(df1["unRealizedProfit"][2]) ), 2), "USDT", " ","ROE%:" ,round((float(df1["unRealizedProfit"][2]) )/ (iM) * 100, 2), "%")

    # #LONG
    # if ((float(df1['positionAmt'][1])==0) & (OBV_1d['OBVV'][-1] == 1) & (OBV_5min['OBVV'][-1] == 1)) :
    #     #market order to buy
    #     buyorder = client.futures_create_order(symbol=market, side='BUY', positionSide='LONG', type='MARKET', quantity=quantity, leverage=20, marginType='cross')       
    #     print(buyorder)
    # if ((float(df1['positionAmt'][1])!=0) & (OBV_1d['OBVV'][-1] == 0) & (OBV_15min['OBVV'][-1] == 0)):
    #     #market order to sell
    #     sellorder=client.futures_create_order(symbol=market, side='SELL', positionSide='LONG', type='MARKET', quantity=float(df1['positionAmt'][1]) )       
    #     print(sellorder)
    
    # #SHORT
    # if ((float(df1['positionAmt'][2])==0) & (OBV_1d['OBVV'][-1] == 0) & (OBV_15min['OBVV'][-1] == 0)) :
    #     buyorder1 = client.futures_create_order(symbol=market, side='SELL', positionSide='SHORT', type='MARKET', quantity=round(quantity, 0), leverage=20, marginType='cross')       
    #     print(buyorder1)
    # if ((float(df1['positionAmt'][2])!=0) & (OBV_1d['OBVV'][-1] == 1) & (OBV_5min['OBVV'][-1] == 1)):
    #     sellorder1=client.futures_create_order(symbol=market, side='BUY', positionSide='SHORT', type='MARKET', quantity=round(float(df1['positionAmt'][2])*(-1), 1))       
    #     print(sellorder1)

    return df1
