from thank import Ui_Form
from PyQt5.QtWidgets import QWidget
import sqlite3
class Thank(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)