import finnhub
import pandas as pd
import yfinance as yf


finnhub_client = finnhub.Client(api_key="cj1em1hr01qhv0uhof90cj1em1hr01qhv0uhof9g")



#print(finnhub_client.general_news('general', min_id=0))
all_data = finnhub_client.company_basic_financials('PEP', 'all')
price = finnhub_client.quote('APPL')

print(all_data["metric"]["epsTTM"])
print(price)

msft=yf.Ticker("APPL")
print(msft.cashflow)
print(msft.info['currentPrice'])
