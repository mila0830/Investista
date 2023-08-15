# Import the libraries
import requests

from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC

from scrapesymb import is_float

import time

import locale


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
                val = row[1]
                val = val.replace('%','')

                locale.setlocale(locale.LC_ALL, '')

                #add that value to the data array
                if val != 'N/A':
                    val2= locale.atof(val)
                    val3 = (val2/100 + 1)
                    data[c]=val3

                else:
                    data[c] = 1
                

            #add to the counter
            counter +=1
    
    return data

