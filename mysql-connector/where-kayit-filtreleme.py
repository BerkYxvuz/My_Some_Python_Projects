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

def getProducts():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="not-app")

    cursor = connection.cursor()

    # cursor.execute("SELECT * From products Where id=1") # id'si 1 olan kayıt gelir
    # cursor.execute("SELECT * From products Where name='Samsung S6'") # İsmi Samsung S6 olanlar gelir
    # cursor.execute("SELECT * From products Where name='Samsung S6' or fiyat>2000") # İki tane filtre or ile
    # cursor.execute("SELECT * From products Where name='Samsung S6' and fiyat>2000") # İki tane filtre and ile
    # cursor.execute("SELECT name,price From products Where name LIKE '%Samsung%'") # name içerisinde Samsung yazıyosa getirir
    # cursor.execute("SELECT name,price From products Where name LIKE 'Samsung%'") # Başında % yoksa başı Samsung olacak filtresi
    cursor.execute("SELECT name,price From products Where name LIKE '%Samsung%'") # Sonunda % yoksa sonu Samsung olacak filtresi

    result = cursor.fetchall()

    print(result)

    # for product in result:
    #     print(f'İsim: {product[0]}' + " | " + f'Fiyat: {product[1]}')

def getProductsID(id):
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="not-app")

    cursor = connection.cursor()

    sql = "SELECT * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql, params)

    result = cursor.fetchone()

    print(result)

getProductsID(1)