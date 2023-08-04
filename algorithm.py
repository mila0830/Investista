import finnhub
import pandas as pd
import yfinance as yf
from scrapesymb import scrape_symb
from scrapesymb import scrape_p
import finnhub
import time
from yahoofinancials import YahooFinancials

finnhub_client = finnhub.Client(api_key="cj4qb51r01qq6hgdoaogcj4qb51r01qq6hgdoap0")

value = finnhub_client.company_basic_financials('APPL', 'all')
print(value['metric']['epsGrowth5Y'])

url3 = "https://www.cnbc.com/nasdaq-100/"

symbols=scrape_symb(url3)
prices=scrape_p(url3)
total_market_cap=0
print(symbols)
print("START---------------------------------")


market_caps=[]
for symb in symbols:
    
    tick=yf.Ticker(symb)
    #print(tick.info)
    market_cap= tick.info['marketCap']
    market_caps.append(market_cap)
    total_market_cap+= market_cap

outstanding_shares = []
for i in range(len(symbols)):
    temp = market_caps[i]/prices[i]
    outstanding_shares.append(temp)
print(total_market_cap)
print(outstanding_shares)
    


counter=0
total_earnings=0
earnings_per_company=[]
for i in range(len(symbols)):
    print(symbols[i])
    if counter == 15:
        time.sleep(20)
        counter=0
    value=finnhub_client.company_basic_financials(symbols[i], 'all')
        
    eps= value['metric']['epsTTM']
    earnings = outstanding_shares[i] * eps
    earnings_per_company.append(earnings)
    total_earnings += earnings
    counter+=1

time.sleep(15)

counter=0
eps_growth = []
#retrieve the growth for the eps
for i in range(len(symbols)):
    if counter == 15:
        time.sleep(20)
        counter=0
    print(symbols[i])
    value=finnhub_client.company_basic_financials(symbols[i], 'all')
    
    if 'epsGrowth5Y' in value['metric'].keys():
        eps_g= value['metric']['epsGrowth5Y']
        print(eps_g)
        eps_growth.append(eps_g)
    else:
        eps_growth.append('None')
    counter+=1

print(eps_growth)


print(total_earnings)
print(total_market_cap)
print(outstanding_shares)
print(earnings_per_company)

price_per_earnings = total_market_cap / total_earnings

#earnings next year

earnings_next_year_total=0
for i in range(len(symbols)):
    temp = earnings_per_company[i] * (1 + (eps_growth[i]/100))
    earnings_next_year_total +=temp

price_growth_index= ((earnings_next_year_total / total_earnings) -1) * 100

print(price_growth_index)
