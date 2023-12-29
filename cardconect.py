from card import Ui_Form
from PyQt5.QtWidgets import QWidget

class Card(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)