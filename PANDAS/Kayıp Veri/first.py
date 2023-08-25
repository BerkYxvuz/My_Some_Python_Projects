import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index=['a','c','e','f','h'], columns=['column1','column2','column3'])

df = df.reindex(['a','b','c','d','e','f','g','h'])

result = df

# result = df.isnull() #null olan değerleri True yapar
# result = df.notnull() #null olan değerleri False yapar

# result = df[df["column1"].notnull()] # sadece değerleri yazdırır
# result = df[df["column1"].isnull()] # sadece null olanları yazdırır

# result = df.dropna() # axis = 0 satıra göre çalışır içinde değer olan satırları getirir
# result = df.dropna(how="any") #null varsa satırı getirmez
# result = df.dropna(how="all") # eğer tüm satır null sa getirmez

result = df.dropna(subset=["column1"], how="all") # subset kolon seçmek için.
result = df.dropna(thresh=3) # thresh komutu en az 4 tane normal veri olursa yazdırmak için.
result = df.fillna(value='no input') # Null değerin yerine verdiğimiz değeri yazdırma.

print(result)