import mysql.connector
import random
from datetime import datetime, timedelta
isimler = ["Ahmet", "Mehmet", "Ayşe", "Fatma", "Ali", "Veli", "Zeynep", "Emine", "Mustafa", "Hasan",
           "Hüseyin", "Ömer", "Hatice", "Gül", "Yusuf", "Serkan", "Ece", "Nur", "Ebru", "Selim",
           "Murat", "Yılmaz", "Sevgi", "İbrahim", "Deniz", "Selin", "Erdem", "Can", "Arzu", "Cem",
           "Beril", "Zeki", "Seda", "Aslı", "Hakan", "Büşra", "İsmail", "Rüya", "Kadir", "Çiğdem",
           "Cansu", "Melike", "Özgür", "Nalan", "Gizem", "Tolga", "Aysun", "Türker", "Yeliz", "Uğur",
           "Kemal", "Gökçe", "Emre", "Yasemin", "Ela", "Umut", "Nihan", "Oğuz", "Şebnem"]
soyisimler = ["Yılmaz", "Kaya", "Demir", "Çelik", "Öztürk", "Arslan", "Aksoy", "Aydın", "Güler", "Şahin",
              "Koç", "Doğan", "Kurt", "Çakır", "Erdoğan", "Taş", "Kara", "Özdemir", "Turan", "Kaplan",
              "Keskin", "Şen", "Güneş", "Bulut", "Acar", "Kılıç", "Yaman", "Çetin", "Karadağ", "Gök",
              "Aslan", "Özen", "Uysal", "Aydoğan", "Şimşek", "Bozkurt", "Ceylan", "Işık", "Kurtuluş",
              "Gündüz", "Ateş", "Şanlı", "Ergün", "Erdem", "Aydos", "Büyük", "Çalışkan", "Gültekin",
              "Karahan", "Mert", "Tunç", "Güçlü", "Kayaalp", "Çeliktaş", "Yavuz", "Koşar", "Sert",
              "Yıldız", "Güler", "Gözen", "Başar", "Kuşçu", "Genç"]
baslangic_tarihi = datetime(2002, 1, 1)
bitis_tarihi = datetime(2005, 12, 31)
baslangic_tarihiTC = datetime(1990, 1, 1)
bitis_tarihiTC = datetime(1995, 12, 31)
cinsiyet = ["E", "K"]
list = []
listc = []
def RandomName():
    return random.choice(isimler)

def RandomSurName():
    return random.choice(soyisimler)

def RandomBirthday():
    tarih_araligi = bitis_tarihi - baslangic_tarihi
    rastgele_gun = random.randint(0, tarih_araligi.days)
    rastgele_tarih = baslangic_tarihi + timedelta(days=rastgele_gun)
    return rastgele_tarih
def RandomBirthdayTeacher():
    tarih_araligi = bitis_tarihiTC - baslangic_tarihiTC
    rastgele_gun = random.randint(0, tarih_araligi.days)
    rastgele_tarih = baslangic_tarihiTC + timedelta(days=rastgele_gun)
    return rastgele_tarih
def RandomGender():
    return random.choice(cinsiyet)
def RandomClassID():
    def RandomChoise():
        return random.randint(0, lng)
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="school")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(id) FROM class")
    try:
        result = cursor.fetchone()
        connection.commit()
        lng = result[0]
    except mysql.connector.Error as EX:
        print(EX)
    finally:
        connection.close()
        return RandomChoise()

def RandomStudentAdd():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="school")

    cursor = connection.cursor()

    sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender,ClassID) VALUES (%s,%s,%s,%s,%s,%s)"
    say = 0
    while say < 40:
        studentnumber = random.randint(0, 3000)
        name = RandomName()
        surname = RandomSurName()
        birthday = RandomBirthday()
        gender = RandomGender()
        classid = RandomClassID()

        list.append((studentnumber, name, surname, birthday, gender, classid))
        say += 1
    try:
        Values = list
        cursor.executemany(sql, Values)
        connection.commit()
        print(f"{len(list)} Tane Veri Eklendi")
    except mysql.connector.Error as EX:
        print(EX)
    finally:
        connection.close()
def AddRandomTeacher():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="school")

    cursor = connection.cursor()

    sql = "INSERT INTO teacher(Branch,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
    say = 0
    while say < 14:
        branch = random.randint(1, 5)
        name = RandomName()
        surname = RandomSurName()
        birthday = RandomBirthdayTeacher()
        gender = RandomGender()

        listc.append((branch, name, surname, birthday, gender))
        say += 1
    try:
        Values = listc
        cursor.executemany(sql, Values)
        connection.commit()
        print(f"{len(list)} Tane Veri Eklendi")
    except mysql.connector.Error as EX:
        print(EX)
    finally:
        connection.close()
def FoundClass():
    connection = mysql.connector.connect(host="localhost", user="root", password="berk1907", database="school")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM classlesson ")

    try:
        result = cursor.fetchall()
        connection.commit()
        for x in result:
            print(x)
    except mysql.connector.Error as ERR:
        print(ERR)
    finally:
        connection.close()
        print("Bağlantı Kapandı")