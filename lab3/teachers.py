from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox
from kvqtlib.table import tableWidget
from components.inputs import nameInput

class teachersManage ( QWidget ):
    def __init__ (self, connection):
        self.connect = connection

        super (QWidget, self).__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(QLabel("Управление учителями"))
        self.setWindowTitle("Управление учителями")

        self.teacher = self.connect.get_teacher_list()

        self.tableWidget = tableWidget(headers = ["ID", "Полное имя"], columns = self.teacher, vertical = False)
        self.layout.addWidget (self.tableWidget)

        self.insertTeacherButton = QPushButton("Добавить учителя")
        self.insertTeacherButton.clicked.connect(self.insertTeacher)
        self.layout.addWidget(self.insertTeacherButton)
        self.deleteTeacherButton = QPushButton("Удалить учителя")
        self.deleteTeacherButton.clicked.connect(self.deleteTeacher)
        self.layout.addWidget(self.deleteTeacherButton)

    def refresh (self):
        self.teacher = self.connect.get_teacher_list()
        self.tableWidget.setTable(self.teacher, False)

    def insertTeacher (self):
        self.insertTeacherWindow = insertTeacher (self.connect, function = lambda: self.refresh() )
        self.insertTeacherWindow.show()

    def deleteTeacher (self):
        self.deleteTeacherWindow = deleteTeacher (self.connect, function = lambda: self.refresh() )
        self.deleteTeacherWindow.show()



class deleteTeacher (QWidget):
    def __init__ (self, connection, function = lambda: print ("Succesfully deleted!")): 
        self.connect = connection

        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout )
        
        self.function = function

        self.layout.addWidget ( QLabel ("Введите индекс учителя:"))
        self.teacher = QSpinBox ()
        self.teacher.setMinimum (1)
        self.teacher.setMaximum (10000)
        self.layout.addWidget (self.teacher)

        self.submitButton = QPushButton ( "Удалить учителя" )
        self.submitButton.clicked.connect ( self.submit )
        self.layout.addWidget ( self.submitButton )

    def submit (self):
        try:
            self.connect.delete_teacher (self.teacher.value ())
            self.function ()
            self.close()
        except Exception as err:
            print ("ERROR while deleting teacher")
            print (err)


class insertTeacher ( QWidget ):
    def __init__ (self, connection, function = lambda: print ("Succesfully added teacher!")): 
        self.connect = connection

        super (QWidget, self).__init__()
        self.setWindowTitle ("Добавить учителя")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.function = function

        self.layout.addWidget(QLabel("Введите полное имя учителя:"))
        self.name = nameInput()
        self.layout.addWidget(self.name)

        self.submitButton = QPushButton("Добавить учителя")
        self.submitButton.clicked.connect(self.submit)
        self.layout.addWidget(self.submitButton)

    def check (self):
        return self.name.check()

    def submit (self):
        if not self.check ():
            return False
        try:
            self.connect.insert_teacher(self.name())
            self.function ()
            self.close()
        except Exception as err:
            print ("ERROR while pushing")
            print (err)
