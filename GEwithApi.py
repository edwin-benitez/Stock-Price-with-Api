#This program will get GE stock price
import requests

f = open("apiKey", "r")
API_KEY = f.readline()
r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GE&apikey=' + API_KEY)
result = r.json()
allDays = result['Time Series (Daily)']
singleDay = allDays['2019-01-04']
print("GE open stock price is " + singleDay['1. open'])
print("GE high stock price is " + singleDay['2. high'])
print("GE low stock price is " + singleDay['3. low'])
print("GE close stock price is " + singleDay['4. close'])
print("GE volume is " + singleDay['5. volume'])


