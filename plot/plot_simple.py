import matplotlib.pyplot as plt
import random
from yahoo_finance import Share


Shares = {}

Shares['YHOO'] = {} 
Shares['YHOO']['object'] = Share('YHOO')
Shares['YHOO']['open'] = Shares['YHOO']['object'].get_open() 
Shares['YHOO']['price'] = Shares['YHOO']['object'].get_price()
Shares['YHOO']['historical'] = Shares['YHOO']['object'].get_historical('2015-01-01', '2015-12-31')


#history = Shares['YHOO']['historical']


Y = []

for day in Shares['YHOO']['historical']:
    Y.append(day['High'])


Shares['GOOG'] = {} 
Shares['GOOG']['object'] = Share('GOOG')
Shares['GOOG']['open'] = Shares['GOOG']['object'].get_open() 
Shares['GOOG']['price'] = Shares['GOOG']['object'].get_price()
Shares['GOOG']['historical'] = Shares['GOOG']['object'].get_historical('2015-01-01', '2015-12-31')

#history = Shares['GOOG']['historical']

G = []

for day in Shares['GOOG']['historical']:
    G.append(day['High'])


Shares['IBM'] = {} 
Shares['IBM']['object'] = Share('IBM')
Shares['IBM']['open'] = Shares['IBM']['object'].get_open() 
Shares['IBM']['price'] = Shares['IBM']['object'].get_price()
Shares['IBM']['historical'] = Shares['IBM']['object'].get_historical('2015-01-01', '2015-12-31')

#history = Shares['GOOG']['historical']

D = []

for day in Shares['IBM']['historical']:
    D.append(day['High'])
    
print(D)

plt.plot(Y)
plt.plot(G)
plt.plot(D)
plt.ylabel('Stock Price')
plt.title('YHOO GOOG IBM')
plt.xlabel('Julian Day')
plt.show()

