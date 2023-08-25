from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.toplama.clicked.connect(self.hesapma)
        self.ui.cikarma.clicked.connect(self.hesapma)
        self.ui.carpma.clicked.connect(self.hesapma)
        self.ui.bolme.clicked.connect(self.hesapma)

    def hesapma(self):
        sender = self.sender().text()
        result = 0

        if sender == 'Toplama':
            result = int(self.ui.sayi1.text()) + int(self.ui.sayi2.text())
        elif sender == 'Çıkarma':
            result = int(self.ui.sayi1.text()) - int(self.ui.sayi2.text())
        elif sender == 'Bölme':
            result = int(self.ui.sayi1.text()) / int(self.ui.sayi2.text())
        elif sender == 'Çarpma':
            result = int(self.ui.sayi1.text()) * int(self.ui.sayi2.text())
        self.ui.sonuc.setText('sonuç: ' + str(result))

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()