import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 75).reshape(15, 5)

df = pd.DataFrame(data, columns=["Column1", "Column2", "Column3", "Column4", "Column5"])

result = df
result = df.columns # Kolonların adını yazdırır.
result = df.head() # ilk 5 kaydı çağırır içine değer girmezsen.
result = df.tail() # son 5 kaydı çağırır içine değer girmezsen
result = df["Column1"].head() # kolon seçerek ilk satırları
result = df["Column1"].tail() # kolon seçerek ilk satırları
result = df[5:15][["Column1","Column2"]].head()
result = df[5:15][["Column1","Column2"]].tail()

result = df > 50
result = df[df > 50] # sayıları gösterir
result = df[df % 2 == 0] # çift sayıları gösterir
result = df[["Column1"]] > 50
result = df[df[["Column1"]] > 50]
result = df[df[["Column1"]] > 50][["Column1","Column2"]]
result = df[(df["Column1"] > 50) & (df["Column1"] <= 70)]
result = df[(df["Column1"] > 50) | (df["Column1"] <= 70)]
result = df.query("Column1 >= 50 & Column1 % 2 == 0")[["Column1"]]

print(result)