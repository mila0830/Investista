# Import the libraries
import requests

from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC

import time

import locale

companies = ['ABNB', 'AMD', 'AMZN', 'TEAM', 'ADSK', 'BKR', 'CRWD', 'DDOG', 'DXCM', 'EBAY', 'ENPH', 'ILMN', 'MRVL', 'JD', 'MRNA', 'PANW', 'PDD', 'SGEN', 'TSLA', 'WBD', 'WDAY', 'ZM', 'ZS']
# Define the URL of the web page that contains the list of NASDAQ 100 companies
#url = "https://finance.yahoo.com/quote/{0}/analysis?p={0}"


#function for scraping the eps annual growth
def scrape_growth(companies):
    #make an array to hold all data
    data = {}

    #iterate through all the other companies
    for c in companies: 

        #set up the url ready
        url = "https://finance.yahoo.com/quote/{0}/analysis?p={0}".format(c)

        #open up chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-certifiate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument('headless')

        #set up chrome path and driver
        chrome_path= r"C:\Desktop\chromedriver.exe"
        service = Service(executable_path=chrome_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        #wait for driver to open
        wait =WebDriverWait(driver,2)

        #open url and wait to load
        driver.get(url)
        time.sleep(5)

        #have a variable to hold the body of the table
        tbody= driver.find_element(By.XPATH, '//*[@id="Col1-0-AnalystLeafPage-Proxy"]/section/table[6]/tbody')
        
        #have a variable hold the counter
        counter = 0

        #iterate through all the table rows
        for tr in tbody.find_elements(By.XPATH, '//tr'):

            #put all the values of the table
            row = [item.text for item in tr.find_elements(By.XPATH,'.//td')]

            #retrieve just the annual growth for next 5 years 
            if counter == 34:
                #add that value to the data array
                data[c]= (row[1])
                print(row[1])

            #add to the counter
            counter +=1
    print(data)
    return data


    #soup = BeautifulSoup(driver.page_source, features = "lxml")
    #rows = soup.select(selector=".BasicTable-symbolName")
    
    """
    # Create a BeautifulSoup object from the response text
    soup = BeautifulSoup(driver.page_source, features = "lxml")
    rows = soup.select(selector=".BasicTable-symbolName")
    symbols_final=[]
    for row in rows:
        symbols_final.append(row.getText())
    """
"""
for c in companies:
    url = "https://finance.yahoo.com/quote/{0}/analysis?p={0}".format(c)
    scrape_growth(url, c)
"""

scrape_growth(companies)


"""
#works but doesn't have growth data
import requests

url = "https://yfapi.net/v6/finance/quote"

querystring = {"symbols":"AAPL,BTC-USD,EURUSD=X"}

headers = {
    'x-api-key': "oUwiBK6MSP8uvPfnJ5wFH8LyRBGmC3Wq3d6H6AGb"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

"""

