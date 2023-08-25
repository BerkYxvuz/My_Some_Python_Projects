import pandas as pd

data = pd.read_csv("all_seasons.csv")

# data["Name"] = data["Name"].str.upper() # Kolondaki bütün kayıtları BÜYÜK harfle yazar
# data["Name"] = data["Name"].str.lower() # Kolondaki bütün kayıtları küçük harfle yazar
# data["index"] = data["Name"].str.find('a') # a harfinin olduğu indexi index kolonuna yazar

# res = data["player_name"].str.contains('Jordan') # contains jordan yazan değerleri bulur
# res = data.player_name.str.replace(' ', '-')
data[["FName", "LName"]] = data["player_name"].loc[data["player_name"].str.split(' ').str.len()==2].str.split(expand=True)
print(data[["FName", "LName"]].head(10))