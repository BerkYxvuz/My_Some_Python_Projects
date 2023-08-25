import mysql.connector
from datetime import date

def UpdateFromID(SN,N,SNAME,BD,G,ID):
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="schooldb")

    cursor = connection.cursor()

    sql = "UPDATE student SET studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"

    values = (SN, N, SNAME, BD, G, ID)

    cursor.execute(sql, values)

    try:
        connection.commit()
        print(f"{ID} ID'sin de Veri Güncellendi")
    except mysql.connector.Error as EX:
        print(f'Hata: {EX}')
    finally:
        connection.close()