import finnhub
import pandas as pd
import yfinance as yf


finnhub_client = finnhub.Client(api_key="cj4qb51r01qq6hgdoaogcj4qb51r01qq6hgdoap0")



#print(finnhub_client.general_news('general', min_id=0))
#all_data = finnhub_client.company_basic_financials('PEP', 'all')
price = finnhub_client.quote('APPL')
print(price)


appl=yf.Ticker("MSFT")
print(appl.info['sharesOutstanding'])


#print(msft.cashflow)
#print(msft.info['currentPrice'])

# Define the URL of the web page that contains the list of NASDAQ 100 companies
url = "https://markets.businessinsider.com/index/components/nasdaq_100"
url2="https://markets.businessinsider.com/index/components/nasdaq_100?p=2"

symbols=[]


print("START---------------------------------")
for symb in symbols:
    print(symb)
    tick=yf.Ticker(symb)
    print(tick.info['sharesOutstanding']) 
