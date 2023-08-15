# Import all necessary libraries 
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


# Define the URL of the web page that contains the list of NASDAQ 100 companies
url = "https://www.cnbc.com/nasdaq-100/"


# Create an empty list to store the company symbols
symbols = []

#scrape symbols functions
def scrape_symb(url):

    #set up selenium
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certifiate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('headless')

    #chrome path ready
    chrome_path= r"C:\Desktop\chromedriver.exe"
    service = Service(executable_path=chrome_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    #wait for the web driver
    wait =WebDriverWait(driver,2)

    #open the url 
    driver.get(url)

    #wait 5 seconds
    time.sleep(5)
    
    # Create a BeautifulSoup object from the response text
    soup = BeautifulSoup(driver.page_source, features = "lxml")

    #get all the rows from the table
    rows = soup.select(selector=".BasicTable-symbolName")

    #make an array that holds all the symbols
    symbols_final=[]

    #iterate through the rows
    for row in rows:
        #get the text of each row 
        symbols_final.append(row.getText())

    #return the final list of symbols
    return symbols_final

#have a function that changes strings in to a float
def is_float(s):

    locale.setlocale(locale.LC_ALL, '')

    #try changing each string into a float
    try:
        #if possible, return true 
        locale.atof(s)
        return True
    except ValueError:
        #if a Value Error is thrown, return false
        return False

#scrape the prices
def scrape_p(url):

    #set up selenium 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certifiate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('headless')

    #prep the chrome driver 
    chrome_path= r"C:\Desktop\chromedriver.exe"
    service = Service(executable_path=chrome_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    #wait 2 seconds for the chrome driver to load
    wait =WebDriverWait(driver,2)

    #get up the url
    driver.get(url)

    #wait 5 seconds for the url to load
    time.sleep(5)
    
    # Create a BeautifulSoup object from the response text
    soup = BeautifulSoup(driver.page_source, features = "lxml")

    #get the table value
    rows = soup.select(selector=".BasicTable-unchanged.BasicTable-numData")
    
    #make an array of final prices
    price_final=[]

    locale.setlocale(locale.LC_ALL, '')

    #iterate through all the rows
    for row in rows:

        #get the values of each row
        temp= row.getText()

        #check to make sure that the value can be a float
        if is_float(temp):

            #add the price as a float into the price final
            price_final.append(locale.atof(temp))
    #return the final price
    return price_final


