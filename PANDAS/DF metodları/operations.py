import pandas as pd
import numpy as np

data = {
     "Column1": [1,2,3,4,5],
     "Column2": [10,20,13,45, 25],
     "Column3": ["abc", "bcaa", "ade", "cba", "de"]
}

df = pd.DataFrame(data)

result = df

'''
result = df["Column2"].unique() # tekrar etmeyen bilgileri yazdırır bilgi tekrar ediyorsa yazdırmaz.
result = df["Column2"].nunique() # kaç tane tekrar etmeyen veri olduğunun sayısını yazdırır.
result = df["Column2"].value_counts() # Tekrar eden veriyi ve sayısını yazdırır
'''

def kareal(x):
    return x * x

kareal2 = lambda x: x*x

# result = df["Column1"] * 2
# result = df["Column1"].apply(kareal) # Column1 için fonksiyon görevlendiririz ve fonksiyon o sütündaki tüm veriler için çalışır
# result = df["Column1"].apply(kareal2) # lambda metodu da verebiliriz
# result = df["Column3"].apply(len) # değerin kaç karakter olduğunu yazdırır.

df["Column4"] = df["Column3"].apply(len) # değerin kaç karakter olduğunu yeni kolona yazdırır.

# result = df.columns
# result = len(df.columns)

# result = df.index
# result = len(df.index)

# result = df.info

# result = df.sort_values("Column2") # int veriler büyüklüğe göre sıralanır
# result = df.sort_values("Column3") # str veriler alfabeye göre sıralanır
# result = df.sort_values("Column3", ascending = False) # ascending str için True ise alfabeye göre False ise tersine
#                                                     # int için tersine düzüne göre yine ayarlanıyor



print(result)