import finnhub
import pandas as pd
import yfinance as yf
from scrapesymb import scrape_symb
from scrapesymb import scrape_p
import finnhub
import time
from yahoofinancials import YahooFinancials

#THIS WORKS
#abnb = yf.Ticker('ABNB')
#info = abnb.info
#print(info['earningsGrowth'])

abnb = yf.Ticker('ABNB')
financials = abnb.get_actions()
print(financials)

#try YH Finance



#analysis = tsla._analysis

#print(analysis._data)



#come BACK TO THIS!!
#ticker = yf.Ticker("MSFT")
#print(ticker.earnings_forecasts)
"""
It seems that the 'recommendations' feature is not currently implemented in the yfinance library for fetching data from the Yahoo API. The error you encountered indicates that this specific functionality is not available.

To work around this issue, you can try using other libraries or APIs that provide recommendations data for stocks. Some popular alternatives include Alpha Vantage, Finnhub, or using a financial data provider such as Bloomberg Terminal or Refinitiv Eikon.

Here's an example of using the Alpha Vantage API to fetch stock recommendations for Tesla (TSLA):
TRy it and let me know

import requests

API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'
symbol = 'TSLA'

url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}'

response = requests.get(url)
data = response.json()

if 'RecommendationKey' in data:
recommendation = data['RecommendationKey']
print(f"Recommendation for {symbol}: {recommendation}")
else:
print("Recommendation data not available.")
"""
def growth_annum(symbols):
    finnhub_client = finnhub.Client(api_key="cj4qb51r01qq6hgdoaogcj4qb51r01qq6hgdoap0")
    counter=0
    eps_growth = {}
    no_growth_num = []
    no_growth_num2 = []
    #retrieve the growth for the eps
    for i in range(len(symbols)):
        if counter == 15:
            time.sleep(20)
            counter=0
        print(symbols[i])
        value=finnhub_client.company_basic_financials(symbols[i], 'all')
        
        if 'epsGrowth5Y' in value['metric'].keys():
            eps_g= value['metric']['epsGrowth5Y']
            if eps_g == None:
                no_growth_num.append(symbols[i])
            elif eps_g != None:
                val= (1 + (eps_g/100)) ** (1/3)
                eps_growth[symbols[i]] = val
                print(val)
        counter+=1 
    return eps_growth, no_growth_num

def no_growth(symbols):
    finnhub_client = finnhub.Client(api_key="cj4qb51r01qq6hgdoaogcj4qb51r01qq6hgdoap0")
    counter=0
    
    no_growth_num = []
    
    #retrieve the growth for the eps
    for i in range(len(symbols)):
        if counter == 15:
            time.sleep(20)
            counter=0
        print(symbols[i])
        value=finnhub_client.company_basic_financials(symbols[i], 'all')
        
        if 'epsGrowth5Y' in value['metric'].keys():
            eps_g= value['metric']['epsGrowth5Y']
            if eps_g == None:
                no_growth_num.append(symbols[i])
    return no_growth_num

