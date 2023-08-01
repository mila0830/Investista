import requests
from bs4 import BeautifulSoup

# Fetch the HTML content of the page
response = requests.get("https://www.nasdaq.com/solutions/nasdaq-100/companies")

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Find the table element that has the class "BasicTable-table"
table = soup.find("table", class_="BasicTable-table")

# Find all the table rows within the table element
rows = table.find_all("tr")

# Initialize an empty list to store the symbols
symbols = []

# Loop through each row
for row in rows:
    # Find the table cell that has the class "BasicTable-symbol"
    cell = row.find("td", class_="BasicTable-symbol")
    # Extract the text from the cell and append it to the symbols list
    symbols.append(cell.get_text())

# Print the symbols list or convert it to an array as needed
print(symbols)
