from cardn1 import Ui_Form
from PyQt5.QtWidgets import QWidget
from thanconnect import Thank

class Buy(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.cardpush())



    def cardpush(self):
        if self.card.text() == '':
            self.lineEdit_2.setText('Заполните поле')
        else:
            self.clikcard = Thank()
            self.clikcard.show()