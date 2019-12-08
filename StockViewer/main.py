# Embedded Programming
# Stock Viewer Python
# main.py

from stocks import *


def main():
    # Alex Eyerly
    # Gets the company and type of summary to provide
    stockSelect = input(
        "What company would you like to see? Please enter the abbreviated symbol for the company. "
    ).upper()
    option = input(
        "Would you like to see the daily, weekly, or monthly summary? Use D, W, or M. "
    ).upper()
    # Daily report
    if option == "D":
        # Makes sure company inputted was valid
        try:
            daily(stockSelect)

        except:
            print(
                "Something went wrong. Perhaps you mistyped the stock code or are sending requests too frequently?"
            )

    elif option == "W":
        # Makes sure company inputted was valid
        try:
            weekly(stockSelect)

        except:
            print(
                "Something went wrong. Perhaps you mistyped the stock code or are sending requests too frequently?"
            )

    elif option == "M":
        # Makes sure company inputted was valid
        try:
            monthly(stockSelect)

        except:
            print(
                "Something went wrong. Perhaps you mistyped the stock code or are sending requests too frequently?"
            )
    # User inputted an incorrect summary option
    else:
        print("Sorry, that's not a recognized command.")


if (__name__) == "__main__":
    main()
