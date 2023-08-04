from alpha_vantage.timeseries import TimeSeries

import pandas as pd

from io import BytesIO

import requests
import json

api_key = 'LAYA87GMLJPQCRJG'
#https://sec-api.io/docs/outstanding-shares-float-api#:~:text=The%20API%20returns%20the%20number,used%20for%20backtesting%20trading%20strategies. use this for number of outstanding shares
symbols=['MFTS', 'IBM']
for symb in symbols:
    url = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={}&apikey=LAYA87GMLJPQCRJG'.format(symb)
    r = requests.get(url)
    data = r.json()
    print(data)

url='https://api-v2.intrinio.com/companies/AAPL/shares_outstanding'
r = requests.get(url)
data = r.json()
print(data)



def earnings(ticker):
    base_url = "https://www.alphavantage.co/query?"
    url= "https://www.alphavantage.co/query?function=EARNINGS&symbol={}&apikey={}".format(ticker, api_key)
    response = requests.get(url)
    response_dict = response.json()
    print(response_dict)
    """
    res = requests.get(url=base_url, params={
    "function":"EARNINGS",
    "symbol":f'{stock}',
    'apikey':api_key})
    print(res)
    EPS = res.json()
    print(EPS)
    for i in range(0,len(EPS['annualEarnings'])-1):
        if i==0:
            df = pd.DataFrame.from_dict(EPS['annualEarnings'][i], orient = 'index')
        else:
            df_1 = pd.DataFrame.from_dict(EPS['annualEarnings'][i], orient = 'index')
            df = pd.merge(df, df_1, left_index = True, right_index = True)
    df = df.transpose()
    df['fiscalDateEnding'] = pd.to_datetime(df['fiscalDateEnding'])
    df[['reported_Annual_EPS']] = df[['reportedEPS']].apply(pd.to_numeric, errors = 'coerce')
    df = df.drop(columns = 'reportedEPS')
    df = df.set_index('fiscalDateEnding')
    return df
    """

value=earnings('APPL')
print(value)

#print(finnhub_client.general_news('general', min_id=0))
#all_data = finnhub_client.company_basic_financials('PEP', 'all')
#price = finnhub_client.quote('APPL')
#print(price)


#appl=yf.Ticker("MSFT")
#print(appl.info['sharesOutstanding'])


#print(msft.cashflow)
#print(msft.info['currentPrice'])

# Define the URL of the web page that contains the list of NASDAQ 100 companies
url = "https://markets.businessinsider.com/index/components/nasdaq_100"
url2="https://markets.businessinsider.com/index/components/nasdaq_100?p=2"

"""
for symb in symbols:
    yahoo_financials = YahooFinancials(symb)
    balance_sheet_data_qt = yahoo_financials.get_num_shares_outstanding(price_type='current')
    print(balance_sheet_data_qt)



"""

#this works but is very slow
from yahoofinancials import YahooFinancials

ticker = 'AAPL'
yahoo_financials = YahooFinancials(ticker)

balance_sheet_data_qt = yahoo_financials.get_num_shares_outstanding(price_type='current')
print(balance_sheet_data_qt)


