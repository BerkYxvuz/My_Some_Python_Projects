import pandas as pd

df = pd.read_csv("USvideos.csv")

# İlk 10 kayıt.

# print(df["title"].head(10))

# İkinci 5 kayıt.

# print(df[5: 15]["title"].head(5))

# Dataset de kolon isimleri ve sayısı

# print(len(df.columns), df.columns)

# Bazı kolonları silme

df = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"], axis=1) # axis ile sütunu seçtik ve sildik
# print(df.columns)

# Like ve Dislike ortalaması

# print(df[["likes", "dislikes"]].mean())

# ilk 50 video,like ve dislike sayılarıyla

# print(df[["title", "likes", "dislikes"]].head(50))

# En fazla görüntülenen video

# print(df[["title", "views"]].max())

# En az görüntülenen videolar.

# print(df.sort_values('views', ascending=False)[["title", "views"]].tail(10))

# En fazla görüntelenen 10 video

# print(df.sort_values('views', ascending=True)[["title", "views"]].tail(10))

# Kategoriye göre beğeni ortalaması

# print(df.groupby('category_id')['likes'].mean())

# Kategoriye göre yorum ortalaması
# result = df.groupby('category_id')['comment_count'].mean()
# print(result.sort_values(ascending=False))

# kategorideki video sayısı

# print(df.groupby('category_id')['title'].count())

# başlık uzunluğu yeni kolona

# df["title_len"] = df["title"].str.len()
# print(df["title_len"])

# videonun tag sayısı
# result = df["tags"].str.split(' ').str.len()
# print(result)

# like disslike oranına göre en popüler videolar

def oranhesapla(dataset):
    likeslist = list(dataset["likes"])
    dislikeslist = list(dataset["dislikes"])

    liste = list(zip(likeslist, dislikeslist)) # tuple'a çeviriyor

    oranlistesi = []

    for like,dislike in liste:
        if like + dislike == 0:
            oranlistesi.append(0)
        else:
            oranlistesi.append(like/(like+dislike))
    return oranlistesi
df["begeni_orani"] = oranhesapla(df)

print(df.sort_values("begeni_orani", ascending=False)[["title","likes","dislikes","begeni_orani"]])