import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(200, 200, 500, 500)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('Sayı 1: ')
        self.lbl_sayi1.move(50, 30)

        self.sayi1_txtbox = QtWidgets.QLineEdit(self)
        self.sayi1_txtbox.move(150, 30)
        self.sayi1_txtbox.resize(200, 32)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText('Sayı 1: ')
        self.lbl_sayi2.move(50, 80)

        self.sayi2_txtbox = QtWidgets.QLineEdit(self)
        self.sayi2_txtbox.move(150, 80)
        self.sayi2_txtbox.resize(200, 32)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText('Topla')
        self.btn_topla.move(150, 130)
        self.btn_topla.clicked.connect(self.toplama)

        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText('Çıkar')
        self.btn_cikar.move(150, 170)
        self.btn_cikar.clicked.connect(self.cikarma)

        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText('Çarp')
        self.btn_carp.move(150, 210)
        self.btn_carp.clicked.connect(self.carpma)

        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText('Böl')
        self.btn_bol.move(150, 250)
        self.btn_bol.clicked.connect(self.bolme)

        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText(f'Sonuç: ')
        self.lbl_sonuc.move(150, 290)
    def toplama(self):
        if self.sayi1_txtbox.text() != '' and self.sayi2_txtbox.text() != '':
            sonuc = int(self.sayi1_txtbox.text()) + int(self.sayi2_txtbox.text())
            self.lbl_sonuc.setText('Sonuç: ' + str(sonuc))
        else:
            pass
    def cikarma(self):
        if self.sayi1_txtbox.text() != '' and self.sayi2_txtbox.text() != '':
            sonuc = int(self.sayi1_txtbox.text()) - int(self.sayi2_txtbox.text())
            self.lbl_sonuc.setText('Sonuç: ' + str(sonuc))
        else:
            pass
    def bolme(self):
        if self.sayi1_txtbox.text() != '' and self.sayi2_txtbox.text() != '':
            sonuc = int(self.sayi1_txtbox.text()) / int(self.sayi2_txtbox.text())
            self.lbl_sonuc.setText('Sonuç: ' + str(sonuc))
        else:
            pass
    def carpma(self):
        if self.sayi1_txtbox.text() != '' and self.sayi2_txtbox.text() != '':
            sonuc = int(self.sayi1_txtbox.text()) * int(self.sayi2_txtbox.text())
            self.lbl_sonuc.setText('Sonuç: ' + str(sonuc))
        else:
            pass

def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()