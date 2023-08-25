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

def getProductsID(id):
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="not-app")

    cursor = connection.cursor()

    sql = "SELECT * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql, params)

    result = cursor.fetchone()

    print(result)

def getProducts():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="not-app")

    cursor = connection.cursor()

    # cursor.execute("Select * From Products Order By name") # bu haliyle alfabeye göre sıralar
    # cursor.execute("Select * From Products Order By price") # bu haliyle fiyatları küçükten büyüğe sıralar
    # cursor.execute("Select * From Products Order By id")  # bu haliyle id'leri küçükten büyüğe sıralar
    # cursor.execute("Select * From Products Order By id DESC")  # bu haliyle büyükten küçüğe sıralar
    # cursor.execute("Select * From Products Order By price DESC")  # bu haliyle büyükten küçüğe sıralar
    cursor.execute("Select * From Products Order By name, price")  # name için sıralama yapıyor fakat name aynıysa ona göre fıyatı baz alarak sıralıyor.

    result = cursor.fetchall()

    for x in result:
        print(x)

getProducts()