import typing
from hesap_machine import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.setWindowTitle("Hesap Makinesi")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.add_number)
        self.ui.pushButton_2.clicked.connect(self.add_number)
        self.ui.pushButton_3.clicked.connect(self.add_number)
        self.ui.pushButton_4.clicked.connect(self.add_number)
        self.ui.pushButton_5.clicked.connect(self.add_number)
        self.ui.pushButton_6.clicked.connect(self.add_number)
        self.ui.pushButton_7.clicked.connect(self.add_number)
        self.ui.pushButton_8.clicked.connect(self.add_number)
        self.ui.pushButton_9.clicked.connect(self.add_number)
        self.ui.pushButton_10.clicked.connect(self.add_number)
        self.ui.pushButton_11.clicked.connect(self.add_number)
        self.ui.pushButton_12.clicked.connect(self.add_number)
        self.ui.pushButton_13.clicked.connect(self.add_number)
        self.ui.pushButton_14.clicked.connect(self.add_number)
        self.ui.pushButton_15.clicked.connect(self.add_number)
        self.ui.pushButton_16.clicked.connect(self.hesapla)
        self.ui.pushButton_17.clicked.connect(self.delete)
    def delete(self):
        try:
            text = self.ui.lineEdit.text()
            text = list(text)
            text = text[::-1]
            del text[0]
            text = text[::-1]
            text_tek = ''.join(text)
            self.ui.lineEdit.setText(text_tek)
        except:
            pass

    def hesapla(self):
        text = self.ui.lineEdit.text()
        self.ui.label.setText(str(eval(text)))
        pass

    def add_number(self):
        number = self.sender()
        num = number.text()
        
        if num == '+' or num == '-' or num == '/' or num == '%' or num == 'X':
            

            textbox_Text = self.ui.lineEdit.text()
            textbox_Text = list(textbox_Text)
            textbox_Text = textbox_Text[::-1]
            if textbox_Text[0] == '+' or textbox_Text[0] == '-' or textbox_Text[0] == '/' or textbox_Text[0] == '%' or textbox_Text[0] == 'X':
                pass
            else:
                if num == 'X':
                    self.ui.lineEdit.insert('*')
                else:
                    self.ui.lineEdit.insert(num)
        else:
            self.ui.lineEdit.insert(num)
app = QtWidgets.QApplication(sys.argv)
win = MyApp()
win.show()
sys.exit(app.exec_())