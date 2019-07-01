# De-crypting cryptocurrency 

Cryptocurrecies are highly volatile assets compared to other asset classes, which becomes a challenge in creating models and making predictions as to when to "invest". For instance, "Bitcoin" is capable of volatility in the form of 10x changes in price versus the U.S. dollar. Also, all the criptocurrencies' correlation gradually increases, as described in this [article](https://www.investopedia.com/articles/investing/052014/why-bitcoins-value-so-volatile.asp).

Hence, we propose a novel way to investigate cryptocurrency valuation by assessing any correlations of these cryptocurrencies at short term periods.  

## De-crypted App 
A web application that allows users to explore trends and correlations between the exchange rates of several cryptocurrencies relative to bitcoin, including historical data, and the option to query a custom-built API live feed. Cryptocurrencies used: ETH (Ether), XRP (Ripple), LTC (litecoin), BCC (Bitcoin Cash),E OS (Eos), BNB (Binance Coin), and three minor cryptocurrencies. 

[Live app](https://de-crypted.herokuapp.com/)

Built using [AWS RDS](https://aws.amazon.com/rds/) and [AWS EC2](https://aws.amazon.com/ec2/)
- [Live data feed](https://flask-crypto.herokuapp.com/livedata)
- [Live ticker price](https://flask-crypto.herokuapp.com/api/v1.0/cryptosies)

On the homepage, there is a "live" data feed for each of the 6 cryptocurrencies, including ticker price and the relevant exchange rates from the past 7 days. 

The real magic is found on the Explore page, where users can request data from a specific time frame (of the past 7 days) between 2 cryptocurrencies, by which the page generates data visualizations, including a line and boxplot of each cryptocurrency, and a scatterplot to represent any correlations with Pearson's r. 

For the comparison page, we prepared a bitcoin correletion data for the real "promising" investers, where you can see 3 less corrlated currencies and their trends.

We designed this app with the intention of discovering patterns in trends in the sporadic and seemingly unpredictable realm of cryptocurrency and presenting these patterns in a visibly informative way.

### Data & App Design Roadmap
<img src="https://raw.githubusercontent.com/ying-li-python/de-crypted/master/static/images%20/data-pipeline.png" width="80%" height="80%">

### Resources: 
- Historical data: [Kaggle](https://www.kaggle.com/philmohun/cryptocurrency-financial-data)
- Live ticker and price information: [Binance API](https://www.binance.com/en)
- Cryptocurrencies by Market Cap: [Coin Market Cap](https://coinmarketcap.com/) (Only for minor cryptocurrencies)

### Additional Databases:
- Local sqlite file (for 1 year history)

### Authors
Nick Setnik, Donish Cushing, Naoko Okada, Priya R., Ying Li

### Github sources
- [Live data feed](https://github.com/Priyarag/flaskapptest)
- [Live app](https://github.com/ying-li-python/de-crypted/)
- [Core app design](https://github.com/nsetnik0703/Crypto-Live)

### Inspiration
![Image of picture1](https://github.com/nsetnik0703/Crypto-Live/blob/master/Proposal/images/Picture1.png)
![Image of picture2](https://github.com/nsetnik0703/Crypto-Live/blob/master/Proposal/images/Picture2.png)
![Image of altcoin_prices_combined](https://github.com/nsetnik0703/Crypto-Live/blob/master/Proposal/images/altcoin_prices_combined.png)
