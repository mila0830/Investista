from polygon import RESTClient

client = RESTClient(api_key="IdVnaT5lcbgEZCmKTX5yXj7lSexeuQss")

ticker = "APPL"

quotes = client.list_quotes(ticker=ticker, timestamp="2022-01-04")
for quote in quotes:
    print(quote)