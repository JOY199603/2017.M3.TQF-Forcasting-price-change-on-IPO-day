# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 19:14:10 2018
GET DATA
@author: Joy
"""

import datetime
import numpy as np
import pandas as pd

#access to the API of WIND
from WindPy import * 
w.start()
setdate="2018-04-10"
fromdate=datetime(2010, 1, 1, 0, 0) #only get the stock IPO after 2010

#get all A-shares on the market
allstock=w.wset("sectorconstituent","date="+setdate+";sectorid=a001010100000000;field=wind_code")
allstock=allstockcode.Data[0]
ipodate=w.wss(allstockcode, "ipo_date")
ipodate=ipodate.Data[0]
finddate=np.nonzero([x>a for x in ipodate])[0]
allstock=np.array(allstock)[finddate]
 
#get the features we need 
IPOdata=w.wss(list(allstock), "industry_gics,mkt,backdoor,ipo_date,ipo_price,ipo_amount,ipo_collection,ipo_netcollection,ipo_puboffrdate,ipo_leadundr,ipo_type,ipo_expense,ipo_pctchange,ipo_listdayvolume","unit=1;industryType=1")
alldata=pd.DataFrame(IPOdata.Data).T
alldata.columns=IPOdata.Fields
alldata.index=allstock

#save the data as csv
alldata.to_csv('C:\\Users\\admin\\Documents\\PHBS\\Topic in quantitative finance\\project\\alldata.csv',header=True,index=True)
