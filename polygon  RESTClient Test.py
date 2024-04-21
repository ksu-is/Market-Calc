from polygon import RESTClient

client = RESTClient(api_key="mk2WSHh93k_lKEW1JyEZUxFZDXVZkCWA")

ticker = "AAPL"

# List Aggregates (Bars)
aggs = []
for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2024-01-01", to="2024-03-13", limit=50000):
    aggs.append(a)

print(aggs)

