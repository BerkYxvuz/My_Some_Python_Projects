import mysql.connector

def insertProducts(list):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="berk1907",
        database="not-app"
    )
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"

    values = list

    cursor.executemany(sql, values)
    try:
        connection.commit() # bunu yazmazsak sunucuya veri gönderme işlemi olmaz
        print(f'{cursor.rowcount} Tane kayıt eklendi.')
        print(f"Son Eklenen Kayıt ID'si {cursor.lastrowid}")
    except mysql.connector.Error as Ex:
        print(Ex)
    finally:
        connection.close()
        print("DataBase Kapandı.")

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="berk1907",
        database="not-app"
    )
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"

    values = (name, price, imageUrl, description)

    cursor.execute(sql, values)
    try:
        connection.commit() # bunu yazmazsak sunucuya veri gönderme işlemi olmaz
        print(f'{cursor.rowcount} Tane kayıt eklendi.')
        print(f"Son Eklenen Kayıt ID'si {cursor.lastrowid}")
    except mysql.connector.Error as Ex:
        print(Ex)
    finally:
        connection.close()
        print("DataBase Kapandı.")

list = []

while True:
    name = input("Ürün Adı: ")
    price = float(input("Ürün Fiyatı: "))
    imageUrl = input("Ürün Resiminin Url'si: ")
    description = input("Ürün İncelemesi: ")

    list.append((name, price, imageUrl, description))

    result = input("Devam Etmek İstiyor Musunuz? (e/h)")
    if result == 'h':
        print("Kayıtlarınız Veri Tabanına Aktarılıyor")
        insertProducts(list)
        break
    else:
        pass


