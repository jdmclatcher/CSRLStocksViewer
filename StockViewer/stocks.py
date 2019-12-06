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


def showChart(data, chartTitle):
    # TODO - fix charting
    # data validation to prevent daily from beign charted
    data.plot()
    plt.title(chartTitle)
    plt.show()


# TODO - add dates
# private function
def __printData(data, symbol):
    # formatting
    sys.stdout.write(Style.BRIGHT + '#### "' + symbol + '" STOCK PRICE - ')
    if len(data) < 7:
        sys.stdout.write(Style.BRIGHT + "TODAY ####\n" + Style.RESET_ALL)
        # TODO - needs better formatting/cleanup
        print(data)
        return
    if len(data) >= 7 and len(data) < 30:
        sys.stdout.write(Style.BRIGHT + "LAST 7 DAYS ####\n" + Style.RESET_ALL)
    if len(data) >= 30:
        sys.stdout.write(Style.BRIGHT + "LAST 30 DAYS ####\n" + Style.RESET_ALL)
    for item in data:
        sys.stdout.write("MM/DD/YYYY: ")
        if item > 0:
            sys.stdout.write(Fore.GREEN + str(item) + "\n" + Fore.RESET)
        else:
            sys.stdout.write(Fore.RED + str(item) + "\n" + Fore.RESET)
