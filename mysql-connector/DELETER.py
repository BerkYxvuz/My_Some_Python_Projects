import mysql.connector

def DeleteProduct():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="not-app")

    cursor = connection.cursor()

    # sql = "DELETE FROM products" # bütün kayıtları siler

    sql = "DELETE FROM products WHERE id=6"

    cursor.execute(sql)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt silindi.")
    except mysql.connector.Error as EX:
        print(EX)
    finally:
        print("Database bağlantısı kapandı")
        connection.close()
DeleteProduct()