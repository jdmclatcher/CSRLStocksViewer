# Jonathan McLatcher
# Embedded Programming
# Stock Viewer Python
# stocks.py

# API test using alpha vantage to get realtime stock market prices --
from alpha_vantage.timeseries import TimeSeries

# import mat plot
import matplotlib.pyplot as plt
import json

# use api key to create ref to timeseries
ts = TimeSeries(key="B664X0BHILI87QRE", output_format="pandas")


# gets stock results from current day
def daily(_symbol):
    return ts.get_quote_endpoint(symbol=_symbol)


def weekly(_symbol):
    data, meta_data = ts.get_daily(symbol=_symbol, outputsize="compact")
    # TODO - edit data to only have last 7 days
    return data


def monthly(_symbol):
    return ts.get_monthly(symbol=_symbol)


# TODO - add more variables and customization to chart
# currenltly doesnt work with daily
def showChart(_data, _chartTitle):
    _data["4. close"].plot()
    plt.title(_chartTitle)
    plt.show()


def printData(_data):
    print(_data)
