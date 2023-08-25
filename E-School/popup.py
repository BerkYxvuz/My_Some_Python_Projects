# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PopupWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 264)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.soyisim = QtWidgets.QTextEdit(self.centralwidget)
        self.soyisim.setGeometry(QtCore.QRect(80, 50, 150, 30))
        self.soyisim.setObjectName("soyisim")
        self.okulno = QtWidgets.QTextEdit(self.centralwidget)
        self.okulno.setGeometry(QtCore.QRect(80, 90, 150, 30))
        self.okulno.setObjectName("okulno")
        self.isim = QtWidgets.QTextEdit(self.centralwidget)
        self.isim.setGeometry(QtCore.QRect(80, 10, 150, 30))
        self.isim.setToolTip("")
        self.isim.setObjectName("isim")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 150, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 130, 47, 13))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.Add_Student)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Ekle"))
        self.soyisim.setPlaceholderText(_translate("MainWindow", "Soyisim"))
        self.okulno.setPlaceholderText(_translate("MainWindow", "Okul No."))
        self.isim.setPlaceholderText(_translate("MainWindow", "İsim"))
        self.comboBox.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox.setItemText(1, _translate("MainWindow", "B"))
        self.comboBox.setItemText(2, _translate("MainWindow", "C"))
        self.comboBox.setItemText(3, _translate("MainWindow", "D"))
        self.label.setText(_translate("MainWindow", "Sınıf"))
    def Add_Student(self):
        try:
            self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="berk1907",
            database="eschool"
            )
            self.mycursor = self.mydb.cursor()
            # DATA BASE PART FINISHED
            sql = ("INSERT INTO Students(Isim,Soyisim,No,Sinif) VALUES (%s,%s,%s,%s)")
            isim = self.isim.toPlainText()
            soyisim = self.soyisim.toPlainText()
            no = self.okulno.toPlainText()
            sinif = self.comboBox.currentText()
            
            Values = (isim,soyisim,no,sinif)

            self.mycursor.execute(sql,Values)

            self.mydb.commit()

        except Exception as ex:
            print(ex)
            pass
        finally:
            self.mydb.close()
            MainWindoww.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindoww = QtWidgets.QMainWindow()
    uii = Ui_PopupWindow()
    uii.setupUi(MainWindoww)
    MainWindoww.show()
    sys.exit(app.exec_())