# William Schaffer
# SPYTweets
# https://github.com/wschaf

# STEP 1: Get the current mark price of $SPY using TD Ameritrade API.
# STEP 2: Tweet something using the Twitter API.
# STEP 3: Combine STEP 1 and STEP 2 to tweet about $SPY pricing.

# STEP 1: Get the current mark price of $SPY using TD Ameritrade API.

#   requests contains library for HTTP functionality.
import requests

#   config contains API authentication strings.
from config import *

TDQuoteEndpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/quotes".format("SPY")

TDQuotePayload = { "apikey": TDapikey}



print()
print()
test = requests.get(url = TDQuoteEndpoint, params = TDQuotePayload)
data = test.json()
print("The current price of {}, {}, is: ${}".format(data['SPY']['symbol'], data['SPY']['description'], data['SPY']['mark']))
print()
print()