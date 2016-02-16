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
    
    # L = [random.randint(10, 100) for i in range(25)]
    # M = [random.randint(10, 100) for i in range(25)] 
    # plt.plot(L)
    # plt.plot(M)
    # plt.ylabel('some numbers')
    # plt.show()

    

# Shares['IBM'] = {}

# Shares['IBM']['object'] = Share('IBM')
# Shares['IBM']['open'] = Shares['IBM']['object'].get_open() 
# Shares['IBM']['price'] = Shares['IBM']['object'].get_price() 








# Shares['YHOO']['price'] = Shares['YHOO']['object'].get_price()
# Shares['YHOO']['historical'] = Shares['YHOO']['object'].get_historical('2015-01-01', '2015-12-31')

#print(Shares)



# Shares['IBM'] = 111.11
# Shares['GOOG'] = 523.32 



# yahoo = Share('YHOO')
# openingPrice = yahoo.get_open()
# currentPrice = yahoo.get_price()
# historicalData = yahoo.get_historical('2015-01-01', '2015-12-31')

# ibm = Share('IBM')
# openingPrice = ibm.get_open()
# currentPrice = ibm.get_price()
# historicalData = ibm.get_historical('2015-01-01', '2015-12-31')

# stock = Share('CUDA')
# openingPrice = stock.get_open()
# currentPrice = stock.get_price()
# historicalData = stock.get_historical('2015-01-01', '2015-12-31')

        # Shares['YHOO'] = {}

        # Shares['YHOO']['object'] = Share('YHOO')
        # Shares['YHOO']['open'] = Shares['YHOO']['object'].get_open() 
        # Shares['YHOO']['price'] = Shares['YHOO']['object'].get_price()

# Shares['IBM'] = {}

# Shares['IBM']['object'] = Share('IBM')
# Shares['IBM']['open'] = Shares['IBM']['object'].get_open() 
# Shares['IBM']['price'] = Shares['IBM']['object'].get_price()

# for key in Shares:
#     print(key,Shares[key])
#     for subkey in Shares[key]:
#         print(subkey,Shares[key][subkey])