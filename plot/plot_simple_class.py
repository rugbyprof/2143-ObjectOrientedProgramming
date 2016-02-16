"""
Yahoo Finance Website:
    https://pypi.python.org/pypi/yahoo-finance

Installing yahoo finance:
    git clone git://github.com/lukaszbanasiak/yahoo-finance.git
    cd yahoo-finance
    python setup.py install

Instructions to install matplotlib here: 
    http://matplotlib.org/faq/installing_faq.html

Small tutorial on MatPlotLib:
    http://matplotlib.org/users/pyplot_tutorial.html
"""

from yahoo_finance import Share 
import matplotlib.pyplot as plt
import random


class StockOrganizer(object):

    def __init__(self):
        self.Stocks = {}

    def loadStock(self,symbol):

        self.Stocks[symbol] = {}
        self.Stocks[symbol]['object'] = Share(symbol)
        self.Stocks[symbol]['open'] = self.Stocks[symbol]['object'].get_open() 
        self.Stocks[symbol]['price'] = self.Stocks[symbol]['object'].get_price()
        self.Stocks[symbol]['historical'] = self.Stocks[symbol]['object'].get_historical('2015-01-01', '2015-2-28')
        
    def dumpStocks(self):
        for key in self.Stocks:
            print(key,self.Stocks[key])
            for subkey in self.Stocks[key]:
                print(subkey,self.Stocks[key][subkey])
                
    def graphAll(self):
        AllHighPrices = {}
        for key in self.Stocks:
            AllHighPrices[key] = []
            for day in self.Stocks[key]['historical']:
                AllHighPrices[key].append(day['High']) 
        for key in AllHighPrices:
            plt.plot(AllHighPrices[key])
        plt.ylabel('some numbers')
        plt.show()     
                       

if __name__=='__main__':
    MyStock = StockOrganizer()
    MyStock.loadStock("IBM")
    MyStock.loadStock("GOOG")
    MyStock.loadStock("CUDA")
    MyStock.loadStock("YHOO")   
    # MyStock.dumpStocks()
    MyStock.graphAll()
    