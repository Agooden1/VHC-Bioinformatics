import datetime
import pandas as pd
import sys
import numpy as np


#load lab orders excel file
#Each of these variables should represent a column in lab orders

lab_orders = pd.read_excel('X:\Lab\Lab_Inventory\Supplies\Lab_Orders.xlsm', 'Ordered 2018')

date_req = lab_orders.iloc[:, 0]
vendor = lab_orders.iloc[:, 1]
qty = lab_orders.iloc[:, 2]
unit = lab_orders.iloc[:, 3]
cat_num = lab_orders.iloc[:, 4]
item = lab_orders.iloc[:, 5]
cost = lab_orders.iloc[:, 6]
order_date = lab_orders.iloc[:, 7]
SAP = lab_orders.iloc[:, 8]
per_req = lab_orders.iloc[:, 9]
per_rec = lab_orders.iloc[:, 10]
date_rec = lab_orders.iloc[:, 11]
comments = lab_orders.iloc[:, 12]
now = datetime.datetime.now()


''' Excel converts the date to the amount of days from 1/1/1900.
This converts today's date into the amount of days from 1/1/1900. 
From here on we can use the dates in excel with today's date.'''

from datetime import date
d0 = date(1900, 1, 1)
d1 = date(now.year, now.month, now.day)
delta = d1 - d0

#This is to try and find all items that were requested 14+ days ago and have yet to come in

rec = []
not_rec = []
i = 0
for i in range(len(date_rec)):
    if pd.isna(date_rec.iloc[i]) == True:
        not_rec.append((lab_orders.iloc[i]))
        i += 1
    elif pd.isna(date_rec.iloc[i]) == False:
        rec.append((lab_orders.iloc[i]))
        i += 1


rec_df = pd.DataFrame(rec)
not_rec_df = pd.DataFrame(not_rec)

writer = pd.ExcelWriter(r'C:\Users\Mike Murphy\Desktop\Not_Received_2018.xlsx')
not_rec_df.to_excel(writer, 'Sheet 1')
writer.save()
print(lab_orders)