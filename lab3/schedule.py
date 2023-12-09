from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox
from kvqtlib.table import tableWidget
from components.selectWidgets import searchWidget

class scheduleManage(QWidget):
    def __init__ (self, connection):
        self.connect = connection

        super (QWidget, self).__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(QLabel("Управление ячейками расписания"))
        self.setWindowTitle("Управление ячейками расписания")

        self.schedule = self.connect.get_schedule_list()

        self.tableWidget = tableWidget(headers = ["ID элемента", "Студенческой группа", "Предмет", "День", "Интервал"], columns = self.schedule, vertical = False)
        self.layout.addWidget (self.tableWidget)

        self.insertschdeuleItemButton = QPushButton("Добавить элемент расписания")
        self.insertschdeuleItemButton.clicked.connect(self.insertSchdeule)
        self.layout.addWidget(self.insertschdeuleItemButton)
        self.deleteschdeuleItemButton = QPushButton("Удалить элемент расписания")
        self.deleteschdeuleItemButton.clicked.connect(self.deleteSchdeule)
        self.layout.addWidget(self.deleteschdeuleItemButton)

    def refresh (self):
        self.schedule = self.connect.get_schedule_list()
        self.tableWidget.setTable(self.schedule, False)

    def insertSchdeule (self):
        self.insertschdeuleItemWindow = insertSchdeule (self.connect, function = lambda: self.refresh() )
        self.insertschdeuleItemWindow.show()

    def deleteSchdeule (self):
        self.deleteschdeuleItemWindow = deleteSchdeule (self.connect, function = lambda: self.refresh() )
        self.deleteschdeuleItemWindow.show()


class deleteSchdeule (QWidget):
    def __init__ (self, connection, function = lambda: print ("Succesfully deleted!")): 
        self.connect = connection

        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout )
        
        self.function = function

        self.layout.addWidget ( QLabel ("Введите индекс элемента расписания:"))
        self.schedule = QSpinBox ()
        self.schedule.setMinimum (1)
        self.schedule.setMaximum (10000)
        self.layout.addWidget (self.schedule)

        self.submitButton = QPushButton ( "Удалить элемент расписания" )
        self.submitButton.clicked.connect ( self.submit )
        self.layout.addWidget ( self.submitButton )

    def submit (self):
        try:
            self.connect.delete_schedule_item (self.schedule.value ())
            self.function ()
            self.close()
        except Exception as err:
            print ("ERROR while deleting schedule")
            print (err)


class insertSchdeule ( QWidget ):
    def __init__ (self, connection, function = lambda: print ("Succesfully added schedule!")): 
        self.connect = connection

        super (QWidget, self).__init__()
        self.setWindowTitle ("Добавить элемент расписания")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.function = function

        self.layout.addWidget(QLabel("Введите данные элемент расписания:"))

        self.layout.addWidget(QLabel("Выберите день:"))
        self.day = searchWidget()
        self.layout.addWidget(self.day)

        for day in self.connect.get_day_list():
            self.day.addItem(day[1], day[0])

        self.layout.addWidget(QLabel("Выберите временной промежуток:"))
        self.time_interval = searchWidget()
        self.layout.addWidget(self.time_interval)

        for time_interval in self.connect.get_time_interval_list():
            self.time_interval.addItem(time_interval[1], time_interval[0])

        self.layout.addWidget(QLabel("Выберите дисциплину:"))
        self.subject = searchWidget()
        self.layout.addWidget(self.subject)

        for subject in self.connect.get_subjects_list():
            self.subject.addItem(subject[1], subject[0])

        self.layout.addWidget(QLabel("Выберите группу:"))
        self.group = searchWidget()
        self.layout.addWidget(self.group)

        for group in self.connect.get_groups_list():
            self.group.addItem(group[1], group[0])

        self.submitButton = QPushButton("Добавить элемент расписания")
        self.submitButton.clicked.connect(self.submit)
        self.layout.addWidget(self.submitButton)

    def check (self):
        return self.day.check() and self.time_interval.check() and self.subject.check() and self.group.check()

        
    def submit (self):
        if not self.check ():
            return False
        try:
            self.connect.insert_schedule_item(self.day.currentData(), self.time_interval.currentData(), self.subject.currentData(), self.group.currentData())
            self.function ()
            self.close()
        except Exception as err:
            print ("ERROR while pushing")
            print (err)
