import finnhub
import pandas as pd
import yfinance as yf
from scrapesymb import scrape_symb
from scrapesymb import scrape_p
import finnhub
import time
from yahoofinancials import YahooFinancials

finnhub_client = finnhub.Client(api_key="cj4qb51r01qq6hgdoaogcj4qb51r01qq6hgdoap0")

symbols = ['ABNB', 'ALGN', 'AMD', 'CEG', 'AMZN', 'AMGN', 'AEP', 'ADI', 'ANSS', 'AAPL', 'AMAT', 'GEHC', 'ASML', 'TEAM', 'ADSK', 'ATVI', 'ADP', 'AZN', 'BKR', 'AVGO', 'BIIB', 'BKNG', 'CDNS', 'ADBE', 'CHTR', 'CPRT', 'CSGP', 'CRWD', 'CTAS', 'CSCO', 'CMCSA', 'COST', 'CSX', 'CTSH', 'DDOG', 'DXCM', 'FANG', 'DLTR', 'EA', 'EBAY', 'ENPH', 'ON', 'EXC', 'FAST', 'GFS', 'META', 'FI', 'FTNT', 'GILD', 'GOOG', 'GOOGL', 'HON', 'ILMN', 'INTC', 'INTU', 'ISRG', 'MRVL', 'IDXX', 'JD', 'KDP', 'KLAC', 'KHC', 'LRCX', 'LCID', 'LULU', 'MELI', 'MAR', 'MCHP', 'MDLZ', 'MRNA', 'MNST', 'MSFT', 'MU', 'NFLX', 'NVDA', 'NXPI', 'ODFL', 'ORLY', 'PCAR', 'PANW', 'PAYX', 'PDD', 'PYPL', 'PEP', 'QCOM', 'REGN', 'ROST', 'SIRI', 'SGEN', 'SBUX', 'SNPS', 'TSLA', 'TXN', 'TMUS', 'VRSK', 'VRTX', 'WBA', 'WBD', 'WDAY', 'XEL', 'ZM', 'ZS']


counter=0
eps_growth = []
#retrieve the growth for the eps
for i in range(len(symbols)):
    if counter == 15:
        time.sleep(20)
        counter=0
    print(symbols[i])
    value=finnhub_client.company_basic_financials(symbols[i], 'all')
    
    if 'epsGrowth3Y' in value['metric'].keys():
        eps_g= value['metric']['epsGrowth3Y']
        print(eps_g)
        eps_growth.append(eps_g)
    else:
        eps_growth.append('None')
    counter+=1

print(eps_growth)