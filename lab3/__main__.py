#!/usr/bin/env python3

from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QDoubleSpinBox, QComboBox, QCheckBox, QDateEdit 
from PyQt6.QtCore import pyqtSlot, QDate
from datetime import datetime
import pandas as pd
import sys

from cabinets import cabinetsManage
from teachers import teachersManage
from subjects import subjectsManage
from time_interval import timeIntervalsManage
from schedule_item import scheduleItemsManage
from schedule import scheduleManage

from kvqtlib.table import tableWidget
from kvqtlib.errors import errorWindow
from kvqtlib.files import writeWidget
from components.inputs import nameInput, passwordInput

import models


global DB_ERROR
try:
    connect = models.Connection ()
    DB_ERROR = False
except:
    DB_ERROR = True

class mainMenu ( QWidget ):
    def __init__ (self):
        super (QWidget, self).__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.resize (300, 300)

        self.setWindowTitle("Меню учителя")
        self.layout.addWidget( QLabel ("Меню учителя:"))

        self.cabinetsButton = QPushButton("Управление кабинетами")
        self.cabinetsButton.clicked.connect(self.cabinetsManage)
        self.layout.addWidget(self.cabinetsButton)

        self.teachersButton = QPushButton("Управление учителями")
        self.teachersButton.clicked.connect(self.teachersManage)
        self.layout.addWidget(self.teachersButton )

        self.subjectsButton = QPushButton("Управление дисциплинами")
        self.subjectsButton.clicked.connect(self.subjectsManage)
        self.layout.addWidget ( self.subjectsButton )

        self.timeIntervalButton = QPushButton ("Управление интервалами")
        self.timeIntervalButton.clicked.connect(self.timeIntervalManage)
        self.layout.addWidget(self.timeIntervalButton)

        self.timeIntervalButton = QPushButton ("Управление элементами расписания")
        self.timeIntervalButton.clicked.connect(self.scheduleItemManage)
        self.layout.addWidget(self.timeIntervalButton)

        self.timeIntervalButton = QPushButton ("Управление расписанием")
        self.timeIntervalButton.clicked.connect(self.scheduleManage)
        self.layout.addWidget(self.timeIntervalButton)

        self.exitButton = QPushButton ( "Выйти из приложения" )
        self.exitButton.clicked.connect ( self.close )
        self.layout.addWidget (self.exitButton )
        self.exitButton.setStyleSheet ("color: rgb(255, 178, 178);")

    def cabinetsManage ( self ):
        self.cabinetsManageWindow = cabinetsManage(connect)
        self.cabinetsManageWindow.show()

    def teachersManage ( self ):
        self.teacherManageWindow = teachersManage(connect)
        self.teacherManageWindow.show()

    def subjectsManage ( self ):
        self.subjectManageWindow = subjectsManage(connect)
        self.subjectManageWindow.show()

    def timeIntervalManage(self):
        self.timeIntervalManageWindow = timeIntervalsManage(connect)
        self.timeIntervalManageWindow.show()

    def scheduleItemManage(self):
        self.scheduleItemsManageWindow = scheduleItemsManage(connect)
        self.scheduleItemsManageWindow.show()

    def scheduleManage(self):
        self.scheduleManageWindow = scheduleManage(connect)
        self.scheduleManageWindow.show()

    def getSchedule(self):
        self.scheduleManageWindow = scheduleManage(connect)
        self.scheduleManageWindow.show()


class main ():
    def __init__ (self):
        self.app = QApplication ( sys.argv )
        global DB_ERROR
        if DB_ERROR:
            self.errorWindow = errorWindow ()
            self.errorWindow.errorTemplate ("Ошибка при подключении к базе данных.\nУведомите об этом администратора.")
            self.errorWindow.show ()
        else:
            self.mw = mainMenu()
            self.mw.show()
        self.app.exec()

if __name__ == "__main__":
    app = main ()
