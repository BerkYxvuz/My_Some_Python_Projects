from PyQt5 import QtWidgets
from msgboxform import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.extbtn.clicked.connect(self.showDialog)
    def showDialog(self):
        msg = QMessageBox()

        msg.setWindowTitle('Kapatmak İstiyor musunuz?')
        msg.setText('Emin misiniz?')

        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
        msg.setDefaultButton(QMessageBox.Ok) # default butonu seçer
        msg.setDetailedText('Programı Kapatır...')
        msg.buttonClicked.connect(self.popup_button)

    def popup_button(self, x):
        if x == x.Ok:
            try:
                sys.exit()
            except:
                print('Hata')
        if x == x.Cancel:
            pass
        if x == x.Ignore:
            print('Ignore ne ya')

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()