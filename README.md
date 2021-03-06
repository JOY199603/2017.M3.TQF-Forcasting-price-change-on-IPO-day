
# Forecasting the Price Change on IPO day

## 1. Team Member
	Zhou Yujin
	1701213169
## 2. Background
* The stocks almost have a large return on their IPO day. What factors have impact on the return? whether we can forecast the return by finding proper features?
<div align=center><img width="500" height="300" src="https://github.com/JOY199603/2017.M3.TQF-Forcasting-price-change-on-IPO-day/blob/master/images/IPOPROCESS.png"/></div>
<div align=center><img width="700" height="300" src="https://github.com/JOY199603/2017.M3.TQF-Forcasting-price-change-on-IPO-day/blob/master/images/policychange.png"/></div>

## 3. Data Set
* The original data set was obtained and processed by Python from the __open API with WIND__. 
* I've collected all the A-shares and choosen __1828__ stocks whose IPO dates were after 2010
* There are __12__ variables of these stocks:

Variables | Description
-------|---------
industry_gics	| the belonging industry of the stock by the wind industry classification,which is similar to the GICS
mkt		| the board of the stock,like main board,ChiNext,etc
backdoor	| whether the stock is IPO by back-door listing
ipo_date	| the ipo date
ipo_price	| the ipo price
ipo_puboffrdate	| the public announcement date of IPO
ipo_amount	| the ipo amount
ipo_leadundr	| the main investment bank to assist the IPO
ipo_type	| the IPO type 
ipo_expense	| the expense of IPO
ipo_pctchange	| the return of the stock on the IPO day
ipo_npctchange	| the return of the stock for the first 10-days
ipo_turn	| the turnover rate of the stock on the IPO day
ipo_nturn	| the turnover rate of the stock for the first 10-days
		
* The ipo_pctchange and ipo_listdayvolume are the response variables

* [Original Data Set](https://github.com/JOY199603/2017.M3.TQF-Forcasting-price-change-on-IPO-day/blob/master/alldata.csv)

<div align=center><img width="500" height="300" src="https://github.com/JOY199603/2017.M3.TQF-Forcasting-price-change-on-IPO-day/blob/master/images/x&y.png"/></div>

## 4. Model
* (1) Define the fuctions we need in the model. Like calculate the confusion matrix, draw the roc curve.
* (2) Preprocess the Data: Deal with nominal and ordinal features,divide data into train and test set.
* There are too much dummy variables. We use random forest to access the feature importance.
<div align=center><img width="500" height="300" src="https://github.com/JOY199603/2017.M3.TQF-Forcasting-price-change-on-IPO-day/blob/master/images/importance.png"/></div>
* (3) Using linear regression to do the regression to the continuous variable. Find the p-value and coefficient of every features.
<div align=center><img width="400" height="700" src="https://github.com/JOY199603/2017.M3.TQF-Forcasting-price-change-on-IPO-day/blob/master/images/stat.png"/></div>
Most variables are significant by their P-value;
The ipo-price and ipo-time have negative impact to the return;
The stocks on Main-board are tend to have smaller return.

* (4)Transfer the continuous return to discrete labels and Use lostic regrssion,SVM,decision tree,random forest,KNN,neural network to train the model and compute the confusion matrix and ROC curve and auc. Compare the result.
<div align=center><img width="800" height="400" src="https://github.com/JOY199603/2017.M3.TQF-Forcasting-price-change-on-IPO-day/blob/master/images/readme.png"/></div>

Models |Mean AUC
-------|---------
Decision Tree	| 0.644
Logistic Regression	| 0.669
KNN	| 0.603
SVM	| 0.863
Neural Network	| 0.772

## 5. Summary
Model result:
 * (1) PCA has no improvement to this data
 * (2) By using K-fold and calculating the mean auc, all the model has mean auc above 0.6
Neural network&svm has significant better result 0.772 and 0.863

Features impact:
 * (1) Using the randon forest to test the importance of variables and find that backdoor、IPO-type、Investment Banks are more unimpotant.
 * (2) IPO_DATE，IPO_PRICE，IPO_AMOUNT，IPO_EXPENSE，and IPO_board have more significant impact to the return
 * (3) The IPO_PRICE and IPO_TIME have negative impact to the return.
 * (4) The stocks on Main-board are tend to have smaller return
 * (5) The return are going to be higher year after year. A share investors all believe the return on ipo day is high, more and more investors are trend to buy the 'new stocks'
 * (6) Some industries tends to have significant higher return: Public utility,health care, Consumer Discretionary,energy. Most these industries are emerging industry
 * (7) Investment banks like 中原证券 中国银河证券 首创证券 华安证券 兴业证券 have higher return, which means these investment banks tend to undervalue the stocks. 
## Reference:
* python-machine-learning-book-2nd-edition 
* [基于SVM的IPO首日投资策略分析(IPO Stock Price Forecasting Using Support Vector Machines)](http://xueshu.baidu.com/s?wd=paperuri%3A%287bd767e78dfed152c735ed0b0a1d2f5a%29&filter=sc_long_sign&tn=SE_xueshusource_2kduw22v&sc_vurl=http%3A%2F%2Fkns.cnki.net%2FKCMS%2Fdetail%2Fdetail.aspx%3Ffilename%3Dxtyy201310042%26dbname%3DCJFD%26dbcode%3DCJFQ&ie=utf-8&sc_us=16091207344911522734)
