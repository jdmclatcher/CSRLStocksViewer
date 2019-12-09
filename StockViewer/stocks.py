# Embedded Programming
# Stock Viewer Python
# stocks.py

# alpha vantage API to get realtime stock market prices
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

import sys
import colorama  # for colored console text
from colorama import Fore, Style

colorama.init()

# create ref to timeseries
ts = TimeSeries(key="B664X0BHILI87QRE", output_format="pandas")

# Jonathan McLatcher

# gets stock results from current day
def daily(symbol):
    data, meta_data = ts.get_quote_endpoint(symbol)
    newData = []
    newData.append(data["05. price"][0])
    newData.append(data["10. change percent"][0])
    __printData(newData, symbol)
    return


# last 7 days - close price
def weekly(symbol):
    data, meta_data = ts.get_daily(symbol, outputsize="compact")
    sys.stdout.write(
        Style.BRIGHT
        + '#### "'
        + symbol
        + '" STOCK PRICE - LAST 7 DAYS ####\n'
        + Style.RESET_ALL
    )
    pprint(data.head(7))
    return


# last 30 days - close price
def monthly(symbol):
    data, meta_data = ts.get_daily(symbol, outputsize="compact")
    sys.stdout.write(
        Style.BRIGHT
        + '#### "'
        + symbol
        + '" STOCK PRICE - LAST 30 DAYS ####\n"'
        + Style.RESET_ALL
    )
    pprint(data.head(30))
    return


# Joe Francesconi
# private function
def __printData(data, symbol):
    # formatting
    sys.stdout.write(Style.BRIGHT + '#### "' + symbol + '" STOCK PRICE - ')
    if len(data) < 7:
        sys.stdout.write(Style.BRIGHT + "TODAY ####\n" + Style.RESET_ALL)
        print("Price: " + data[0])
        sys.stdout.write("Percent Change: ")
        percent = str(data[1])
        if float(percent[0:-1]) > 0:
            sys.stdout.write(Fore.GREEN + str(data[1]) + "\n" + Fore.RESET)
        else:
            sys.stdout.write(Fore.RED + str(data[1]) + "\n" + Fore.RESET)
        return
