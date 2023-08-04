# Import the requests library to make web requests
import requests
# Import the BeautifulSoup library to parse the HTML content
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

def scrape_symb(url):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certifiate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')

    chrome_path= r"C:\Desktop\chromedriver.exe"
    service = Service(executable_path=chrome_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    wait =WebDriverWait(driver,2)

    driver.get(url)
    time.sleep(5)
    
    # Create a BeautifulSoup object from the response text
    soup = BeautifulSoup(driver.page_source, features = "lxml")
    rows = soup.select(selector=".BasicTable-symbolName")
    symbols_final=[]
    for row in rows:
        symbols_final.append(row.getText())

    #check if dublicates in list
    return symbols_final
def is_float(s):
    locale.setlocale(locale.LC_ALL, '')
    try:
        locale.atof(s)
        return True
    except ValueError:
        return False

def scrape_p(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certifiate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')

    chrome_path= r"C:\Desktop\chromedriver.exe"
    service = Service(executable_path=chrome_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    wait =WebDriverWait(driver,2)

    driver.get(url)
    time.sleep(5)
    
    # Create a BeautifulSoup object from the response text
    soup = BeautifulSoup(driver.page_source, features = "lxml")
    rows = soup.select(selector=".BasicTable-unchanged.BasicTable-numData")
    
    
    price_final=[]

    #could try this instead of all the locale stuff
    #float("123,456.908".replace(',',''))

    locale.setlocale(locale.LC_ALL, '')

    for row in rows:
        temp= row.getText()
        if is_float(temp):
            price_final.append(locale.atof(temp))
        #print(row)
        # print(row.getText())
    

    return price_final



"""
def scrape_weight(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certifiate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')

    chrome_path= r"C:\Desktop\chromedriver.exe"
    service = Service(executable_path=chrome_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    #WebDriverWait(driver,20).until(EC.invisibility_of_element((By.XPATH,'./html/body/div[3]/div/main/div[2]/article/div[3]/div[1]/div/div/div[3]/div[2]/div[2]/div/button')))
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, './html/body/div[3]/div/main/div[2]/article/div[3]/div[1]/div/div/div[3]/div[2]/div[2]/div/button'))).click()

    WebDriverWait(driver,20)
    time.sleep(10)

    cookies=driver.find_element(By.ID, "onetrust-accept-btn-handler")
    cookies.click()

    button=driver.find_element(By.CLASS_NAME, "nasdaq-screener__form-button--download")
    button.click()
    time.sleep(20)

    #button=driver.find_element(By.XPATH,'./html/body/div[3]/div/main/div[2]/article/div[3]/div[1]/div/div/div[3]/div[2]/div[2]/div/button')
    #button.click()
scrape_weight("https://www.nasdaq.com/market-activity/stocks/screener")
#print(scrape_weight("https://www.slickcharts.com/nasdaq100"))
print(scrape_symb(url))

"""
