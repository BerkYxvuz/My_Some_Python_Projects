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

    # cursor.execute("SELECT * From products")

    cursor.execute("SELECT name,price From products")

    # result = cursor.fetchall() bütün kayıtları alıyor

    result = cursor.fetchone() # bulduğu ilk kaydı alıyor

    print(f'İsim: {result[0]}' + " | " + f'Fiyat: {result[1]}')

    # print(result) hepsini liste halinde yazdırıyor

    '''
    for product in result: # satır satır yazdırır
        print(product)
    '''

    # for product in result:
    #     print(f'İsim: {product[0]}' + " | " + f'Fiyat: {product[1]}')

getProducts()