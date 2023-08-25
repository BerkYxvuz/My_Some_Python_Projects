import sys
from PyQt5 import QtWidgets
from datetimeform import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCalculate.clicked.connect(self.calculate)
    def calculate(self):
        start = self.ui.datestart.date()
        end = self.ui.dateend.date()

        print(start, end)

        print('Days in month: {0}'.format(start.daysInMonth()))

        print('total days: {0}'.format(start.daysTo(end)))

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()