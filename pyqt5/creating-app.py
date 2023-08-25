import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon



def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('First App')
    win.setGeometry(200, 200, 500, 500)
    # win.setWindowIcon('')

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText('Adınız: ')
    lbl_name.move(50, 30)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText('Soy Adınız: ')
    lbl_surname.move(50, 80)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(120, 30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(120, 80)

    def clicked(self):
        print('Butona Tıklandı Name: ' + txt_name.text() + ' Surname: ' + txt_surname.text())

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText('Kaydet')
    btn_save.move(120, 120)
    btn_save.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())

window()