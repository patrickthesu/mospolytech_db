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

class insertExamGradetype (QWidget):
    def __init__ (self, function = lambda: print ("Succesfully added insertExamGradetype!")): 
        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout )

        self.setWindowTitle ("Добавить")
        
        self.function = function

        self.layout.addWidget ( QLabel ("Введите индекс экзамена:"))
        self.exam = QSpinBox ()
        self.exam.setMinimum (1) 
        self.layout.addWidget (self.exam)

        self.layout.addWidget ( QLabel ("Введите индекс профиля обучения:"))
        self.gradetype = QSpinBox () 
        self.gradetype.setMinimum (1)
        self.layout.addWidget ( self.gradetype )

        self.profile = QCheckBox ("Профильный")
        self.layout.addWidget (self.profile)

        self.submitButton = QPushButton ( "Добавить связку" )
        self.submitButton.clicked.connect ( self.submit )
        self.layout.addWidget ( self.submitButton )

    def submit (self):
        try:
            connect.insertExamGradetype (self.exam.value (), self.gradetype.value (), self.profile.isChecked())
            self.function ()
            self.close()
        except Exception as err:
            print ("ERROR while pushing gradetype")
            print (err)

class deleteExamGradetype (QWidget):
    def __init__ (self, function = lambda: print ("Succesfully deleted!")): 
        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout )

        self.setWindowTitle ("Удалить")
        
        self.function = function

        self.layout.addWidget ( QLabel ("Введите индекс экзамена:"))
        self.exam = QSpinBox ()
        self.exam.setMinimum (1) 
        self.layout.addWidget (self.exam)

        self.layout.addWidget ( QLabel ("Введите индекс профиля обучения:"))
        self.gradetype = QSpinBox ()
        self.gradetype.setMinimum (1)
        self.layout.addWidget ( self.gradetype )

        self.submitButton = QPushButton ( "Удалить экзамен" )
        self.submitButton.clicked.connect ( self.submit )
        self.layout.addWidget ( self.submitButton )

    def submit (self):
        try:
            connect.deleteExamGradetype (self.exam.value (), self.gradetype.value ())
            self.function ()
            self.close()
        except Exception as err:
            self.errorWindow = errorWindow ()
            self.errorWindow.errorTemplate ("Ошибка при удалении, убедись что такой индекс существует в таблице.")
            self.errorWindow.show ()
            print ("ERROR while deleting gradetype")
            print (err)

class makeGroups (QWidget):
    def __init__ (self):
        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout )

        self.setWindowTitle ("Создать группы")

        self.allGroups = connect.getGradeTypes ()
        self.groupCombo = QComboBox ()

        for exam in self.allGroups:
            self.groupCombo.addItem ( exam[1], userData = exam[0] )
 
        self.tableWidget = tableWidget ()
        self.layout.addWidget (self.tableWidget)

        self.setTable ()
 
        self.layout.addWidget ( self.groupCombo )
        self.groupCombo.currentIndexChanged.connect ( self.setTable )

        self.bottomLayout = QHBoxLayout ()

        self.bottomWidget = QWidget ()
        self.bottomWidget.setLayout (self.bottomLayout)
        self.layout.addWidget (self.bottomWidget)

        self.exportButton = QPushButton ("Экспортировать в таблицу")
        self.exportButton.clicked.connect (self.exportTable)
        #self.bottomLayout.addWidget (self.exportButton)

        self.updateButton = QPushButton ("Обновить страницу")
        self.updateButton.clicked.connect (self.setTable)
        self.bottomLayout.addWidget (self.updateButton)

        self.getStudetnForSuccessButton = QPushButton ("Рекомендовать/Не рекомендовать к поступлению")
        self.getStudetnForSuccessButton.clicked.connect (self.getStudetnForSuccess)
        self.layout.addWidget (self.getStudetnForSuccessButton)

    def getStudetnForSuccess (self):
        groupData = self.groupCombo.currentData ()
        self.studentSuccess = StudentsSuccesSelecting (groupData)
        self.studentSuccess.show ()

    def setTable ( self ):
        groupData = self.groupCombo.currentData ()

        exams = connect.getExamsByGrade (groupData)

        headers = ["Имя", "Номер телефона", ]
        headers.append ("Зачислен(а)")
        for exam in exams:
            headers.append (exam) 
        headers.append ("Средняя оценка")

        studentsList = connect.getFullGrade ( groupData )  
        
        self.tableWidget.setTable (columns = studentsList, vertical = False)
        self.tableWidget.setHeaders (headers)


        #self.data = {'Имя': [],'Номер':[],'Кабинет': [],'Средняя оценка': []}
        #for student in studentList:
            #self.data['Имя'].append (student[0])
            #self.data['Номер'].append(student[1])
            #self.data['Средняя оценка'].append(student[2])

    #def setStudentsStatus (self):

    def exportTable (self):
        self.writeWidget = writeWidget (writeFunction = self.writeFile)
        self.writeWidget.show()

    def writeFile (self, filename):
        df = pd.DataFrame(self.data)
        df.to_excel (filename + ".xlsx")

class showExamLists (QWidget):
    def __init__ (self):
        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout )

        self.setWindowTitle ("Списки по экзаменам")

        self.allExams = connect.getAllExamsNames ()
        self.examsCombo = QComboBox ()

        for exam in self.allExams:
            self.examsCombo.addItem ( exam[0], userData = exam[1] )
 
        examData = self.examsCombo.currentData ()
        
        studentsList = connect.getFullExam ( examData [0], examData[1] )

        self.data = {'Имя': [],'Номер':[],'Кабинет': [],'Оценка': []}
        for student in studentsList:
            self.data['Имя'].append (student[0])
            self.data['Номер'].append(student[1])
            self.data['Оценка'].append(student[2])

        self.tableWidget = tableWidget ( headers = ["Имя", "Номер телефона", "Кабинет", "Оценка"], columns = studentsList, vertical = False)
        self.layout.addWidget (self.tableWidget)
 
        self.layout.addWidget ( self.examsCombo )
        self.examsCombo.currentIndexChanged.connect ( self.setTable )

        self.exportButton = QPushButton ("Экспортировать в таблицу")
        self.exportButton.clicked.connect (self.exportTable)

        self.bottomLayout = QHBoxLayout ()

        self.bottomWidget = QWidget ()
        self.bottomWidget.setLayout (self.bottomLayout)
        self.layout.addWidget (self.bottomWidget)

        self.exportButton = QPushButton ("Экспортировать в таблицу")
        self.exportButton.clicked.connect (self.exportTable)
        self.bottomLayout.addWidget (self.exportButton)

        self.updateButton = QPushButton ("Обновить страницу")
        self.updateButton.clicked.connect (self.setTable)
        self.bottomLayout.addWidget (self.updateButton)



    def setTable ( self ):
        examData = self.examsCombo.currentData ()
        studentsList = connect.getFullExam ( examData [0], examData[1] )
        self.tableWidget.setTable ( studentsList, vertical = False )
        self.data = {'Имя': [],'Номер':[],'Кабинет': [],'Оценка': []}
        for student in studentsList:
            self.data['Имя'].append (student[0])
            self.data['Номер'].append(student[1])
            self.data['Оценка'].append(student[2])

    def exportTable (self):
        self.writeWidget = writeWidget (writeFunction = self.writeFile)
        self.writeWidget.show()

    def writeFile (self, filename):
        df = pd.DataFrame(self.data)
        df.to_excel (filename + ".xlsx")


class makeExamList ( QWidget ):
    def __init__ ( self ):
        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout )

        self.setWindowTitle ("Сгенерировать экзамены")
        
        self.layout.addWidget (QLabel ("Введите дату проведения:"))
        
        now = datetime.now()

        self.date = QDateEdit(self)
        self.date.setDate(QDate(now.year, now.month, now.day))
        self.layout.addWidget (self.date)
        
        self.autoGenerateButton = QPushButton ( "Сгенерировать автоматически" )
        self.autoGenerateButton.clicked.connect ( self.autoGenerate )
        self.layout.addWidget ( self.autoGenerateButton )

    def autoGenerate (self):
        self.close ()
        connect.makeAutoAllExams (self.date.date().toString("yyyy.MM.dd"))
        self.examLists = showExamLists ()
        self.examLists.show ()


class SetMarkWidget ( QWidget ):
    def __init__ (self, examId, profile, student, function = lambda: print ( "ERROR: invalid SetMarkWidget init" )):
        super (QWidget, self).__init__()
        self.setWindowTitle ("Поставить оценку")
        self.layout = QVBoxLayout ()
        self.setLayout (self.layout)
        self.examId = examId
        self.profile = profile
        self.student = student
        self.function = function

        self.layout.addWidget ( QLabel ("Поставить оценку за екзамен для:") )
        self.layout.addWidget ( QLabel (str ( self.student["student_name"] )) )

        self.markInput = QSpinBox ()
        self.markInput.setMinimum (0)
        self.markInput.setMaximum (100)
        self.layout.addWidget ( self.markInput )

        confirmButton = QPushButton ( "Подтвердить" )
        confirmButton.clicked.connect ( self.setMark )
        self.layout.addWidget (confirmButton)

    def setMark (self):
        try:
            connect.setMark ( self.markInput.value(), self.student["student_id"], self.examId, self.profile )
            self.close ()
            self.function ()
        except Exception as err:
            print ( "ERROR: on setting mark" )
            print ( err )

class StudentsSuccesSelecting ( QWidget ):
    def __init__ ( self, gradetype_id: int ):
        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout ) 

        self.setWindowTitle ("Определить студент")

        self.layout.addWidget (QLabel ("Выберите ученика, которого хотели оценить."))
        
        self.gradetype_id = gradetype_id

        self.studentsList = connect.getStudentsByGradetype (self.gradetype_id)
        self.students = []

        for student in self.studentsList:
            studentButton = QPushButton ( student[0] )
            studentButton.data = student
            studentButton.clicked.connect ( self.setSuccess )
            self.students.append (studentButton)
            self.layout.addWidget (studentButton)

    def isFinal (self):
        for studentButton in self.students:
           if not studentButton.isHidden() : 
                return False
        return True

    @pyqtSlot ()
    def setSuccess (self):
        sender = self.sender()
        sender.hide ()
 
        self.setMark = SetSuccessWidget ( sender.data, self.gradetype_id, lambda: self.endExam () if self.isFinal () else None )
        self.setMark.show()

    def endExam (self):
        print ( "Ending..." )

        self.endWidget = QWidget ()

        layout = QVBoxLayout ()
        layout.addWidget ( QLabel( "Поздравляем вас!\nВы оценили всех учеников." ) )
        closeButton = QPushButton ( "Oк" )
        closeButton.clicked.connect ( lambda: self.endWidget.close () )
        layout.addWidget ( closeButton )

        self.endWidget.setLayout (layout)
        self.endWidget.setWindowTitle ("Конец")

        self.close ()
        self.endWidget.show()

class SetSuccessWidget ( QWidget ):
    def __init__ (self, student, gradetype_id, function = lambda: print ( "ERROR: invalid SetMarkWidget init" )):
        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout (self.layout)
        self.student = student
        self.gradetype_id = gradetype_id
        self.function = function

        self.layout.addWidget ( QLabel ("Выберите рекомендацию к зачислению студента:") )
        self.layout.addWidget ( QLabel (str( self.student[0] )) )

        self.setSuccessButton = QPushButton ("Рекомендован к зачислению")
        self.layout.addWidget (self.setSuccessButton )
        self.setSuccessButton.clicked.connect (self.successStudent)
        self.setUnsuccessButton = QPushButton ("Не рекомендован к зачислению")
        self.layout.addWidget (self.setUnsuccessButton )
        self.setUnsuccessButton.clicked.connect (self.unsuccessStudent)

    def successStudent (self):
        try:
            connect.setSucces ( self.student[1], self.gradetype_id, True )
            self.close ()
            self.function ()
        except Exception as err:
            print ( "ERROR: on setting mark" )
            print ( err )

    def unsuccessStudent (self):
        try:
            connect.setSucces ( self.student[1], self.gradetype_id, False )
            self.close ()
            self.function ()
        except Exception as err:
            print ( "ERROR: on setting mark" )
            print ( err )


class StudentsExamList ( QWidget ):
    def __init__ ( self, examList, examData, teacherId = None, endParent = lambda: print ( "ERROR: Invalid studentExamList init" ) ):
        super (QWidget, self).__init__()
        self.examList = examList
        self.examData = examData
        self.endParent = endParent

        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout )

        self.layout.addWidget ( QLabel ( "Выберите ученика которуму собираетесь поставить оценку:" ))

        self.students =  []

        for student in self.examList:
            studentButton = QPushButton ( student["student_name"] )
            studentButton.data = student
            studentButton.clicked.connect ( self.takeExam )
            self.students.append ( studentButton )
            self.layout.addWidget (studentButton)

    def isFinal (self):
        for studentButton in self.students:
           if not studentButton.isHidden() : 
                return False
        return True

    @pyqtSlot ()
    def takeExam (self):
        sender = self.sender()
        sender.hide ()
 
        self.setMark = SetMarkWidget ( self.examData[0], self.examData[1], sender.data, lambda: self.endExam () if self.isFinal () else None )        
        self.setMark.show()

    def endExam (self):
        print ( "Ending..." )

        self.endWidget = QWidget ()

        layout = QVBoxLayout ()
        layout.addWidget ( QLabel( "Поздравляем вас!\nЕкзамен закончился" ) )
        closeButton = QPushButton ( "Oк" )
        closeButton.clicked.connect ( lambda: self.endWidget.close () )
        layout.addWidget ( closeButton )

        self.endWidget.setLayout ( layout )
        self.endWidget.setWindowTitle ( "Конец" )

        self.close ()
        self.endParent ()
        self.endWidget.show()


class ExamsList (QWidget):
    def __init__ ( self, teacherId = None, function = lambda examsList, examData: print ( "ERROR: invalid ExamsList init" )):
        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout )

        self.function = function

        self.layout.addWidget ( QLabel ("Выберите екзамен который вы хотите провести:") )

        allExams = connect.getAllExamsNames ()
        for exam in allExams:
            examData = exam[1]
            examList = connect.getFullExam ( examData [0], examData[1] )
            if len (examList) == 0: continue

            button = QPushButton ( exam[0] )
            button.data = exam[1]
            button.clicked.connect (self.selectExam)

            self.layout.addWidget ( button )

    @pyqtSlot ()
    def selectExam (self):
        examData =  self.sender().data
        examsList = connect.getFullExam ( examData [0], examData[1], True )
        self.function ( examsList, examData )
               

class Exam ( QWidget ):
    def __init__ (self, teacherId = None):
        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout )

        self.teacherId = teacherId

        self.examsList = ExamsList ( teacherId, self.selectExam )
        self.layout.addWidget (self.examsList)

    def selectExam ( self, examList, examData ):
        self.examsList.hide()
        self.studentExamsList = StudentsExamList ( examList, examData, self.teacherId, self.close )
        self.layout.addWidget (self.studentExamsList)


class examsManage ( QWidget ):
    def __init__ ( self ):
        super (QWidget, self).__init__()
        self.layout = QVBoxLayout ()
        self.setLayout ( self.layout )

        self.layout.addWidget ( QLabel ("Управления экзаменами") )
        self.setWindowTitle ("Управление экзаменами")

        self.cabinets = connect.getExamGradetype ()
        self.tableWidget = tableWidget ( headers = ["Название экзамена", "ID Экзамена", "Название профиля", "ID профиля", "Профильный(Да/Нет)"], columns = self.cabinets, vertical = False)
        self.layout.addWidget (self.tableWidget)
        self.insertCabinetButton = QPushButton ("Добавить экзамен")
        self.insertCabinetButton.clicked.connect ( self.insertCabinet )
        self.layout.addWidget ( self.insertCabinetButton )
        self.deleteExamCabinet = QPushButton ("Удалить экзамен")
        self.deleteExamCabinet.clicked.connect ( self.deleteCabinet )
        self.layout.addWidget ( self.deleteExamCabinet )

    def refresh (self):
        self.cabinets = connect.getExamGradetype ()
        self.tableWidget.setTable ( self.cabinets, False )

    def insertCabinet ( self ):
        self.insertCabinetWindow = insertExamGradetype ( function = lambda: self.refresh() )
        self.insertCabinetWindow.show()

    def deleteCabinet ( self ):
        self.insertCabinetWindow = deleteExamGradetype (function = lambda: self.refresh())
        self.insertCabinetWindow.show()


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
        self.timeIntervalButton = QPushButton ("Управление расписаним")
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
        self.timeIntervalManageWindow = scheduleItemsManage(connect)
        self.timeIntervalManageWindow.show()

    def scheduleManage(self):
        #self.timeIntervalManageWindow = scheduleItemManage(connect)
        self.timeIntervalManageWindow.show()


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
