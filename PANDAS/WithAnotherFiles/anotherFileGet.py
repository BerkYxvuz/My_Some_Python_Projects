import pandas as pd
'''
# df = pd.read_json("dosya.json") # json dan bilgi alır.
# df = pd.read_excel("dosya.xlsx") # excel den bilgi alır.

# connection = sqlite3.connect("database.db") # önce bağlandık.
# df = pd.read_sql_query("") # sql query den bilgi alır.
'''
df = pd.read_csv('files/Football teams.csv')# csv den bilgi alma

print(df)