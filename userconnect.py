from user import Ui_Form
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from buyconect import Buy
import sqlite3


class User(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.suma=0
        self.count=0
        self.setupUi(self)
        self.buyp.clicked.connect(self.buypush)
        self.con = sqlite3.connect("db.sqlite")
        cur = self.con.cursor()
        result = cur.execute("""SELECT dish FROM food""").fetchall()
        for i in result:
            self.comboBox.addItem(i[0])
        self.res=[i for i in cur.execute("""SELECT * FROM food""").fetchall()]
        self.tableWidget.setRowCount(len(self.res))
        self.tableWidget.setColumnCount(len(self.res[0]))
        for i, elem in enumerate(self.res):
            for y, val in enumerate(elem):
                self.tableWidget.setItem(i,y, QTableWidgetItem(str(val)))
        self.save.clicked.connect(self.savep)

    def savep(self):
        dish = self.comboBox.currentText()
        for i in self.res:
            if i[1] == dish:
                self.lcdNumber_2.display(self.count + 1)
                self.lcdNumber.display(self.suma + i[3])
                self.suma += i[3]
                self.count+=1

    def buypush(self):
        self.clickbuy = Buy()
        self.clickbuy.show()
