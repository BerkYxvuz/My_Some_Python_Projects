import pandas as pd

df = pd.read_csv("all_seasons.csv")
df = pd.DataFrame(df)
# İlk 10 kayıt.

# print(df.head(10))

# Toplam Kayıt.

# print(len(df["player_name"]))

# Tüm oyuncuların ortalama yaşı.

# print(df["age"].mean())

# En Yüksek Yaş

# print(df["age"].max())

# En Yüksek Yaş'taki oyuncu.

# print(df[["player_name", "age"]].max())

# 20-25 yaş arası oyuncuların adı ve takımları

# print(df.query("age >= 20 & age <= 25")[["player_name", "team_abbreviation"]])

# John Holland'ın oynadığı takım.

# print(df.query("player_name == 'John Holland'")[["player_name", "team_abbreviation"]])

# takımlara göre ortalama yaş

# print(df.groupby("team_abbreviation")["age"].mean())

# kaç farklı takım var?

# print(len(df.groupby("team_abbreviation").count()))

# takımda toplam oynayan oyuncu sayısı

# print(df.groupby("team_abbreviation")["player_name"].count())

# isminde and olanlar

isimler = df["player_name"].str.contains('and')

print(df.loc[isimler, :])