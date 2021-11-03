import requests
import time

url = 'https://alpha-vantage.p.rapidapi.com/query'

querystring = {
    "interval":"5min",
    "function":"TIME_SERIES_INTRADAY",
    "symbol": None,
    "datatype":"json",
    "output_size":"compact"
}

symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP',
           'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP',
           'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP',
           'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP',
           'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP',
           'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP', 'AAPL', 'GOOG', 'TSLA', 'MSFT', 'PEP']

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
}

results = []

start = time.time()
for symbol in symbols:
    print(f'Working on ${symbol}')
    querystring[symbol] = symbol
    response = requests.request(method='GET', url=url, params=querystring, headers=headers)
    results.append(response.json)
end = time.time()
total_time = end - start

print(f'It took ${total_time} seconds to make ${len(symbols)} API calls')
print('You did it!')


