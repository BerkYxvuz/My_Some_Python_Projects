import mysql.connector
'''
# database oluşturma

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

# data base leri yazdırma.

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
'''

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="berk1907",
    database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")