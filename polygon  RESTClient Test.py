from polygon import RESTClient
import mplfinance as mpf
import pandas as pd

client = RESTClient(api_key="mk2WSHh93k_lKEW1JyEZUxFZDXVZkCWA")

ticker = "AAPL"

# List Aggregates (Bars)
aggs = []
for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2024-01-01", to="2024-03-13", limit=50000):
    aggs.append(a)


# Python3 code here creating class
class bar:
	def __init__(self, date, open, high, low, close, volume):
		self.date = date
		self.open = open
		self.high = high
		self.low = low
		self.close = close
		self.volume = volume

	def __str__(self):
		return f"{self.date}{self.open}"
	
	def __repr__(self):
		return str(self)

		
# creating list
bars = []

# appending bars to list

for entry in aggs:
	bars.append([entry.timestamp, entry.open, entry.high, entry.low, entry.close, entry.volume])
	#bars.append(bar(entry.timestamp, entry.open, entry.high, entry.low, entry.close, entry.volume))

import csv

# field names 
fields = ['Date' ,'Open' ,'High' ,'Low' ,'Close' ,'Volume'] 


with open('GFG', 'w') as f:
	
	# using csv.writer method from CSV package
	write = csv.writer(f)
	
	write.writerow(fields)
	write.writerows(bars)

