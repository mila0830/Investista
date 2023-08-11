import finnhub
import pandas as pd
import yfinance as yf
from scrapesymb import scrape_symb
from scrapesymb import scrape_p
from scrape_growth import scrape_growth
from growth import growth_annum
from growth import no_growth
import finnhub
import time
from yahoofinancials import YahooFinancials

#use API key to prep Client
finnhub_client = finnhub.Client(api_key="cj4qb51r01qq6hgdoaogcj4qb51r01qq6hgdoap0")

#scrpe all the companies within the Nasdaq 100 with the following link
url_symb = "https://www.cnbc.com/nasdaq-100/"

#variable to hold symbol names
symbols=scrape_symb(url_symb)

#variable to hold prices for each company
prices=scrape_p(url_symb)

#have a variable to total the market capitalization
total_market_cap=0

#array to hold all companies market capitalization
market_caps=[]
print(symbols)
#itarate through each symbol
for symb in symbols:
    
    #form a ticker for each symbol
    tick=yf.Ticker(symb)
    
    #optain market capitlization
    market_cap= tick.info['marketCap']

    #add the market capitalization for each company into the array
    market_caps.append(market_cap)

    #add the market capitalization for each company to the total
    total_market_cap+= market_cap

#have an array hold the number of outstanding shares
outstanding_shares = []

#iterate through each company in the Nasdaq 100
for i in range(len(symbols)):

    #calculate the outstanding shares by dividing the market capitilzation by prices
    temp = market_caps[i]/prices[i]

    #add the number of outstanding shares to the array
    outstanding_shares.append(temp)

#make a counter to help with API limit calls
counter=0

#variable holds total earnings
total_earnings=0

#have an array hold the earnings for each company
earnings_per_company=[]

#iterate through the companies of the Nasdaq 100
for i in range(len(symbols)):
    
    #at every 15th company post pone the API call
    if counter == 15:
        time.sleep(20)
        counter=0

    #get the information about the company
    value=finnhub_client.company_basic_financials(symbols[i], 'all')
    
    #get the value of the eps of the company
    eps= value['metric']['epsTTM']

    #get the ernings by multiplying outstanding shares by eps
    earnings = outstanding_shares[i] * eps

    #add the earnings of each company to the list 
    earnings_per_company.append(earnings)

    #add up the earnings in to a total earnings
    total_earnings += earnings

    #add to the counter
    counter+=1

#let the API sleep for 15 seconds
time.sleep(15)



print(total_earnings)
print(total_market_cap)
print(outstanding_shares)
print(earnings_per_company)

#calculate the price/earnings for the Nasdaq 100
price_per_earnings = total_market_cap / total_earnings



#finding future growth rates

growth_dict = growth_annum(symbols)

companies= no_growth(symbols)

print(growth_dict)
print(companies)
#the url for the annual growth
url = "https://finance.yahoo.com/quote/{0}/analysis?p={0}"

#iterate through the list of companies that you don't already have 5y growth 
for c in companies:
    url = "https://finance.yahoo.com/quote/{0}/analysis?p={0}".format(c)
    scrape_growth(url)

#earnings next year
"""
earnings_next_year_total=0
for i in range(len(symbols)):
    temp = earnings_per_company[i] * (1 + (eps_growth[i]/100))
    earnings_next_year_total +=temp

price_growth_index= ((earnings_next_year_total / total_earnings) -1) * 100

print(price_growth_index)
"""