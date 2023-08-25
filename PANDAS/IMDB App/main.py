import pandas as pd

df = pd.read_csv("imdb_top_1000.csv")
'''
# ilk 5 kayıt

print(df["Series_Title"].head())

# ilk 10 kayıt

print(df.Series_Title.head(10))

# Son 5 kayıt

print(df.Series_Title.tail())

# Son 10 kayıt

print(df.Series_Title.tail(10)) '''

# Sadece Title'lar

# print(df["Series_Title"])

# sadece rating ve isim(ilk 5)

# print(df[["Series_Title", "IMDB_Rating"]].head())

# sadece rating ve isim(son 7)

# print(df[["Series_Title", "IMDB_Rating"]].tail(7))

# Sadece isim ve raytin 2. ilk 5 kolon

# print(df[5:][["Series_Title", "IMDB_Rating"]].head())

# İsim ve Rating 8.0 üstü olan ve ilk 50 tane
# result = df.query("IMDB_Rating >= 8.0")
# print(result[["Series_Title", "IMDB_Rating"]].head(50))

# 2014-2015 arası filmler

# result = df.query("Released_Year >= '2014' & Released_Year  <= '2015'")
#
# print(result["Series_Title"])

# Değerlendirme Sayısı 100.000 den büyük ya da imdb puanı 8 ile 9 arasında

result = df.query("No_of_Votes >= 100.000 | IMDB_Rating >= 8 & IMDB_Rating <= 9")

print(result[["Series_Title", "No_of_Votes", "IMDB_Rating"]])