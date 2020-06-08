# SPYTweets
## Implementing a Bot Using Twitter and TD Ameritrade's APIs to check S&P 500 Pricing

#### Documentation located in: readme.md

#### William G. Schaffer
#### [Source Code On Github](https://github.com/wschaf/SPYTweets "Source Code On Github")


### Background:

I like to play with stocks. I also have been meaning to build a project in Python for a while. $SPY is an index fund that tracks performance of the Standard & Poors ( S&P ) 500, which is the 500 largest companies on the listed on the stock exchanges in the United States. When I check the prices for $SPY, I usually open an app on my phone or Google the word "SPY" to check the price.

### Goal

Implement a twitter bot that will check the current price of $SPY and tweet about it if the price rises or falls more than 1%.

- Make use of [Python](https://www.python.org/doc/ "Python")

- Make use of the [Twitter API](https://github.com/wschaf/SPYTweets "Source Code On Github")

- Make use of the [TD Ameritrade API](https://github.com/wschaf/SPYTweets "Source Code On Github")

### Improvements

If this continues to interest me beyond the minimum viable product, I plan to:

1. Scan SPY Call/Put option distribution for parity.

2. Implement paper trading and let the bot trade based on [MACD](https://en.wikipedia.org/wiki/MACD "Moving Average Convergence/Divergence")