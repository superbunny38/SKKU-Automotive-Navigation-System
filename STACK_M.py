# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'STACK_M.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from STACK_M_start import m_input_start_point


class map_myeongryun(object):
    def start_point(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = m_input_start_point()
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
        self.pushButton.clicked.connect(self.start_point)
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "유생 길라잡이"))
        self.pushButton.setText(_translate("Dialog", "시작 위치"))
        self.pushButton_2.setText(_translate("Dialog", "도착 위치"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = map_myeongryun()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
