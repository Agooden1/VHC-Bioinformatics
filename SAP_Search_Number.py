import pandas as pd


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


SAP_Input = input('Please enter the SAP number: ')

SAP_Number = []

i = 0

for i in range(len(SAP)):
    if SAP.iloc[i] == int(SAP_Input):
        SAP_Number.append(lab_orders.iloc[i])
        i += 1
    elif SAP.iloc[i] == int(SAP_Input):
        SAP_Number.append(lab_orders.iloc[i])
        i += 1
    elif SAP.iloc[i] == str(SAP_Input):
        SAP_Number.append(lab_orders.iloc[i])
        i += 1

writer = pd.ExcelWriter(r'C:\Users\Mike Murphy\Desktop\SAP_' + str(SAP_Input) + '_2018.xlsx')
SAP_Number_df = pd.DataFrame(SAP_Number)
SAP_Number_df.to_excel(writer, str(SAP_Input))
writer.save()
