import pandas as pd
li=[]
df1 = pd.read_csv('/home/uvionics/data/Latest_mar6/shoppe_result/shopee_milkformula_SG_2019-01-31_sku.csv', delimiter=',', quotechar='"')
df1['sales']=df1[' Stock']
df1['sales']=df1['sales'].diff(1)
df1['sales'].iloc[0]=0
df1.sales[df1.sales>0] = 0
df1['sales']=df1['sales'].abs() 
df1.to_csv('/home/uvionics/data/Latest_mar6/shoppe_result/sales/shopee_milkformula_SG_2019-01-31_sku_sales.csv', sep='\t', encoding='utf-8',index=False)
