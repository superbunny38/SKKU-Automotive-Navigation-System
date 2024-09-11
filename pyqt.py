import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

global startX, startY, destX, destY, startC, destC
global myeong, yul
global user_loc


class node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None


class stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def push(self, x, y):
        new_node = node(x, y)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if (self.is_empty()):
            return
        del_node = self.top
        resultX = self.top.x
        resultY = self.top.y
        self.top = del_node.next
        del del_node
        self.size -= 1
        return resultX, resultY

    def peek(self):
        if (self.is_empty()):
            return
        return self.top.x, self.top.y
        # point=self.top.point
        # return point

    def print(self):
        tmp = stack()
        count = self.count()
        for i in range(count):
            point1, point2 = self.pop()  ##
            tmp.push(point1, point2)
        for i in range(count):
            point1, point2 = tmp.pop()
            print("({}.{})".format(point1, point2), end=' ')  ##
            self.push(point1, point2)

    def is_empty(self):
        if (self.count() == 0):
            return True
        else:
            return False

    def count(self):
        return self.size

    def clear(self):
        while (self.top):
            self.pop()


# 지도 초기화
def init_Map():
    global myeong
    global yul
    myeong = [
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    yul = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


class map_myeongryun(object):
    def m_start_point(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = m_input_start_point()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def m_destination_point(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = m_input_destination_point()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def myeongryun_move(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = m_move()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 360, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("명륜캠 지도.jpg"))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 599, 361, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.m_start_point)
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.m_destination_point)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_2")
        self.pushButton_3.clicked.connect(self.myeongryun_move)
        self.verticalLayout.addWidget(self.pushButton_3)

        self.retranslateUi(Dialog)
        self.pushButton_3.clicked.connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.pushButton.setText(_translate("Dialog", "Starting Location"))
        self.pushButton_2.setText(_translate("Dialog", "Destination"))
        self.pushButton_3.setText(_translate("Dialog", "Find Path"))


class m_input_start_point(object):
    def start_1(self):
        global startX, startY
        startX = 28
        startY = 16

    def start_2(self):
        global startX, startY
        startX = 9
        startY = 16

    def start_3(self):
        global startX, startY
        startX = 21
        startY = 11

    def start_4(self):
        global startX, startY
        startX = 0
        startY = 3

    def setupUi(self, Dialog):
        global startC
        startC = 1
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 360, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("명륜캠 시작점.jpg"))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 590, 181, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(30, 0, 15, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.start_1)
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.start_2)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(180, 590, 181, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(15, 0, 30, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.start_3)
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.start_4)
        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.hide)
        self.pushButton_3.clicked.connect(Dialog.hide)
        self.pushButton_2.clicked.connect(Dialog.hide)
        self.pushButton_4.clicked.connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.pushButton.setText(_translate("Dialog", "Main Entrance (정문)"))
        self.pushButton_2.setText(_translate("Dialog", "Iron Entrance (철문)"))
        self.pushButton_3.setText(_translate("Dialog", "Side Entrance (쪽문)"))
        self.pushButton_4.setText(_translate("Dialog", "Back Entrance (후문)"))


class m_input_destination_point(object):
    def m_classroom(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = m_select_classroom()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def m_amenities(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = m_find_amenities()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def y_destination_point(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = y_input_destination_point()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

        global destC
        destC = 2

    def setupUi(self, Dialog):
        global destC
        destC = 1
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 360, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("명륜캠 지도.jpg"))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 599, 361, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.m_classroom)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.m_amenities)
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.y_destination_point)
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.hide)
        self.pushButton_3.clicked.connect(Dialog.hide)
        self.pushButton.clicked.connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.pushButton_2.setText(_translate("Dialog", "Find Classrooms"))
        self.pushButton_3.setText(_translate("Dialog", "Find Amenities"))
        self.pushButton.setText(_translate("Dialog", "Suwon Campus"))


class m_select_classroom(object):
    def classroom_as_name(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = m_classroom_as_name()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def classroom_as_number(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = m_classroom_as_number()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 360, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("명륜캠 지도.jpg"))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 599, 361, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.classroom_as_number)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.classroom_as_name)
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.hide)
        self.pushButton.clicked.connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.pushButton_2.setText(_translate("Dialog", "Search Classroom by Number"))
        self.pushButton.setText(_translate("Dialog", "Search Classroom by Name"))


class m_classroom_as_number(object):
    def select_number(self):
        global destX, destY

        n = self.textEdit.toPlainText()
        int_n = int(n)

        n12 = int_n // 1000
        n3 = (int_n - n12 * 1000) // 100
        n45 = int_n % 100

        if n12 == 1:
            print("600주년 기념관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 15
            destY = 13
        elif n12 == 2:
            print("법학관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 9
            destY = 3
        elif n12 == 9:
            print("국제관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 18
            destY = 14
        elif n12 == 31:
            print("인문관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 4
            destY = 9
        elif n12 == 32:
            print("다산경제관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 4
            destY = 9
        elif n12 == 33:
            print("경영관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 8
            destY = 10
        elif n12 == 61:
            print("수선관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 6
            destY = 5
        elif n12 == 2:
            print("수선관 별관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 4
            destY = 4
        elif n12 == 50:
            print("호암관1")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 8
            destY = 8
        elif n12 == 51:
            print("호암관2")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 6
            destY = 9
        else:
            print("입력한 번호의 건물이 존재하지 않습니다")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 360, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("명륜캠 지도.jpg"))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(40, 610, 141, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.select_number)
        self.pushButton.setGeometry(QtCore.QRect(210, 610, 121, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.pushButton.setText(_translate("Dialog", "Set Destination"))


class m_classroom_as_name(object):
    def m_classroom_1(self):
        global destX, destY
        destX = 18
        destY = 14

    def m_classroom_2(self):
        global destX, destY
        destX = 8
        destY = 10

    def m_classroom_3(self):
        global destX, destY
        destX = 4
        destY = 9

    def m_classroom_4(self):
        global destX, destY
        destX = 4
        destY = 9

    def m_classroom_5(self):
        global destX, destY
        destX = 8
        destY = 8

    def m_classroom_6(self):
        global destX, destY
        destX = 6
        destY = 9

    def m_classroom_7(self):
        global destX, destY
        destX = 6
        destY = 5

    def m_classroom_8(self):
        global destX, destY
        destX = 4
        destY = 4

    def m_classroom_9(self):
        global destX, destY
        destX = 9
        destY = 3

    def m_classroom_10(self):
        global destX, destY
        destX = 15
        destY = 13

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 750)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 360, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("명륜캠 지도.jpg"))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(10, 600, 108, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 600, 108, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(250, 600, 108, 19))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(250, 630, 108, 19))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 630, 108, 19))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_6.setGeometry(QtCore.QRect(130, 630, 108, 19))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 660, 108, 19))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_8.setGeometry(QtCore.QRect(130, 660, 108, 19))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_9.setGeometry(QtCore.QRect(250, 660, 108, 19))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_10.setGeometry(QtCore.QRect(110, 690, 141, 19))
        self.radioButton_10.setObjectName("radioButton_10")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 720, 221, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.hide)
        self.radioButton.clicked.connect(self.m_classroom_1)
        self.radioButton_2.clicked.connect(self.m_classroom_2)
        self.radioButton_3.clicked.connect(self.m_classroom_3)
        self.radioButton_4.clicked.connect(self.m_classroom_4)
        self.radioButton_5.clicked.connect(self.m_classroom_5)
        self.radioButton_6.clicked.connect(self.m_classroom_6)
        self.radioButton_7.clicked.connect(self.m_classroom_7)
        self.radioButton_8.clicked.connect(self.m_classroom_8)
        self.radioButton_9.clicked.connect(self.m_classroom_9)
        self.radioButton_10.clicked.connect(self.m_classroom_10)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.radioButton.setText(_translate("Dialog", "국제관"))
        self.radioButton_2.setText(_translate("Dialog", "경영관"))
        self.radioButton_3.setText(_translate("Dialog", "다산경제관"))
        self.radioButton_4.setText(_translate("Dialog", "퇴계인문관"))
        self.radioButton_5.setText(_translate("Dialog", "호암관1"))
        self.radioButton_6.setText(_translate("Dialog", "호암관2"))
        self.radioButton_7.setText(_translate("Dialog", "수선관"))
        self.radioButton_8.setText(_translate("Dialog", "수선관 별관"))
        self.radioButton_9.setText(_translate("Dialog", "법학관"))
        self.radioButton_10.setText(_translate("Dialog", "600주년 기념관"))
        self.pushButton.setText(_translate("Dialog", "Set Destination"))


class m_find_amenities(object):
    def m_amenity_1(self):
        global destX, destY
        destX = 7
        destY = 12

    def m_amenity_2(self):
        global destX, destY
        destX = 8
        destY = 10

    def m_amenity_3(self):
        global destX, destY
        destX = 4
        destY = 9

    def m_amenity_4(self):
        global destX, destY
        destX = 8
        destY = 10

    def m_amenity_5(self):
        global destX, destY
        destX = 7
        destY = 12

    def m_amenity_6(self):
        global destX, destY
        destX = 4
        destY = 9

    def m_amenity_7(self):
        global destX, destY
        destX = 12
        destY = 10

    def m_amenity_8(self):
        global destX, destY
        destX = 15
        destY = 13

    def m_amenity_9(self):
        global destX, destY
        destX = 18
        destY = 14

    def m_amenity_10(self):
        global destX, destY
        destX = 9
        destY = 13

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 770)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 360, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("명륜캠 편의시설.jpg"))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(13, 600, 108, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(133, 600, 108, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(240, 600, 121, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(13, 630, 108, 19))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(240, 630, 121, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_6.setGeometry(QtCore.QRect(133, 630, 108, 19))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_7.setGeometry(QtCore.QRect(240, 660, 121, 20))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_8.setGeometry(QtCore.QRect(13, 660, 108, 19))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_9.setGeometry(QtCore.QRect(133, 660, 108, 19))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_10.setGeometry(QtCore.QRect(110, 690, 141, 20))
        self.radioButton_10.setObjectName("radioButton_10")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 720, 171, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.hide)
        self.radioButton.clicked.connect(self.m_amenity_1)
        self.radioButton_2.clicked.connect(self.m_amenity_2)
        self.radioButton_3.clicked.connect(self.m_amenity_3)
        self.radioButton_4.clicked.connect(self.m_amenity_4)
        self.radioButton_5.clicked.connect(self.m_amenity_5)
        self.radioButton_6.clicked.connect(self.m_amenity_6)
        self.radioButton_7.clicked.connect(self.m_amenity_7)
        self.radioButton_8.clicked.connect(self.m_amenity_8)
        self.radioButton_9.clicked.connect(self.m_amenity_9)
        self.radioButton_10.clicked.connect(self.m_amenity_10)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.radioButton.setText(_translate("Dialog", "교수회관"))
        self.radioButton_2.setText(_translate("Dialog", "편의점 경영"))
        self.radioButton_3.setText(_translate("Dialog", "편의점 인문"))
        self.radioButton_4.setText(_translate("Dialog", "ATM 경영"))
        self.radioButton_5.setText(_translate("Dialog", "ATM 교수회관"))
        self.radioButton_6.setText(_translate("Dialog", "ATM 인문"))
        self.radioButton_7.setText(_translate("Dialog", "ATM 학생회관"))
        self.radioButton_8.setText(_translate("Dialog", "ATM 600주년"))
        self.radioButton_9.setText(_translate("Dialog", "ATM 국제관"))
        self.radioButton_10.setText(_translate("Dialog", "ATM 중앙도서관"))
        self.pushButton.setText(_translate("Dialog", "Set Destination"))


class map_yuljeon(object):
    def y_start_point(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = y_input_start_point()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def y_destination_point(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = y_input_destination_point()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def yuljeon_move(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = y_move()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 540))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("율전캠 지도.jpg"))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 540, 481, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.y_start_point)
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.y_destination_point)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_2")
        self.pushButton_3.clicked.connect(self.yuljeon_move)
        self.verticalLayout.addWidget(self.pushButton_3)

        self.retranslateUi(Dialog)
        self.pushButton_3.clicked.connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.pushButton.setText(_translate("Dialog", "Starting Location"))
        self.pushButton_2.setText(_translate("Dialog", "Destination"))
        self.pushButton_3.setText(_translate("Dialog", "Find Path"))


class y_input_start_point(object):
    def start_1(self):
        global startX, startY
        startX = 13
        startY = 0

    def start_2(self):
        global startX, startY
        startX = 0
        startY = 18

    def setupUi(self, Dialog):
        global startC
        startC = 2
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 540))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("율전캠 시작점.jpg"))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 540, 481, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.start_1)
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.start_2)
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.hide)
        self.pushButton_2.clicked.connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.pushButton.setText(_translate("Dialog", "Main Entrance (정문)"))
        self.pushButton_2.setText(_translate("Dialog", "Back Entrance (후문)"))


class y_input_destination_point(object):
    def y_classroom(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = y_select_classroom()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def y_amenities(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = y_find_amenities()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def m_destination_point(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = m_input_destination_point()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

        global destC
        destC = 1

    def setupUi(self, Dialog):
        global destC
        destC = 2
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 540))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("율전캠 지도.jpg"))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 539, 481, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.y_classroom)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.y_amenities)
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.m_destination_point)
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.hide)
        self.pushButton_3.clicked.connect(Dialog.hide)
        self.pushButton.clicked.connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.pushButton_2.setText(_translate("Dialog", "Find Classrooms"))
        self.pushButton_3.setText(_translate("Dialog", "Find Amenities"))
        self.pushButton.setText(_translate("Dialog", "Hyehwa Campus"))


class y_select_classroom(object):
    def classroom_as_name(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = y_classroom_as_name()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def classroom_as_number(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = y_classroom_as_number()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 540))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("율전캠 지도.jpg"))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 540, 481, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.classroom_as_number)
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.classroom_as_name)
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.hide)
        self.pushButton_2.clicked.connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.pushButton.setText(_translate("Dialog", "Search Classroom by Number"))
        self.pushButton_2.setText(_translate("Dialog", "Search Classroom by Name"))


class y_classroom_as_number(object):
    def select_number(self):
        global destX, destY

        n = self.textEdit.toPlainText()
        int_n = int(n)

        n12 = int_n // 1000
        n3 = (int_n - n12 * 1000) // 100
        n45 = int_n % 100

        if n12 == 71:
            print("의학관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 10
            destY = 6
        elif n12 == 53:
            print("약학관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 19
            destY = 6
        elif n12 == 33:
            print("화학관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 21
            destY = 5

        elif n12 == 40:
            print("반도체관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 23
            destY = 6

        elif n12 == 81:
            print("제1종합연구동")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 24
            destY = 8

        elif n12 == 83:
            print("제2종합연구동")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 23
            destY = 10

        elif 21 <= n12 and n12 <= 23:
            print("제1공학관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 16
            destY = 12

        elif 25 <= n12 and n12 <= 27:
            print("제2공학관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 16
            destY = 16

        elif n12 == 31:
            print("제1과학관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 15
            destY = 17

        elif n12 == 32:
            print("제2과학관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 14
            destY = 17

        elif n12 == 51:
            print("기초학문관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 13
            destY = 18

        elif n12 == 61 or n12 == 62:
            print("생명공학관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 10
            destY = 19

        elif n12 == 5:
            print("수성관")
            print(n3, "층")
            print(n45, "호 강의실입니다.")
            destX = 7
            destY = 6

        else:
            print("입력한 번호의 건물이 존재하지 않습니다")
            destX = 0
            destY = 0

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 540))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("율전캠 지도.jpg"))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(40, 570, 201, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.select_number)
        self.pushButton.setGeometry(QtCore.QRect(260, 570, 181, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.pushButton.setText(_translate("Dialog", "Set Destination"))


class y_classroom_as_name(object):
    def y_classroom_1(self):
        global destX, destY
        destX = 10
        destY = 6

    def y_classroom_2(self):
        global destX, destY
        destX = 19
        destY = 6

    def y_classroom_3(self):
        global destX, destY
        destX = 23
        destY = 6

    def y_classroom_4(self):
        global destX, destY
        destX = 21
        destY = 5

    def y_classroom_5(self):
        global destX, destY
        destX = 16
        destY = 16

    def y_classroom_6(self):
        global destX, destY
        destX = 23
        destY = 10

    def y_classroom_7(self):
        global destX, destY
        destX = 24
        destY = 8

    def y_classroom_8(self):
        global destX, destY
        destX = 16
        destY = 12

    def y_classroom_9(self):
        global destX, destY
        destX = 10
        destY = 19

    def y_classroom_10(self):
        global destX, destY
        destX = 14
        destY = 17

    def y_classroom_11(self):
        global destX, destY
        destX = 15
        destY = 17

    def y_classroom_12(self):
        global destX, destY
        destX = 13
        destY = 18

    def y_classroom_13(self):
        global destX, destY
        destX = 7
        destY = 6

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 540))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("율전캠 지도.jpg"))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(10, 550, 108, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 550, 108, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(370, 550, 108, 19))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(250, 550, 108, 19))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(370, 580, 108, 19))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_6.setGeometry(QtCore.QRect(130, 580, 108, 19))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 580, 108, 19))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_8.setGeometry(QtCore.QRect(250, 580, 108, 19))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_9.setGeometry(QtCore.QRect(370, 610, 108, 19))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_10.setGeometry(QtCore.QRect(130, 610, 108, 19))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_11 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_11.setGeometry(QtCore.QRect(10, 610, 108, 19))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_12 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_12.setGeometry(QtCore.QRect(250, 610, 108, 19))
        self.radioButton_12.setObjectName("radioButton_12")
        self.radioButton_13 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_13.setGeometry(QtCore.QRect(190, 640, 108, 19))
        self.radioButton_13.setObjectName("radioButton_13")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 670, 241, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.hide)
        self.radioButton.clicked.connect(self.y_classroom_1)
        self.radioButton_2.clicked.connect(self.y_classroom_2)
        self.radioButton_3.clicked.connect(self.y_classroom_3)
        self.radioButton_4.clicked.connect(self.y_classroom_4)
        self.radioButton_5.clicked.connect(self.y_classroom_5)
        self.radioButton_6.clicked.connect(self.y_classroom_6)
        self.radioButton_7.clicked.connect(self.y_classroom_7)
        self.radioButton_8.clicked.connect(self.y_classroom_8)
        self.radioButton_9.clicked.connect(self.y_classroom_9)
        self.radioButton_10.clicked.connect(self.y_classroom_10)
        self.radioButton_11.clicked.connect(self.y_classroom_11)
        self.radioButton_12.clicked.connect(self.y_classroom_12)
        self.radioButton_13.clicked.connect(self.y_classroom_13)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.radioButton.setText(_translate("Dialog", "의학관"))
        self.radioButton_2.setText(_translate("Dialog", "약학관"))
        self.radioButton_3.setText(_translate("Dialog", "반도체관"))
        self.radioButton_4.setText(_translate("Dialog", "화학관"))
        self.radioButton_5.setText(_translate("Dialog", "제2공학관"))
        self.radioButton_6.setText(_translate("Dialog", "제2연구동"))
        self.radioButton_7.setText(_translate("Dialog", "제1연구동"))
        self.radioButton_8.setText(_translate("Dialog", "제1공학관"))
        self.radioButton_9.setText(_translate("Dialog", "생명공학관"))
        self.radioButton_10.setText(_translate("Dialog", "제2과학관"))
        self.radioButton_11.setText(_translate("Dialog", "제1과학관"))
        self.radioButton_12.setText(_translate("Dialog", "기초학문관"))
        self.radioButton_13.setText(_translate("Dialog", "수성관"))
        self.pushButton.setText(_translate("Dialog", "도착지 설정"))


class y_find_amenities(object):
    def y_amenity_1(self):
        global destX, destY
        destX = 6
        destY = 5

    def y_amenity_2(self):
        global destX, destY
        destX = 9
        destY = 11

    def y_amenity_3(self):
        global destX, destY
        destX = 8
        destY = 11

    def y_amenity_4(self):
        global destX, destY
        destX = 13
        destY = 9

    def y_amenity_5(self):
        global destX, destY
        destX = 18
        dextY = 21

    def y_amenity_6(self):
        global destX, destY
        destX = 10
        destY = 22

    def y_amenity_7(self):
        global destX, destY
        destX = 8
        destY = 19

    def y_amenity_8(self):
        global destX, destY
        destX = 13
        destY = 20

    def y_amenity_9(self):
        global destX, destY
        destX = 5
        destY = 18

    def y_amenity_10(self):
        global destX, destY
        destX = 8
        destY = 11

    def y_amenity_11(self):
        global destX, destY
        destX = 8
        destY = 19

    def y_amenity_12(self):
        global destX, destY
        destX = 16
        destY = 16

    def y_amenity_13(self):
        global destX, destY
        destX = 13
        destY = 20

    def y_amenity_14(self):
        global destX, destY
        destX = 5
        destY = 18

    def y_amenity_15(self):
        global destX, destY
        destX = 10
        destY = 22

    def y_amenity_16(self):
        global destX, destY
        destX = 16
        destY = 16

    def y_amenity_17(self):
        global destX, destY
        destX = 13
        destY = 9

    def y_amenity_18(self):
        global destX, destY
        destX = 8
        destY = 11

    def y_amenity_19(self):
        global destX, destY
        destX = 21
        destY = 5

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 740)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 540))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("율전캠 편의시설.jpg"))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(20, 540, 108, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 540, 108, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(350, 540, 108, 19))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(240, 540, 108, 19))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(350, 570, 108, 19))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_6.setGeometry(QtCore.QRect(130, 570, 108, 19))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_7.setGeometry(QtCore.QRect(20, 570, 108, 19))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_8.setGeometry(QtCore.QRect(240, 570, 108, 19))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_10 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_10.setGeometry(QtCore.QRect(50, 660, 141, 19))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_11 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_11.setGeometry(QtCore.QRect(200, 660, 108, 19))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_12 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_12.setGeometry(QtCore.QRect(320, 660, 131, 19))
        self.radioButton_12.setObjectName("radioButton_12")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 700, 181, 28))
        self.pushButton.setObjectName("pushButton")
        self.radioButton_9 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_9.setGeometry(QtCore.QRect(20, 600, 108, 19))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_13 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_13.setGeometry(QtCore.QRect(350, 600, 108, 19))
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_14 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_14.setGeometry(QtCore.QRect(130, 600, 108, 19))
        self.radioButton_14.setObjectName("radioButton_14")
        self.radioButton_15 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_15.setGeometry(QtCore.QRect(240, 600, 108, 19))
        self.radioButton_15.setObjectName("radioButton_15")
        self.radioButton_16 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_16.setGeometry(QtCore.QRect(350, 630, 121, 19))
        self.radioButton_16.setObjectName("radioButton_16")
        self.radioButton_17 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_17.setGeometry(QtCore.QRect(130, 630, 108, 19))
        self.radioButton_17.setObjectName("radioButton_17")
        self.radioButton_18 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_18.setGeometry(QtCore.QRect(20, 630, 108, 19))
        self.radioButton_18.setObjectName("radioButton_18")
        self.radioButton_19 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_19.setGeometry(QtCore.QRect(240, 630, 108, 19))
        self.radioButton_19.setObjectName("radioButton_19")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.hide)
        self.radioButton.clicked.connect(self.y_amenity_1)
        self.radioButton_2.clicked.connect(self.y_amenity_2)
        self.radioButton_3.clicked.connect(self.y_amenity_3)
        self.radioButton_4.clicked.connect(self.y_amenity_4)
        self.radioButton_5.clicked.connect(self.y_amenity_5)
        self.radioButton_6.clicked.connect(self.y_amenity_6)
        self.radioButton_7.clicked.connect(self.y_amenity_7)
        self.radioButton_8.clicked.connect(self.y_amenity_8)
        self.radioButton_9.clicked.connect(self.y_amenity_9)
        self.radioButton_10.clicked.connect(self.y_amenity_10)
        self.radioButton_11.clicked.connect(self.y_amenity_11)
        self.radioButton_12.clicked.connect(self.y_amenity_12)
        self.radioButton_13.clicked.connect(self.y_amenity_13)
        self.radioButton_14.clicked.connect(self.y_amenity_14)
        self.radioButton_15.clicked.connect(self.y_amenity_15)
        self.radioButton_16.clicked.connect(self.y_amenity_16)
        self.radioButton_17.clicked.connect(self.y_amenity_17)
        self.radioButton_18.clicked.connect(self.y_amenity_18)
        self.radioButton_19.clicked.connect(self.y_amenity_19)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.radioButton.setText(_translate("Dialog", "의대 대강당"))
        self.radioButton_2.setText(_translate("Dialog", "학생회관"))
        self.radioButton_3.setText(_translate("Dialog", "복지회관"))
        self.radioButton_4.setText(_translate("Dialog", "학술 정보관"))
        self.radioButton_5.setText(_translate("Dialog", "기숙사 <지>"))
        self.radioButton_6.setText(_translate("Dialog", "기숙사 <의>"))
        self.radioButton_7.setText(_translate("Dialog", "기숙사 <인>"))
        self.radioButton_8.setText(_translate("Dialog", "기숙사 <예>"))
        self.radioButton_10.setText(_translate("Dialog", "편의점 복지회관"))
        self.radioButton_11.setText(_translate("Dialog", "편의점 <인>"))
        self.radioButton_12.setText(_translate("Dialog", "편의점 제2공학"))
        self.pushButton.setText(_translate("Dialog", "도착지 설정"))
        self.radioButton_9.setText(_translate("Dialog", "기숙사 <신>"))
        self.radioButton_13.setText(_translate("Dialog", "ATM <예>"))
        self.radioButton_14.setText(_translate("Dialog", "ATM <신>"))
        self.radioButton_15.setText(_translate("Dialog", "ATM <의>"))
        self.radioButton_16.setText(_translate("Dialog", "ATM 제2공학"))
        self.radioButton_17.setText(_translate("Dialog", "ATM 디도"))
        self.radioButton_18.setText(_translate("Dialog", "ATM 복지"))
        self.radioButton_19.setText(_translate("Dialog", "ATM 화학관"))


class m_move(object):
    def suttle_timetable(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = campus_move()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def finish(self):
        Dialog.show()

    def move_loc_up(self, campus_code, user_location):
        nowX, nowY = user_location.peek()
        is_move = 1
        if (nowX == 0):
            nowX += 1
            is_move = 0
        nowX = -1

        user_location.push(nowX, nowY)

    def move_loc_down(self, campus_code, user_location):
        nowX, nowY = user_location.peek()
        is_move = 1
        if ((campus_code == 1 and nowX == 29) or (campus_code == 2 and nowX == 26)):
            nowX -= 1
            is_move = 0
        nowX += 1

        user_location.push(nowX, nowY)

    def move_loc_left(self, campus_code, user_location):
        nowX, nowY = user_location.peek()
        is_move = 1
        if (nowY == 0):
            nowY += 1
            is_move = 0
        nowY -= 1

        user_location.push(nowX, nowY)

    def move_loc_right(self, campus_code, user_location):
        nowX, nowY = user_location.peek()
        is_move = 1
        if ((campus_code == 1 and nowY == 17) or (campus_code == 2 and nowY == 23)):
            nowY -= 1
            is_move = 0
        nowY += 1

        user_location.push(nowX, nowY)

    def is_follow(self, route, user_location):
        global startX, startY, destX, destY, startC, destC
        destination = [destX, destY]
        if (route.peek() == user_location.peek()):
            route.pop()
            if (user_location.peek() == destination):
                print("Arrived at the Destination.")
                print("Terminating your navigation.")
                return
            self.move_loc(route, user_location)
            self.is_follow(route, user_location)
        else:
            print("You are off the course.")
            now_location = user_location.peek()
            user_location.claer()
            self.find_way(now_location[0], now_location[1], destX, destY, startC, destC)
            self.is_follow(route, user_location)

    def find_way(self, startX, startY, destX, destY, startC, destC):
        if (startC == destC):
            self.print_route(startC, startX, startY, destX, destY)
            print("finish")
        elif startC == 1 and destC == 2:
            self.print_route(startC, startX, startY, 14, 12)  ##
            print("finish")
        else:
            self.print_route(destC, 14, 12, destX, destY)
            print("finish")

    def print_shuttle_bus_table(self):
        if startC == destC:
            QMessageBox.about(None, "유생 길라잡이", "같은 캠퍼스 내 이동 중입니다.\n프로그램이 종료됩니다.")
        elif startC == 2 and destC == 1:
            QMessageBox.about(None, "유생 길라잡이", "이미 셔틀버스를 탑승하셨습니다.\n프로그램이 종료됩니다.")
        else:
            self.suttle_timetable()


    def print_maze(self, campus_code):
        if campus_code == 1:
            for i in range(30):
                for j in range(18):
                    if (myeong[i][j] == 1):
                        print("■", end='')
                    elif (myeong[i][j] == 2):
                        print("○", end='')
                    elif (myeong[i][j] == 3):
                        print("☆", end='')
                    elif (myeong[i][j] == 5):  # 선택된 최단 경로
                        print("♡", end='')
                    else:
                        print("□", end='')
                print(end='\n')
            print("\n\n")
        elif campus_code == 2:
            for i in range(27):
                for j in range(24):
                    if (yul[i][j] == 1):
                        print("■", end='')
                    elif (yul[i][j] == 2):
                        print("○", end='')
                    elif (yul[i][j] == 3):
                        print("☆", end='')
                    elif (yul[i][j] == 5):  # 선택된 최단 경로
                        print("♡", end='')
                    else:
                        print("□", end='')
                print(end='\n')
            print("\n\n")

    def print_route(self, campus_code, startX, startY, destX, destY):
        global user_loc
        user_loc = stack()
        route = self.select_shortest_route(campus_code, startX, startY, destX, destY)
        count = route.size
        self.get_estimate_time(campus_code, count)
        ptr = stack()
        if campus_code == 1:
            while (route.size != 0):
                x, y = route.pop()
                myeong[x][y] = 5
                ptr.push(x, y)
        elif campus_code == 2:
            while (route.size != 0):
                x, y = route.pop()
                yul[x][y] = 5
                ptr.push(x, y)

        ptr.print()
        print("\n")

        for i in range(count):
            ptrX, ptrY = ptr.pop()
            user_loc.push(ptrX, ptrY)

        self.print_maze(campus_code)

    def find_route(self, campus_code, startX, startY, destX, destY, dir):
        init_Map()
        cur = node(startX, startY)
        route = stack()

        while True:
            if (campus_code == 1):
                myeong[cur.x][cur.y] = 2
                if (cur.x == destX and cur.y == destY):
                    # print("destination")
                    break
                forward = False
                count = 0
                direction = dir
                while (count < 4):
                    count += 1
                    if (direction == 4):
                        direction = 0
                    if (self.movable(campus_code, cur.x, cur.y, direction)):
                        route.push(cur.x, cur.y)
                        cur = self.move_to(cur, direction)
                        forward = True
                        break
                    direction += 1
                if (forward == False):
                    myeong[cur.x][cur.y] = 3
                    if (route.is_empty()):
                        print("no path")
                        break
                    cur.x, cur.y = route.pop()


            elif (campus_code == 2):
                yul[cur.x][cur.y] = 2
                if (cur.x == destX and cur.y == destY):
                    break
                forward = False
                count = 0
                direction = dir
                while (count < 4):
                    count += 1
                    if (direction == 4):
                        direction = 0
                    if (self.movable(campus_code, cur.x, cur.y, direction)):
                        route.push(cur.x, cur.y)
                        cur = self.move_to(cur, direction)
                        forward = True
                        break
                    direction += 1
                if (forward == False):
                    yul[cur.x][cur.y] = 3
                    if (route.is_empty()):
                        print("no path")
                        break
                    cur.x, cur.y = route.pop()

        return route

    def select_shortest_route(self, campus_code, startX, startY, destX, destY):
        routeN = stack()
        routeE = stack()
        routeS = stack()
        routeW = stack()
        selectRoute = stack()

        routeN = self.find_route(campus_code, startX, startY, destX, destY, 0)
        routeE = self.find_route(campus_code, startX, startY, destX, destY, 1)
        routeS = self.find_route(campus_code, startX, startY, destX, destY, 2)
        routeW = self.find_route(campus_code, startX, startY, destX, destY, 3)

        selectRoute = routeN
        if (selectRoute.size > routeE.size):
            selectRoute = routeE
        if (selectRoute.size > routeS.size):
            selectRoute = routeS
        if (selectRoute.size > routeW.size):
            selectRoute = routeW

        return selectRoute

    def movable(self, campus_code, curX, curY, direct):
        result = 0
        global myeong
        global yul
        if campus_code == 1:
            if direct == 0:  # 북
                if (curX == 0):
                    result = 0
                elif myeong[curX - 1][curY] == 1:
                    result = 1
            elif direct == 1:  # 동
                if (curY == 17):
                    result = 0
                elif myeong[curX][curY + 1] == 1:
                    result = 1
            elif direct == 2:  # 남
                if (curX == 29):
                    result = 0
                elif myeong[curX + 1][curY] == 1:
                    result = 1
            elif direct == 3:  # 서
                if (curY == 0):
                    result = 0
                elif myeong[curX][curY - 1] == 1:
                    result = 1

        if campus_code == 2:
            if direct == 0:  # 북
                if (curX == 0):
                    result = 0
                elif yul[curX - 1][curY] == 1:
                    result = 1
            elif direct == 1:  # 동
                if (curY == 23):
                    result = 0
                elif yul[curX][curY + 1] == 1:
                    result = 1
            elif direct == 2:  # 남
                if (curX == 26):
                    result = 0
                elif yul[curX + 1][curY] == 1:
                    result = 1
            elif direct == 3:  # 서
                if (curY == 0):
                    result = 0
                elif yul[curX][curY - 1] == 1:
                    result = 1

        return result

    def move_to(self, cur, direct):
        offset = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        new_node = node(cur.x + offset[direct][0], cur.y + offset[direct][1])
        return new_node

    def get_estimate_time(self, campus_code, count):
        second = 0
        if campus_code == 1:
            second = count * 15
        if campus_code == 2:
            second = count * 30
        minute, second = divmod(second, 60)
        hour, minute = divmod(minute, 60)

        if hour == 0:
            self.show_time(minute, second)
        else:
            self.show_time_hour(hour, minute, second)

    def show_time(self, minute, second):
        QMessageBox.about(None, "SKKU GPS Navigation System", "Anticipated Time for Travel is %dmin(s) %dsec(s)." % (minute, second))

    def show_time_hour(self, hour, minute, second):
        QMessageBox.about(None, "SKKU GPS Navigation System", "Anticipated Time for Travel is %dhour(s) %dmin(s) %dsec(s)." % (hour, minute, second))

    def show_start_point(self):
        global user_loc
        count = user_loc.count()
        for i in range(count):
            locX, locY = user_loc.pop()
            i = QtWidgets.QLabel()
            i.setText("")
            i.setPixmap(QtGui.QPixmap("경로 표시.jpg"))
            self.gridLayout.addWidget(i, locX, locY)
        if startC == destC or (startC == 2 and destC == 1):
            dest_label = QtWidgets.QLabel()
            dest_label.setText("")
            dest_label.setPixmap(QtGui.QPixmap("경로 표시.jpg"))
            self.gridLayout.addWidget(dest_label, destX, destY)

    def setupUi(self, Dialog):
        self.find_way(startX, startY, destX, destY, startC, destC)
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 360, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("명륜캠 지도.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 600, 31, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 660, 31, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 630, 31, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 630, 31, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 660, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, -1, 362, 602))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_34 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 12, 17, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 9, 17, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 29, 10, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 29, 13, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_48.setText("")
        self.label_48.setObjectName("label_48")
        self.gridLayout.addWidget(self.label_48, 27, 17, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_44.setText("")
        self.label_44.setObjectName("label_44")
        self.gridLayout.addWidget(self.label_44, 22, 17, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 29, 9, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 6, 17, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_49.setText("")
        self.label_49.setObjectName("label_49")
        self.gridLayout.addWidget(self.label_49, 28, 17, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 0, 17, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 29, 12, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 29, 5, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_46.setText("")
        self.label_46.setObjectName("label_46")
        self.gridLayout.addWidget(self.label_46, 24, 17, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 29, 14, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 4, 17, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_47.setText("")
        self.label_47.setObjectName("label_47")
        self.gridLayout.addWidget(self.label_47, 26, 17, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 29, 8, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 29, 7, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_41.setText("")
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 19, 17, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 29, 3, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.gridLayout.addWidget(self.label_43, 21, 17, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 29, 11, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 29, 2, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 11, 17, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 3, 17, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 5, 17, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 25, 17, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 14, 17, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 13, 17, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 8, 17, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 29, 16, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_39.setText("")
        self.label_39.setObjectName("label_39")
        self.gridLayout.addWidget(self.label_39, 17, 17, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 10, 17, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 29, 4, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 2, 17, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 16, 17, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.gridLayout.addWidget(self.label_42, 20, 17, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.gridLayout.addWidget(self.label_45, 23, 17, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_37.setText("")
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 15, 17, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 29, 15, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 29, 6, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 29, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_40.setText("")
        self.label_40.setObjectName("label_40")
        self.gridLayout.addWidget(self.label_40, 18, 17, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 29, 17, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 1, 17, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 7, 17, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 29, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 600, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 630, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.hide)
        self.pushButton_2.clicked.connect(self.finish)
        self.pushButton_2.clicked.connect(init_Map)
        self.pushButton_6.clicked.connect(self.show_start_point)
        self.pushButton_7.clicked.connect(self.print_shuttle_bus_table)
        self.pushButton_7.clicked.connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.pushButton.setText(_translate("Dialog", "▲"))
        self.pushButton_3.setText(_translate("Dialog", "▼"))
        self.pushButton_4.setText(_translate("Dialog", "▶"))
        self.pushButton_5.setText(_translate("Dialog", "◀"))
        self.pushButton_2.setText(_translate("Dialog", "End"))
        self.pushButton_6.setText(_translate("Dialog", "Show Path"))
        self.pushButton_7.setText(_translate("Dialog", "Shuttle"))


class y_move(object):
    def suttle_timetable(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = campus_move()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()


    def finish(self):
        Dialog.show()

    def move_loc_up(self, campus_code, user_location):
        nowX, nowY = user_location.peek()
        is_move = 1
        if (nowX == 0):
            nowX += 1
            is_move = 0
        nowX = -1

        user_location.push(nowX, nowY)

    def move_loc_down(self, campus_code, user_location):
        nowX, nowY = user_location.peek()
        is_move = 1
        if ((campus_code == 1 and nowX == 29) or (campus_code == 2 and nowX == 26)):
            nowX -= 1
            is_move = 0
        nowX += 1

        user_location.push(nowX, nowY)

    def move_loc_left(self, campus_code, user_location):
        nowX, nowY = user_location.peek()
        is_move = 1
        if (nowY == 0):
            nowY += 1
            is_move = 0
        nowY -= 1

        user_location.push(nowX, nowY)

    def move_loc_right(self, campus_code, user_location):
        nowX, nowY = user_location.peek()
        is_move = 1
        if ((campus_code == 1 and nowY == 17) or (campus_code == 2 and nowY == 23)):
            nowY -= 1
            is_move = 0
        nowY += 1

        user_location.push(nowX, nowY)

    def is_follow(self, route, user_location):
        global startX, startY, destX, destY, startC, destC
        destination = [destX, destY]
        if (route.peek() == user_location.peek()):
            route.pop()
            if (user_location.peek() == destination):
                print("목적지에 도착했습니다")
                print("안내를 종료합니다")
                return
            self.move_loc(route, user_location)
            self.is_follow(route, user_location)
        else:
            print("경로를 이탈했습니다")
            now_location = user_location.peek()
            user_location.claer()
            self.find_way(now_location[0], now_location[1], destX, destY, startC, destC)
            self.is_follow(route, user_location)

    def find_way(self, startX, startY, destX, destY, startC, destC):
        if (startC == destC):
            self.print_route(startC, startX, startY, destX, destY)
            print("finish")
        elif startC == 1 and destC == 2:
            self.print_route(destC, 16, 13, destX, destY)  ##
            print("finish")
        else:
            self.print_route(startC, startX, startY, 16, 13)
            print("finish")

    def print_shuttle_bus_table(self):
        if startC == destC:
            QMessageBox.about(None, "SKKU GPS Navigation System", "같은 캠퍼스 내 이동 중입니다.\n프로그램이 종료됩니다.")
        elif startC == 1 and destC == 2:
            QMessageBox.about(None, "SKKU GPS Navigation System", "이미 셔틀버스를 탑승하셨습니다.\n프로그램이 종료됩니다.")
        else:
            self.suttle_timetable()

    def print_maze(self, campus_code):
        if campus_code == 1:
            for i in range(30):
                for j in range(18):
                    if (myeong[i][j] == 1):
                        print("■", end='')
                    elif (myeong[i][j] == 2):
                        print("○", end='')
                    elif (myeong[i][j] == 3):
                        print("☆", end='')
                    elif (myeong[i][j] == 5):  # 선택된 최단 경로
                        print("♡", end='')
                    else:
                        print("□", end='')
                print(end='\n')
            print("\n\n")
        elif campus_code == 2:
            for i in range(27):
                for j in range(24):
                    if (yul[i][j] == 1):
                        print("■", end='')
                    elif (yul[i][j] == 2):
                        print("○", end='')
                    elif (yul[i][j] == 3):
                        print("☆", end='')
                    elif (yul[i][j] == 5):  # 선택된 최단 경로
                        print("♡", end='')
                    else:
                        print("□", end='')
                print(end='\n')
            print("\n\n")

    def print_route(self, campus_code, startX, startY, destX, destY):
        global user_loc
        user_loc = stack()
        route = self.select_shortest_route(campus_code, startX, startY, destX, destY)
        count = route.size
        self.get_estimate_time(campus_code, count)
        ptr = stack()
        if campus_code == 1:
            while (route.size != 0):
                x, y = route.pop()
                myeong[x][y] = 5
                ptr.push(x, y)
        elif campus_code == 2:
            while (route.size != 0):
                x, y = route.pop()
                yul[x][y] = 5
                ptr.push(x, y)

        ptr.print()
        print("\n")

        for i in range(count):
            ptrX, ptrY = ptr.pop()
            user_loc.push(ptrX, ptrY)

        self.print_maze(campus_code)

    def find_route(self, campus_code, startX, startY, destX, destY, dir):
        init_Map()
        cur = node(startX, startY)
        route = stack()

        while True:
            if (campus_code == 1):
                myeong[cur.x][cur.y] = 2
                if (cur.x == destX and cur.y == destY):
                    # print("destination")
                    break
                forward = False
                count = 0
                direction = dir
                while (count < 4):
                    count += 1
                    if (direction == 4):
                        direction = 0
                    if (self.movable(campus_code, cur.x, cur.y, direction)):
                        route.push(cur.x, cur.y)
                        cur = self.move_to(cur, direction)
                        forward = True
                        break
                    direction += 1
                if (forward == False):
                    myeong[cur.x][cur.y] = 3
                    if (route.is_empty()):
                        print("no path")
                        break
                    cur.x, cur.y = route.pop()


            elif (campus_code == 2):
                yul[cur.x][cur.y] = 2
                if (cur.x == destX and cur.y == destY):
                    break
                forward = False
                count = 0
                direction = dir
                while (count < 4):
                    count += 1
                    if (direction == 4):
                        direction = 0
                    if (self.movable(campus_code, cur.x, cur.y, direction)):
                        route.push(cur.x, cur.y)
                        cur = self.move_to(cur, direction)
                        forward = True
                        break
                    direction += 1
                if (forward == False):
                    yul[cur.x][cur.y] = 3
                    if (route.is_empty()):
                        print("no path")
                        break
                    cur.x, cur.y = route.pop()

        return route

    def select_shortest_route(self, campus_code, startX, startY, destX, destY):
        routeN = stack()
        routeE = stack()
        routeS = stack()
        routeW = stack()
        selectRoute = stack()

        routeN = self.find_route(campus_code, startX, startY, destX, destY, 0)
        routeE = self.find_route(campus_code, startX, startY, destX, destY, 1)
        routeS = self.find_route(campus_code, startX, startY, destX, destY, 2)
        routeW = self.find_route(campus_code, startX, startY, destX, destY, 3)

        selectRoute = routeN
        if (selectRoute.size > routeE.size):
            selectRoute = routeE
        if (selectRoute.size > routeS.size):
            selectRoute = routeS
        if (selectRoute.size > routeW.size):
            selectRoute = routeW

        return selectRoute

    def movable(self, campus_code, curX, curY, direct):
        result = 0
        global myeong
        global yul
        if campus_code == 1:
            if direct == 0:  # 북
                if (curX == 0):
                    result = 0
                elif myeong[curX - 1][curY] == 1:
                    result = 1
            elif direct == 1:  # 동
                if (curY == 17):
                    result = 0
                elif myeong[curX][curY + 1] == 1:
                    result = 1
            elif direct == 2:  # 남
                if (curX == 29):
                    result = 0
                elif myeong[curX + 1][curY] == 1:
                    result = 1
            elif direct == 3:  # 서
                if (curY == 0):
                    result = 0
                elif myeong[curX][curY - 1] == 1:
                    result = 1

        if campus_code == 2:
            if direct == 0:  # 북
                if (curX == 0):
                    result = 0
                elif yul[curX - 1][curY] == 1:
                    result = 1
            elif direct == 1:  # 동
                if (curY == 23):
                    result = 0
                elif yul[curX][curY + 1] == 1:
                    result = 1
            elif direct == 2:  # 남
                if (curX == 26):
                    result = 0
                elif yul[curX + 1][curY] == 1:
                    result = 1
            elif direct == 3:  # 서
                if (curY == 0):
                    result = 0
                elif yul[curX][curY - 1] == 1:
                    result = 1

        return result

    def move_to(self, cur, direct):
        offset = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        new_node = node(cur.x + offset[direct][0], cur.y + offset[direct][1])
        return new_node

    def get_estimate_time(self, campus_code, count):
        second = 0
        if campus_code == 1:
            second = count * 15
        if campus_code == 2:
            second = count * 30
        minute, second = divmod(second, 60)
        hour, minute = divmod(minute, 60)

        if hour == 0:
            self.show_time(minute, second)
        else:
            self.show_time_hour(hour, minute, second)

    def show_time(self, minute, second):
        QMessageBox.about(None, "SKKU GPS Navigation System", "Anticipated Time for Travel is %dmin(s) %dsec(s)." % (minute, second))

    def show_time_hour(self, hour, minute, second):
        QMessageBox.about(None, "SKKU GPS Navigation System", "Anticipated Time for Travel is %dhour(s) %dmin(s) %dsec(s)." % (hour, minute, second))

    def show_start_point(self):
        global user_loc
        count = user_loc.count()
        for i in range(count):
            locX, locY = user_loc.pop()
            i = QtWidgets.QLabel()
            i.setText("")
            i.setPixmap(QtGui.QPixmap("경로 표시.jpg"))
            self.gridLayout.addWidget(i, locX, locY)
        if startC == destC or (startC == 1 and destC == 2):
            dest_label = QtWidgets.QLabel()
            dest_label.setText("")
            dest_label.setPixmap(QtGui.QPixmap("경로 표시.jpg"))
            self.gridLayout.addWidget(dest_label, destX, destY)

    def setupUi(self, Dialog):
        self.find_way(startX, startY, destX, destY, startC, destC)
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 540))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("율전캠 지도.jpg"))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 600, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 600, 31, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 570, 31, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 540, 31, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 570, 31, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 481, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 26, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 26, 21, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_53.setText("")
        self.label_53.setObjectName("label_53")
        self.gridLayout.addWidget(self.label_53, 25, 23, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 0, 23, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 6, 23, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 26, 12, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_48.setText("")
        self.label_48.setObjectName("label_48")
        self.gridLayout.addWidget(self.label_48, 21, 23, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_44.setText("")
        self.label_44.setObjectName("label_44")
        self.gridLayout.addWidget(self.label_44, 17, 23, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 1, 23, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_47.setText("")
        self.label_47.setObjectName("label_47")
        self.gridLayout.addWidget(self.label_47, 20, 23, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_46.setText("")
        self.label_46.setObjectName("label_46")
        self.gridLayout.addWidget(self.label_46, 19, 23, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 26, 7, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.gridLayout.addWidget(self.label_43, 16, 23, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 4, 23, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 26, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 26, 6, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 5, 23, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 26, 9, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_42.setText("")
        self.label_42.setObjectName("label_42")
        self.gridLayout.addWidget(self.label_42, 15, 23, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 26, 22, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.gridLayout.addWidget(self.label_45, 18, 23, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 2, 23, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_37.setText("")
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 10, 23, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 26, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 26, 10, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 26, 19, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_41.setText("")
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 14, 23, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 8, 23, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 26, 20, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_39.setText("")
        self.label_39.setObjectName("label_39")
        self.gridLayout.addWidget(self.label_39, 12, 23, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 11, 23, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 26, 17, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_51.setText("")
        self.label_51.setObjectName("label_51")
        self.gridLayout.addWidget(self.label_51, 24, 23, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 9, 23, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 26, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 26, 15, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_50.setText("")
        self.label_50.setObjectName("label_50")
        self.gridLayout.addWidget(self.label_50, 23, 23, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 26, 13, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 26, 16, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_40.setText("")
        self.label_40.setObjectName("label_40")
        self.gridLayout.addWidget(self.label_40, 13, 23, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_49.setText("")
        self.label_49.setObjectName("label_49")
        self.gridLayout.addWidget(self.label_49, 22, 23, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 26, 23, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 3, 23, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 26, 14, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 26, 4, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 26, 8, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 26, 11, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 7, 23, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 26, 18, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 26, 2, 1, 1)
        self.label_52 = QtWidgets.QLabel(Dialog)
        self.label_52.setGeometry(QtCore.QRect(430, 580, 20, 21))
        self.label_52.setText("")
        self.label_52.setObjectName("label_52")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(300, 540, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(300, 570, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.hide)
        self.pushButton_2.clicked.connect(self.finish)
        self.pushButton_2.clicked.connect(init_Map)
        self.pushButton_6.clicked.connect(self.show_start_point)
        self.pushButton_7.clicked.connect(self.print_shuttle_bus_table)
        self.pushButton_7.clicked.connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.pushButton_2.setText(_translate("Dialog", "End"))
        self.pushButton_3.setText(_translate("Dialog", "▼"))
        self.pushButton_4.setText(_translate("Dialog", "▶"))
        self.pushButton.setText(_translate("Dialog", "▲"))
        self.pushButton_5.setText(_translate("Dialog", "◀"))
        self.pushButton_6.setText(_translate("Dialog", "Show Path"))
        self.pushButton_7.setText(_translate("Dialog", "Shuttle"))

class campus_move(object):
    def suttle_move(self):
        if (startC == 2 and destC == 1):
            self.window = QtWidgets.QMainWindow()
            self.ui = m_move()
            self.ui.setupUi(self.window)
            Dialog.hide()
            self.window.show()

        elif (startC == 1 and destC == 2):
            self.window = QtWidgets.QMainWindow()
            self.ui = y_move()
            self.ui.setupUi(self.window)
            Dialog.hide()
            self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 370)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 360, 347))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("셔틀 버스 시간표.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 330, 101, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.suttle_move)
        self.pushButton.clicked.connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Naviagation System"))
        self.pushButton.setText(_translate("Dialog", "캠퍼스 이동"))


class Ui_Dialog(object):
    def print_myeongyrun(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = map_myeongryun()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def print_yuljeon(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = map_yuljeon()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(960, 694)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("symbolmark_vPe_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 960, 694))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("유생 길라잡이.jpg"))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 620, 961, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(100, 0, 100, 0)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.print_myeongyrun)
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.print_yuljeon)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SKKU GPS Navigation System"))
        self.pushButton_3.setText(_translate("Dialog", "Hyehwa Campus"))
        self.pushButton_2.setText(_translate("Dialog", "Suwon Campus"))
        self.pushButton.setText(_translate("Dialog", "Exit"))


if __name__ == "__main__":
    import sys

    init_Map()
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
