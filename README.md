# CSRLStocksViewer

## About

Stock Market viewer application written in Python by the Johns Creek CSRL Embedded Programming Team.

This application provides various functions for viewing stock prices for every trading company.

# Functions

## `daily()`

### Parameters

- symbol (required) (type: `string`) - standardized market symbol

### About

Returns the current stock price for the current day.

# 

## `weekly()`

### Parameters

- symbol (required) (type: `string`) - standardized market symbol

### About

Returns the closing stock price from the last 7 days of trading.

# 

## `monthly()`

### Parameters

- symbol (required) (type: `string`) - standardized market symbol

### About

Returns the closing stock price from the last 30 days of trading.

# Attributions

## Alpha Vantage

Used for pulling real-time stock market data.
Click [here](https://www.alphavantage.co/ "Alpha Vantage Website") to view website.
