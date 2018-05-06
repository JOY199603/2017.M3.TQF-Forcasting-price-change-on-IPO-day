# Forecasting the Price Change on IPO day

## 1. Team Member
	Zhou Yujin
	1701213169
## 2. Background
* The stocks almost have a large return on their IPO day. What factors have impact on the return? whether we can forecast the return by finding proper features?
## 3. Data Set
* The original data set was obtained and processed by Python from the __open API with WIND__. 
* I've collected all the A-shares and choosen __1828__ stocks whose IPO dates were after 2010
* There are __12__ variables of these stocks:
  * __industry_gics__: the belonging industry of the stock by the wind industry classification,which is similar to the GICS
  * __mkt__: the board of the stock,like main board,ChiNext,etc
  * __backdoor__: whether the stock is IPO by back-door listing
  * __ipo_date__: the ipo date
  * __ipo_price__: the ipo price
  * __ipo_amount__: the ipo amount
  * __ipo_puboffrdate__: the public announcement date of IPO
  * __ipo_leadundr__: the main investment bank to assist the IPO
  * __ipo_type__: the IPO type 
  * __ipo_expense__: the expense of IPO
  * __ipo_pctchange__: the return of the stock on the IPO day
  * __ipo_listdayvolume__: the trading volume of the stock on the IPO day
		
* The ipo_pctchange and ipo_listdayvolume are the response variables
* [Original Data Set](https://github.com/JOY199603/2017.M3.TQF-Forcasting-price-change-on-IPO-day/blob/master/alldata.csv)

## 3. Model
* Using linear regression to do the regression to the continuous variable.
* Try to predict the price change of stocks that IPO in 2017 by trainning these stocks IPO between 2010 to 2016.
## Reference:
* python-machine-learning-book-2nd-edition 
* [基于SVM的IPO首日投资策略分析(IPO Stock Price Forecasting Using Support Vector Machines)](http://xueshu.baidu.com/s?wd=paperuri%3A%287bd767e78dfed152c735ed0b0a1d2f5a%29&filter=sc_long_sign&tn=SE_xueshusource_2kduw22v&sc_vurl=http%3A%2F%2Fkns.cnki.net%2FKCMS%2Fdetail%2Fdetail.aspx%3Ffilename%3Dxtyy201310042%26dbname%3DCJFD%26dbcode%3DCJFQ&ie=utf-8&sc_us=16091207344911522734)
