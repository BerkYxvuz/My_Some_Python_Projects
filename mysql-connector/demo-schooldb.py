import datetime
import mysql.connector

list = [("101","Ahmet", "Yılmaz", datetime.datetime(2005, 5, 17), "E"),
        ("102", "Ali", "Can", datetime.datetime(2005, 7, 17), "E"),
        ("103", "Canan", "Tan", datetime.datetime(2005, 7, 7), "K"),
        ("104", "Ayşe", "Taner", datetime.datetime(2005, 9, 23), "K"),
        ("105", "Bahadır", "Toksöz", datetime.datetime(2004, 7, 27), "E"),
        ("106", "Ali", "Cenk", datetime.datetime(2005, 8, 25), "E")]

def insertValues(list):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="berk1907",
        database="schooldb"
    )

    cursor = connection.cursor()

    sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
    
    values = list
    cursor.executemany(sql, values)
    try:
        print("Değerler Gönderildi")
        connection.commit()
    except mysql.connector.Error as ex:
        print(ex)
    finally:
        connection.close()

insertValues(list)