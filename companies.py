# Import the requests library to make web requests
import requests
# Import the BeautifulSoup library to parse the HTML content
from bs4 import BeautifulSoup

# Define the URL of the web page that contains the list of NASDAQ 100 companies
url = "https://markets.businessinsider.com/index/components/nasdaq_100"
url2="https://markets.businessinsider.com/index/components/nasdaq_100?p=2"

# Create an empty list to store the company symbols
symbols = []

def scrape(url):
    # Make a GET request to the URL and store the response object
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:

        # Create a BeautifulSoup object from the response text
        soup = BeautifulSoup(response.text, "html.parser")
        
        

        # Find the table element that has the class "table instruments"
        table = soup.find("table", class_="table table__layout--fixed")
       

        # Find all the table rows that have the class "table__row"
        rows = table.findChildren("tr")
        


        # Create an empty list to store the company symbols
        #symbols = []

        # Loop through each row and extract the company symbol
        for row in rows:
            # Find the table cell that contains the company symbol
            cell = row.find("td", class_="table__td table__td--big")
            


            # Check if the cell exists
            if cell:
                # Get the text content of the cell and strip any whitespace
                symbol = cell.text.strip()

                # Append the symbol to the list of symbols
                symbols.append(symbol)

        # Print the list of symbols
        return symbols
    else:
        # Print an error message if the request failed
        print("Error: sight doesn't work for scraping")



def scrape_p(url):
    #create an empty list to store the company price
    prices = [] 
    # Make a GET request to the URL and store the response object
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:

        # Create a BeautifulSoup object from the response text
        soup = BeautifulSoup(response.text, "html.parser")
        
        

        # Find the table element that has the class "table instruments"
        table = soup.find("table", class_="table table__layout--fixed")
       

        # Find all the table rows that have the class "table__row"
        rows = table.findChildren("tr")
        print(len(rows))
        


        # Create an empty list to store the company symbols
        #symbols = []

        # Loop through each row and extract the company symbol
        for row in rows:
            
            cell_p= row.find_all("td")
            

            if cell_p:
                price1=cell_p[1]
                print(price1)
                price = price1.text.strip()
                one_price=''
                for element in price:
                    if element != "\n":
                        one_price +=element
                    else:
                        break
                    

                prices.append(one_price)

        # Print the list of symbols
        
        return prices
    else:
        # Print an error message if the request failed
        print("Error: sight doesn't work for scraping")



