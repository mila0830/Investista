import finnhub
import pandas as pd
import yfinance as yf
import finnhub
import time
from yahoofinancials import YahooFinancials

def growth_annum(symbols):
    finnhub_client = finnhub.Client(api_key="cj4qb51r01qq6hgdoaogcj4qb51r01qq6hgdoap0")
    counter=0
    eps_growth = {}
    no_growth_num = []
    
    #retrieve the growth for the eps
    for i in range(len(symbols)):
        if counter == 15:
            time.sleep(20)
            counter=0
        
        value=finnhub_client.company_basic_financials(symbols[i], 'all')
        
        if 'epsGrowth5Y' in value['metric'].keys():
            eps_g= value['metric']['epsGrowth5Y']
            
            if eps_g == None:
                no_growth_num.append(symbols[i])
            elif eps_g != None:
                val= (1 + (eps_g/100)) ** (1/5)
                eps_growth[symbols[i]] = val
                
        counter+=1 
    return eps_growth, no_growth_num

