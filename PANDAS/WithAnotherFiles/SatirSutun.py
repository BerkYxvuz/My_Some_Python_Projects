import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3),index=["A", "B", "C"],columns=["Kolon-1", "Kolon-2", "Kolon-3"])
result = df
result = df["Kolon-1"]
result = type(df["Kolon-1"])
result = df[["Kolon-1", "Kolon-2"]]
# result = df.iloc[2] # iloc index'i ne belirlersek belirleyelim sayılarla seçmemizi sağlar.

# result = df.loc["A"] # Satır seçme.
# result = df.loc[:, "Kolon-1","Kolon-2"] # Kolon seçme
# result = df.loc[:, "Kolon-1":"Kolon-3"] # Kolon 1'den Kolon'3 e kadar seçer
# result = df.loc["A":"B", "Kolon-1":"Kolon-3"] # Hem Satır Hemen Kolon seçer
# result = df.loc[:"B", "Kolon-1":"Kolon-3"] # B'ye Satır Seçer Hemen Kolon seçer
# result = df.loc["A", "Kolon-2"] # A satırında'ki kolon-2 değerini alır.
# result = df.loc[["A","B"], ["Kolon-2","Kolon-3"]] # A satırında'ki kolon-2 değerini alır.

# Yeni KOLON ekleme.
df["Kolon-4"] = pd.Series(randn(3), ["A", "B", "C"])
df["Kolon-5"] = df["Kolon-1"] + df["Kolon-2"]

# Kolon silme.

df.drop("Kolon-5", axis=1) # böyle kalıcı olarak silmez asıl değer aynı kalır
result = df.drop("Kolon-5", axis=1) # böyle kalıcı olur. VEYA
df.drop("Kolon-5", axis=1, inplace=True) # İNPLACE KULLANARAKTA KALICI YAPABİLİRİZ

print(df)