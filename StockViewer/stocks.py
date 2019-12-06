# Jonathan McLatcher
# Embedded Programming
# Stock Viewer Python
# stocks.py

# alpha vantage API to get realtime stock market prices
from alpha_vantage.timeseries import TimeSeries

import matplotlib.pyplot as plt  # for charting

import sys
import colorama  # for colored console text
from colorama import Fore, Style

colorama.init()

# create ref to timeseries
ts = TimeSeries(key="B664X0BHILI87QRE", output_format="pandas")


# gets stock results from current day
def daily(symbol):
    data = ts.get_quote_endpoint(symbol)
    newData = []
    newData.append(data[0]["05. price"])
    newData.append(data[0]["10. change percent"])
    __printData(newData, symbol)
    return


# last 7 days - close price
def weekly(symbol):
    data, meta_data = ts.get_daily(symbol, outputsize="compact")
    newData = []
    y = 0
    for item in data["4. close"]:
        if y == 7:
            break
        newData.append(item)
        y = y + 1
    __printData(newData, symbol)
    return


# last 30 days - close price
def monthly(symbol):
    data, meta_data = ts.get_daily(symbol, outputsize="compact")
    newData = []
    y = 0
    for item in data["4. close"]:
        if y == 30:
            break
        newData.append(item)
        y = y + 1
    __printData(newData, symbol)
    return


# TODO - add more variables and customization to chart
def showChart(data, chartTitle):
    # TODO - fix charting
    # data validation to prevent daily from beign charted
    data.plot()
    plt.title(chartTitle)
    plt.show()


# private function
def __printData(data, symbol):
    # formatting
    sys.stdout.write(Style.BRIGHT + '#### "' + symbol + '" STOCK PRICE - ')
    if len(data) < 7:
        print(Style.BRIGHT + "TODAY ####")
        # TODO - needs better formatting/cleanup
        print(data)
        return
    if len(data) >= 7 and len(data) < 30:
        print(Style.BRIGHT + "LAST 7 DAYS ####")
    if len(data) >= 30:
        print(Style.BRIGHT + "LAST 30 DAYS ####")
    for item in data:
        if item > 0:
            print(Fore.GREEN + str(item))
        else:
            print(Fore.RED + str(item))
