import json, re, os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        self.loadUsers()
    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r', encoding='utf-8') as f:
                users = json.load(f)
                for user in users:
                    user = json.loads(user) #Burada user'ı json stringine dönüştürdük hala sözlük ama json'da uyumlu.
                    newUser = User(username=user['username'],
                                   password=user['password'],# Burada ise verileri derleyip toparladık
                                   email=user['email']) #      ve tekrar append ettik.
                    self.users.append(newUser)

    def register(self, user: User):
        if self.isLoggedIn:
            print('Zaten Bir Hesabınız Var.')
        else:
            self.users.append(user)
            self.savetoFile()
        print('Kullanıcı Oluşturuldu')
    def logout(self):
        if self.isLoggedIn:
            self.isLoggedIn = False
            self.currentUser = {}
        else:
            print('Zaten Giriş Yapılmamış.')
        print('Çıkış Yapıldı.')
    def identity(self):
        if self.isLoggedIn:
            print(f'Kullanıcı: {self.currentUser.username}')
        else:
            print('Giriş Yapılmadı.')
    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Giriş Başarılı.')
            else:
                print('Giriş Başarısız.')
    def savetoFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))  #.__dict__ user'ı sözlüğe çeviriyor.

        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(list, f)

repositor = UserRepository()

while True:
    print('Menü'.center(50, '-'))
    if repositor.isLoggedIn:
        print(f'Sayın: {repositor.currentUser.username}'.center(10, '*'))
    secim = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz: ')
    if secim == '5':
        break
    else:
        if secim == '1':
            username = input('Username: ')
            password = input('Password: ')
            againpassword = input('Again password: ')
            email = input('Email: ')
            emailcont = re.findall("@gmail.com$", email) # E posta adresi gerçek mi kontrol ettik.
            with open('users.json', 'r', encoding='utf-8') as f: #json dosyamızı username kontrolü için açtık
                usernameler = []# liste oluşturduk ki kullanıcı adlarını içine atalım
                for i in f:
                    usernameler.append(i)# okunanları ekledik
                    if username in i or email in i: #listemizde var mı diye kontrol ettik
                        if username in i:
                            usernamekontrol = False
                            print('Bu Kullancı Adı Zaten Var!')
                        elif email in i:
                            emailkontrol = False
                            print('Bu E-Posta Zaten Var!')
                    else:
                        emailkontrol = True
                        usernamekontrol = True

            if password == againpassword and emailcont == ['@gmail.com'] and usernamekontrol is True and emailkontrol is True:
                user = User(username=username, password=password, email=email)
                print(usernameler)
                repositor.register(user)
            else:
                if emailcont == []:
                    print('E-Posta geçersiz.')
                elif password != againpassword:
                    print('Şifreler Uyumsuz.')

        if secim == '2':
            if repositor.isLoggedIn:
                print('Zaten Giriş Yapılmış.')
            else:
                username = input('Username: ')
                password = input('Password: ')
                repositor.login(username=username, password=password)
        if secim == '3':
            repositor.logout()
        if secim == '4':
            repositor.identity()
        if secim == '5':
            break
        elif secim != '1' and secim != '2' and secim != '3' and secim != '4' and secim != '5':
            print('Yanlış Seçim.')