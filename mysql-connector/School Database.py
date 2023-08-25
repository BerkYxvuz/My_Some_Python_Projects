import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="berk1907",
    database="schooldb"
)

mycursor = connection.cursor()