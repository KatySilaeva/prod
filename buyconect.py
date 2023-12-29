from buy import Ui_Form
from PyQt5.QtWidgets import QWidget
from cardconect import Card
import sqlite3
class Buy(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con2 = sqlite3.connect("C:/Users/User/PycharmProjects/pythonProject6/my_info.sqlite")
        cur2 = self.con2.cursor()
        result2 = cur2.execute("""SELECT card FROM info""").fetchall()
        for i in result2:
            self.comboBox1.addItem(i[0])
        self.nocard.clicked.connect(self.cardpush)


    def cardpush(self):
        self.clikcard=Card()
        self.clikcard.show()