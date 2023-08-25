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

def getProductsWithAggregate():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="not-app")

    cursor = connection.cursor()

    # sql = "SELECT COUNT(name) from Products"# count() ile verinin kayıt sayısını yazdırırız

    # sql = "SELECT AVG(price) from Products"# AVG() Ortalama alır.

    # sql = "SELECT SUM(price) from Products"# SUM() Toplamını alır.

    # sql = "SELECT MIN(price) from Products"# MIN() Minumum fiyatı alır.

    # sql = "SELECT MAX(price) from Products"# MAX() Max fiyatı alır.

    sql = "SELECT name,price from Products where price = (Select MAX(price) from products)"# MAX() Max fiyatı alır.

    cursor.execute(sql)

    result = cursor.fetchone()

    print(f'{result[0]} | {result[1]}')

getProductsWithAggregate()