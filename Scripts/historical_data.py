import requests
import json 

class HistoricalData():

	def get(self,symbol,crypto,market,data_range,interval):
		
		""" Function to get historical data of a financial instrument
			symbol : Ticker
			crypto : 1 if you want data of crypto otherwise 0
			market : for stock only, NS for NSE, BO for BSE
			data_range : Valid ranges -> 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
			interval : Valid intervals -> 5m, 15m, 30m, 60m, 1d
		"""
		if crypto == 0:
			URL = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}.{market}?symbol={symbol}.{market}&range={data_range}&useYfid=true&interval={interval}&includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&region=US&crumb=H.D9hubFl7k&corsDomain=finance.yahoo.com"
		
		else:
			URL = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}-USD?symbol={symbol}-USD&range={data_range}&useYfid=true&interval={interval}&includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&region=US&crumb=H.D9hubFl7k&corsDomain=finance.yahoo.com"
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}

		print(f"Trying to retrieve data: {symbol}")
		self.res = requests.get(URL, headers=headers)

		clean_data = self.clean()
		return clean_data

	def clean(self):

		""" cleans the retreived data 
		 	returns a dictionary with keys: volume, O, H, L, C
		"""
		if self.res.status_code == 200:

			print("Data retrive succesfull")
			data = json.loads(self.res.text)
			subset = dict(data['chart']['result'][0])
			rows = dict(subset['indicators']['quote'][0])

			clean_data = {
				"volume": rows['volume'],
				"open": rows['open'],
				"high": rows['high'],
				"low": rows['low'],
				"close": rows['close']
			}

			return clean_data
		
		else:
			print("Data retrive fail. Err code:",self.res.status_code)
			exit()
