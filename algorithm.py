import finnhub
import pandas as pd
import yfinance as yf
from scrapesymb import scrape_symb
from scrapesymb import scrape_p
from scrape_growth import scrape_growth
from growth import growth_annum
from growth import no_growth
from scrapesymb import is_float
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

#have a dict hold the earnings for each company
earnings_per_company={}

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
    earnings_per_company[symbols[i]]= earnings

    #add up the earnings in to a total earnings
    total_earnings += earnings

    #add to the counter
    counter+=1

#let the API sleep for 15 seconds
time.sleep(15)

#calculate the price/earnings for the Nasdaq 100
price_per_earnings = total_market_cap / total_earnings

#finding future growth rates

growth_dict, companies = growth_annum(symbols)


#the url for the annual growth
url = "https://finance.yahoo.com/quote/{0}/analysis?p={0}"

#get the growth from the companies using data scraping becuse not available in API
additional_dict= scrape_growth(companies)

#merge the two dictionaries
final_growth_dict= growth_dict | additional_dict


#form a dictionary of all the predicted earnings per company 
predicted_earnings_per_company = {}

#add up all the predicted total earnings per company
total_predicted_earnings_per_company = 0

#iterate through all the companies
for key in final_growth_dict:
    #calculate the predicted earnings for each company using the growth rates
    value= final_growth_dict[key] * earnings_per_company[key]
    #add that value to the dictionary 
    predicted_earnings_per_company[key] = value
    #add this to the total value of all the predicted earnings
    total_predicted_earnings_per_company += value

#calculate the growth rate
growth = ((total_predicted_earnings_per_company / total_earnings) -1 ) * 100

#calculate the price/earnings/growth 
peg = price_per_earnings / growth

#form a ticker to grab the 10-year Treasury Bond Yield
tick=yf.Ticker('^TNX')

#get the value 
treasury_yield= tick.info['previousClose']

#calculate the Benjamin Graham formula
ben_graham_number = (total_earnings * (8.5 + 2 * growth) * 4.4 ) / treasury_yield

#state if profitable if ben graham number is above current years market cap
if (ben_graham_number > total_market_cap):
    print("Invest today!")
    print("Today's price per earnings: " + str(price_per_earnings))
    print("Predicted price per earnings: " + str(total_predicted_earnings_per_company))
    print("Growth rate: " + str(growth))
    print("PEG: " + str(peg))
#state it isn't profitable to invest today if ben graham is less than market capitalization
else:
    print("Investment today is not worth it")
    print("Today's price per earnings: " + str(price_per_earnings))
    print("Predicted price per earnings: " + str(total_predicted_earnings_per_company))
    print("Growth rate: " + str(growth))
    print("PEG: " + str(peg))



    




