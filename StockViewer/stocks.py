# Jonathan McLatcher
# Embedded Programming
# Stock Viewer Python
# stocks.py

# API test using alpha vantage to get realtime stock market prices --
from alpha_vantage.timeseries import TimeSeries

# import mat plot
import matplotlib.pyplot as plt
import json

# import datetime

# use api key to create ref to timeseries
ts = TimeSeries(key="B664X0BHILI87QRE", output_format="pandas")


# gets stock results from current day
def daily(symbol):
    # TODO - need to return "5. price" and "10. change percent" column
    data = ts.get_quote_endpoint(symbol)
    return data[0]["05. price"]


def weekly(symbol):
    data, meta_data = ts.get_daily(symbol, outputsize="compact")
    # only get data from last 7 days - close price
    # TODO get close value (4) for each day, week percent, and year to date
    newData = []
    y = 0
    for item in data["4. close"]:
        if y == 7:
            break
        newData.append(item)
        y = y + 1
    return newData


# last 30 days - close price
def monthly(symbol):
    newData = []
    y = 0
    for item in data["4. close"]:
        if y == 30:
            break
        newData.append(item)
        y = y + 1
    return newData


# TODO - add more variables and customization to chart
# currently doesn't work with daily
def showChart(_data, _chartTitle):
    _data["4. close"].plot()
    plt.title(_chartTitle)
    plt.show()


def printData(_data):
    print(_data)
