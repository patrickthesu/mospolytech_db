from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox
from kvqtlib.table import tableWidget
from components.inputs import nameInput

class telegramUsersManage ( QWidget ):
    def __init__ (self, connection):
        self.connect = connection

        super (QWidget, self).__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(QLabel("Управление дисциплинами"))
        self.setWindowTitle("Управление дисциплинами")

        self.telegramUser = self.connect.get_telegram_users_list()

        self.tableWidget = tableWidget(headers = ["ID", "Наименование"], columns = self.telegramUser, vertical = False)
        self.layout.addWidget (self.tableWidget)

        self.insertSubjectButton = QPushButton("Добавить дисциплину")
        self.insertSubjectButton.clicked.connect(self.insertSubject)
        self.layout.addWidget(self.insertSubjectButton)
        self.deleteSubjectButton = QPushButton("Удалить дисциплину")
        self.deleteSubjectButton.clicked.connect(self.deleteSubject)
        self.layout.addWidget(self.deleteSubjectButton)

    def refresh (self):
        self.telegramUser = self.connect.get_telegram_users_list()
        self.tableWidget.setTable(self.telegramUser, False)

    def insertSubject (self):
        self.insertSubjectWindow = insertSubject (self.connect, function = lambda: self.refresh() )
        self.insertSubjectWindow.show()

    def deleteSubject (self):
        self.deleteSubjectWindow = deleteSubject (self.connect, function = lambda: self.refresh() )
        self.deleteSubjectWindow.show()


class deleteSubject (QWidget):
    def __init__ (self, connection, function = lambda: print ("Succesfully deleted!")): 
        self.connect = connection

        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout )
        
        self.function = function

        self.layout.addWidget ( QLabel ("Введите индекс дисциплины:"))
        self.telegramUser = QSpinBox ()
        self.telegramUser.setMinimum (1)
        self.telegramUser.setMaximum (10000)
        self.layout.addWidget (self.telegramUser)

        self.submitButton = QPushButton ( "Удалить дисциплины" )
        self.submitButton.clicked.connect ( self.submit )
        self.layout.addWidget ( self.submitButton )

    def submit (self):
        try:
            self.connect.delete_telegramUser (self.telegramUser.value ())
            self.function ()
            self.close()
        except Exception as err:
            print ("ERROR while deleting telegramUser")
            print (err)


class insertSubject ( QWidget ):
    def __init__ (self, connection, function = lambda: print ("Succesfully added telegramUser!")): 
        self.connect = connection

        super (QWidget, self).__init__()
        self.setWindowTitle ("Добавить дисциплины")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.function = function

        self.layout.addWidget(QLabel("Введите полное наименование дисциплины:"))
        self.name = QLineEdit()
        self.name.setMaxLength(255)
        self.layout.addWidget(self.name)

        self.submitButton = QPushButton("Добавить дисциплину")
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
            self.connect.insert_telegramUser(self.name.text())
            self.function ()
            self.close()
        except Exception as err:
            print ("ERROR while pushing")
            print (err)
