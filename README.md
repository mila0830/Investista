# Nasdaq 100 Earning Analysis
## Description
The following project uses Finnhub and Yahoo Finance data to state the profitability of a current investment in the Nasdaq 100
## How to Use
Run the algorithm.py file to get a response if an investment in the Nasdaq 100 today is worth it

The main branch holds the final version of the earning analysis, however, it only contains Yahoo Finance predictions on the EPS 5Y growth. 

The YF-Finnhub-Data branch holds the final version of the earning analysis that takes into account a mix of Finnhub and Yahoo Finance's predictions on the EPS 5Y growth. This version runs much faster, but I found that the purely Yahoo Finance data provides more accurate and reliable predictions. Both versions tend to give the same overall result of if an investment is worth it or not just some calculations are different. 

Note: Runtime is greatly affected by the need to wait inbetween API calls becuase of not buying premium packages

## Resources Used
Yahoo Finance library, Finnhub API, CNBC, and Yahoo Finance website

## Financial Values Used 
Market prices, market capitalization per company, outstanding shares per company, earnings per company, total earnings, price per earnings, eps 5 year growth, total predicted earnings next 5 years (per annum), growth rate, price / earnings per growth, and Benjamin Graham number 
