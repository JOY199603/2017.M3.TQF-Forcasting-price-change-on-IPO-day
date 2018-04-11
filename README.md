# Forecasting the Price Change on IPO day

## 1. Team Member
	Zhou Yujin
	1701213169

## 2. Data Set
* The data set was obtained and processed by Python from the __open API with WIND__. 
* I've collected all the A-shares and choosen __1837__ stocks whose IPO dates were after 2010
* There are __14__ variables of these stocks:
  * __industry_gics__: the belonging industry of the stock by the wind industry classification,which is similar to the GICS
  * __mkt__: the board of the stock,like main board,ChiNext,etc
  * __backdoor__: whether the stock is IPO by back-door listing
  * __ipo_date__: the ipo date
  * __ipo_price__: the ipo price
  * __ipo_amount__: the ipo amount
  * __ipo_collection__: the money raised by IPO
  * __ipo_netcollection__: the money raised by IPO munis the cost
  * __ipo_puboffrdate__: the public announcement date of IPO
  * __ipo_leadundr__: the main investment bank to assist the IPO
  * __ipo_type__: the IPO type 
  * __ipo_expense__: the expense of IPO
  * __ipo_pctchange__: the return of the stock on the IPO day
  * __ipo_listdayvolume__: the trading volume of the stock on the IPO day
		
* The ipo_pctchange and ipo_listdayvolume are the response variables

## 3. Plan
* Using different machine learning method to find which features have significant impact to the price change and trading volume on IPO day and try to find the financial explain for this.
* Try to predict the price change of stocks that IPO in 2017 by trainning these stocks IPO between 2010 to 2016.# 2017.M3.TQF-Forcasting price change on IPO day
