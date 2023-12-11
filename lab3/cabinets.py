from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox
from kvqtlib.table import tableWidget

class cabinetsManage ( QWidget ):
    def __init__ (self, connection):
        self.connect = connection

        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout )

        self.layout.addWidget ( QLabel ("Управление кабинетами") )
        self.setWindowTitle ("Управление кабинетами")

        self.cabinets = self.connect.get_cabinets_list()

        self.tableWidget = tableWidget(headers = ["ID", "Название"], columns = self.cabinets, vertical = False)
        self.layout.addWidget (self.tableWidget)

        self.insertCabinetButton = QPushButton ( "Добавить кабинет" )
        self.insertCabinetButton.clicked.connect ( self.insertCabinet )
        self.layout.addWidget ( self.insertCabinetButton )
        self.deleteCabinetButton = QPushButton ( "Удалить кабинет" )
        self.deleteCabinetButton.clicked.connect ( self.deleteCabinet )
        self.layout.addWidget ( self.deleteCabinetButton )

    def refresh (self):
        self.cabinets = self.connect.get_cabinets_list()
        self.tableWidget.setTable(self.cabinets, False)

    def insertCabinet (self):
        self.insertCabinetWindow = insertCabinet (self.connect, function = lambda: self.refresh() )
        self.insertCabinetWindow.show()

    def deleteCabinet (self):
        self.deleteCabinetWindow = deleteCabinet (self.connect, function = lambda: self.refresh() )
        self.deleteCabinetWindow.show()



class deleteCabinet (QWidget):
    def __init__ (self, connection, function = lambda: print ("Succesfully deleted!")): 
        self.connect = connection

        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout )
        
        self.function = function

        self.layout.addWidget ( QLabel ("Введите индекс каибинета:"))
        self.cabinet = QSpinBox ()
        self.cabinet.setMinimum (1) 
        self.cabinet.setMaximum (10000)
        self.layout.addWidget (self.cabinet)

        self.submitButton = QPushButton ( "Удалить кабинет" )
        self.submitButton.clicked.connect ( self.submit )
        self.layout.addWidget ( self.submitButton )

    def submit (self):
        try:
            self.connect.delete_cabinet (self.cabinet.value ())
            self.function ()
            self.close()
        except Exception as err:
            print ("ERROR while deleting cabinet")
            print (err)


class insertCabinet ( QWidget ):
    def __init__ (self, connection, function = lambda: print ("Succesfully added cabinet!")): 
        self.connect = connection

        super (QWidget, self).__init__()
        self.setWindowTitle ("Добавить кабинет")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.function = function

        self.layout.addWidget(QLabel("Введите название кабинета:"))
        self.name = QLineEdit()
        self.name.setMaxLength(255)
        self.layout.addWidget(self.name)

        self.submitButton = QPushButton("Добавить кабинет")
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
            self.connect.insert_cabinet(self.name.text())
            self.function ()
            self.close()
        except Exception as err:
            print ("ERROR while pushing")
            print (err)
