import urllib2
import urllib
import csv

# Specify the url
"""
"","year","month","intent","police","sex","age","race","hispanic","place","education"

Possible Queries:

Query: Determine all the different "intents"
Output:
    Homicide
    Suicide
    Undetermined
    etc.
Query: Count the occurences of each "intent"
Output:
    xxxx Homicides
    xxxx Suicides
    xxxx etc.
Query: Count the distinct races
Output:
    xxxx Asian/Pacific Islander
    xxxx Black
    xxxx Hispanic
    xxxx Native American/Native Alaskan
    xxxx White
    xxxx etc.
Query: Find the oldest victim
Query: Find the youngest victim

"""
url = 'https://raw.githubusercontent.com/fivethirtyeight/guns-data/master/full_data.csv'

# This packages the request (it doesn't make it) 
request = urllib2.Request(url)

# Sends the request and catches the response
response = urllib2.urlopen(request)

# Extracts the response
file = response.read().split("\n")

for f in file:
    f = f.replace("'","")
    f = f.replace('"','')
    items = f.split(',')
    print(items)

