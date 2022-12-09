import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from qt import Ui_MainWindow
from find_data import FindData

class Example(QMainWindow, Ui_MainWindow, FindData):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Задачник')
        self.all_dates = {}
        self.pushButton.clicked.connect(self.find_date)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())