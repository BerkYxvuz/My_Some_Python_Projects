import pandas as pd

customers = {
    "CustomerId": [1,2,3,4],
    "FirstName": ["Ahmet","Ali","Hasan","Canan"],
    "LastName": ["Yılmaz","Korkmaz","Çelik","Toprak"]
}
orders = {
    'OrderId': [10,11,12,13],
    'CustomerId': [1,2,5,7],
    'OrderDate': ['2010-07-04','2010-07-08','2010-07-09','2010-07-10']
}

df_customers = pd.DataFrame(customers, columns=["CustomerId","FirstName","LastName"])
df_orders = pd.DataFrame(orders, columns=["OrderId","CustomerId","OrderDate"])

# result = pd.merge(df_customers, df_orders, how="inner") # inner tamamen ortak olanları yazdırır
# result = pd.merge(df_customers, df_orders, how="outer") # BÜTÜN KAYITLAR YAZILIR
# result = pd.merge(df_customers, df_orders, how="left") # soldakileri getir yani müşterileri siparişi yoksa bile getirir
# result = pd.merge(df_customers, df_orders, how="right") # siparişleri getirir sahipsiz olsa bile

customersA = {
    "CustomerId": [1,2,3,4],
    "FirstName": ["Ahmet","Ali","Hasan","Canan"],
    "LastName": ["Yılmaz","Korkmaz","Çelik","Toprak"]
}
customersB = {
    "CustomerId": [4,5,6,7],
    "FirstName": ["Yağmur","Çınar","Cengiz","Can"],
    "LastName": ["Bilge","Turan","Yılmaz","Turan"]
}

df_customersA = pd.DataFrame(customersA, columns=["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB, columns=["CustomerId","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB]) # 2 data frame birleştirme

print(result)