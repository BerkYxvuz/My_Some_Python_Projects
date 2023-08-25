import mysql.connector

def UpdateProduct():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="not-app")

    cursor = connection.cursor()

    sql = "UPDATE Products Set name='Samsung S10' where id=1"

    cursor.execute(sql)

    try:
        connection.commit()
        print("1 Kayıt Güncellendi")
    except mysql.connector.Error as EX:
        print(EX)
    finally:
        print("Database bağlantısı kapandı")
        connection.close()
UpdateProduct()