import mysql.connector
from datetime import datetime

def AllStudent():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="schooldb")

    cursor = mydb.cursor()

    cursor.execute("SELECT * From Student")

    result = cursor.fetchall()

    connection.commit()

    for x in result:
        print(x)

def Filters():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="schooldb")

    cursor = connection.cursor()

    cursor.execute("Select StudentNumber,Name,Surname FROM student")

    result = cursor.fetchall()

    connection.commit()

    for x in result:
        print(x)

def JustGirlsNameSN():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="schooldb")

    cursor = connection.cursor()

    cursor.execute("SELECT name,surname FROM student WHERE Gender = 'K'")

    result = cursor.fetchall()

    connection.commit()

    for x in result:
        print(x)
def Just2003s():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="schooldb")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM student WHERE YEAR(Birthdate) = 2003")

    result = cursor.fetchall()

    connection.commit()

    for x in result:
        print(x)
def IFnali():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="schooldb")

    cursor = connection.cursor()

    # cursor.execute("SELECT * From Student WHERE name = 'Ali' and Birthdate LIKE '2005%'")

    cursor.execute("SELECT * From Student WHERE name = 'Ali' and YEAR(Birthdate) = 2005")

    result = cursor.fetchall()

    connection.commit()

    for x in result:
        print(x)
def LikeAn():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="schooldb")

    cursor = connection.cursor()

    cursor.execute("SELECT * From Student WHERE name LIKE '%an%'")

    result = cursor.fetchall()

    connection.commit()

    for x in result:
        print(x)
def GendreCount():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="schooldb")

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(id) From Student where Gender='E'")

    result = cursor.fetchall()

    connection.commit()

    print(result)