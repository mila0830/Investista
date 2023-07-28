import finnhub
import pandas as pd
import yfinance as yf
from companies import scrape
from companies import scrape_p

finnhub_client = finnhub.Client(api_key="cj1em1hr01qhv0uhof90cj1em1hr01qhv0uhof9g")



#print(finnhub_client.general_news('general', min_id=0))
all_data = finnhub_client.company_basic_financials('PEP', 'all')
price = finnhub_client.quote('APPL')

print(all_data["metric"]["epsTTM"])
print(price)

msft=yf.Ticker("APPL")
#print(msft.cashflow)
#print(msft.info['currentPrice'])

# Define the URL of the web page that contains the list of NASDAQ 100 companies
url = "https://markets.businessinsider.com/index/components/nasdaq_100"
url2="https://markets.businessinsider.com/index/components/nasdaq_100?p=2"

first_half_symbols=scrape("https://markets.businessinsider.com/index/components/nasdaq_100")
second_half_symbols=scrape("https://markets.businessinsider.com/index/components/nasdaq_100?p=2")

first_half_prices=scrape_p("https://markets.businessinsider.com/index/components/nasdaq_100")
second_half_prices=scrape_p("https://markets.businessinsider.com/index/components/nasdaq_100?p=2")

print(len(first_half_prices))
print(len(second_half_prices))