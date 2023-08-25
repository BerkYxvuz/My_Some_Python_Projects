import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="not-app")

    cursor = connection.cursor()

    # sql = "SELECT * FROM products"
    # sql = "SELECT * FROM categories"
    # sql = "SELECT * FROM products inner join categories on Categories.id=Products.Categoryid" # iki tabloyu inner join ile birleştirdik on diyerek hangi sütun için ortak id olduğunu belirttik.
    # sql = "SELECT Products.name,Products.price,Categories.name FROM products inner join categories on Categories.id=Products.Categoryid"
    # sql = "SELECT Products.name,Products.price,Categories.name FROM products inner join categories on Categories.id=Products.Categoryid where Categories.name='telefon'"
    sql = "SELECT p.name,p.price,c.name FROM products as p inner join categories as c on c.id=p.Categoryid where p.name='Samsung S5'"

    cursor.execute(sql)

    try:
        result = cursor.fetchall()
        for product in result:
            print(product)
    except mysql.connector.Error as EX:
        print(EX)
    finally:
        print("Database kapandı.")
        connection.close()
getProducts()