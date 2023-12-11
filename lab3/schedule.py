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

        self.tableWidget = tableWidget(headers = ["ID элемента", "Имя учителя", "Кабинет", "Предмет", "День", "Интервал"], columns = self.schedule, vertical = False)
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
        self.schedule = searchWidget()
        self.layout.addWidget(self.schedule)

        for schedule in self.connect.get_extended_schedule_list():
            self.schedule.addItem(f'{schedule[1]}, {schedule[2]}, {schedule[3]}, {schedule[4]}', (schedule[0], schedule[5], schedule[6]))

        self.submitButton = QPushButton ( "Удалить элемент расписания" )
        self.submitButton.clicked.connect ( self.submit )
        self.layout.addWidget ( self.submitButton )

    def submit (self):
        try:
            self.connect.delete_schedule (*self.schedule.currentData())
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

        self.layout.addWidget(QLabel("Введите данные элемента расписания:"))

        self.layout.addWidget(QLabel("Выберите элемент расписания:"))
        self.schedule_item = searchWidget()
        self.layout.addWidget(self.schedule_item)

        for time_interval in self.connect.get_schedule_item_list():
            self.schedule_item.addItem(f'{time_interval[1]}, {time_interval[3]}, {time_interval[4]}', time_interval[0])

        self.layout.addWidget(QLabel("Выберите преподавателя:"))
        self.teacher = searchWidget()
        self.layout.addWidget(self.teacher)

        for teacher in self.connect.get_teacher_list():
            self.teacher.addItem(teacher[1], teacher[0])

        self.layout.addWidget(QLabel("Выберите кабинет:"))
        self.cabinet = searchWidget()
        self.layout.addWidget(self.cabinet)

        for cabinet in self.connect.get_cabinets_list():
            self.cabinet.addItem(cabinet[1], cabinet[0])

        self.submitButton = QPushButton("Добавить полный элемент расписания")
        self.submitButton.clicked.connect(self.submit)
        self.layout.addWidget(self.submitButton)

    def check (self):
        return self.schedule_item.check() and self.teacher.check() and self.cabinet.check()

        
    def submit (self):
        if not self.check ():
            return False
        try:
            self.connect.insert_schedule(
                    self.teacher.currentData(), 
                    self.cabinet.currentData(), 
                    self.schedule_item.currentData()
            )
            self.function ()
            self.close()
        except Exception as err:
            print ("ERROR while pushing")
            print (err)
