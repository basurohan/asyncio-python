import asyncio
import aiohttp
import time

url = 'https://alpha-vantage.p.rapidapi.com/query'

querystring = {
    "interval": "5min",
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "",
    "datatype": "json",
    "output_size": "compact"
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


def get_tasks(session):
    tasks = []
    for symbol in symbols:
        querystring[symbol] = symbol
        tasks.append(session.request(method='GET', url=url, params=querystring, headers=headers, ssl=False))
    return tasks


async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.json())


start = time.time()
"""
loop = asyncio.get_event_loop()
loop.run_until_complete(get_symbols())
loop.close()
"""
# The above can be written in one line only
asyncio.run(get_symbols())
end = time.time()
total_time = end - start
print(f'It took ${total_time} seconds to make ${len(symbols)} API calls')
print('You did it!')
