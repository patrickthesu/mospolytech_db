from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox
from kvqtlib.table import tableWidget
from components.inputs import nameInput

class timeIntervalsManage ( QWidget ):
    def __init__ (self, connection):
        self.connect = connection

        super (QWidget, self).__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(QLabel("Управление интервалами"))
        self.setWindowTitle("Управление интервалами")

        self.time_interval = self.connect.get_time_interval_list()

        self.tableWidget = tableWidget(headers = ["ID", "Интервал"], columns = self.time_interval, vertical = False)
        self.layout.addWidget (self.tableWidget)

        self.insertTimeIntervalButton = QPushButton("Добавить интервал")
        self.insertTimeIntervalButton.clicked.connect(self.insertTimeInterval)
        self.layout.addWidget(self.insertTimeIntervalButton)
        self.deleteTimeIntervalButton = QPushButton("Удалить интервал")
        self.deleteTimeIntervalButton.clicked.connect(self.deleteTimeInterval)
        self.layout.addWidget(self.deleteTimeIntervalButton)

    def refresh (self):
        self.time_interval = self.connect.get_time_interval_list()
        self.tableWidget.setTable(self.time_interval, False)

    def insertTimeInterval (self):
        self.insertTimeIntervalWindow = insertTimeInterval (self.connect, function = lambda: self.refresh() )
        self.insertTimeIntervalWindow.show()

    def deleteTimeInterval (self):
        self.deleteTimeIntervalWindow = deleteTimeInterval (self.connect, function = lambda: self.refresh() )
        self.deleteTimeIntervalWindow.show()


class deleteTimeInterval (QWidget):
    def __init__ (self, connection, function = lambda: print ("Succesfully deleted!")): 
        self.connect = connection

        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout )
        
        self.function = function

        self.layout.addWidget ( QLabel ("Введите индекс интервала:"))
        self.time_interval = QSpinBox ()
        self.time_interval.setMinimum (1)
        self.time_interval.setMaximum (10000)
        self.layout.addWidget (self.time_interval)

        self.submitButton = QPushButton ( "Удалить интервал" )
        self.submitButton.clicked.connect ( self.submit )
        self.layout.addWidget ( self.submitButton )

    def submit (self):
        try:
            self.connect.delete_time_interval (self.time_interval.value ())
            self.function ()
            self.close()
        except Exception as err:
            print ("ERROR while deleting time_interval")
            print (err)


class insertTimeInterval ( QWidget ):
    def __init__ (self, connection, function = lambda: print ("Succesfully added time_interval!")): 
        self.connect = connection

        super (QWidget, self).__init__()
        self.setWindowTitle ("Добавить интервал")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.function = function

        self.layout.addWidget(QLabel("Введите полное наименование интервала:"))
        self.name = QLineEdit()
        self.name.setMaxLength(255)
        self.layout.addWidget(self.name)

        self.submitButton = QPushButton("Добавить интервал")
        self.submitButton.clicked.connect(self.submit)
        self.layout.addWidget(self.submitButton)

    def check (self):
        if self.name.text().strip() == "":
            return False
        return True

    def submit (self):
        if not self.check ():
            return False
        try:
            self.connect.insert_time_interval(self.name.text())
            self.function ()
            self.close()
        except Exception as err:
            print ("ERROR while pushing") 
            print (err)
