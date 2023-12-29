import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from meny import Ui_MainWindow
from userconnect import User



class Meny(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.user.clicked.connect(self.userpush)

    def userpush(self):
        self.clickuser = User()
        self.clickuser.show()

    def adminpush(self):
        self.clickadmin.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Meny()
    ex.show()
    sys.exit(app.exec_())
