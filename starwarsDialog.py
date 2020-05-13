# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'starwarsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(650, 700))
        Dialog.setMaximumSize(QtCore.QSize(650, 700))
        Dialog.setStyleSheet("QDialog {\n"
"background-color: rgb(8, 8, 8);\n"
"}\n"
" QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    border: 1px solid grey;\n"
"}\n"
"\n"
"QPushButton {\n"
"  padding: 15px 25px;\n"
"  font-size: 14px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  outline: none;\n"
"  color: #fff;\n"
"  background-color: rgb(143, 0, 24);\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(191, 24, 39);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(191, 24, 39);\n"
"}")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 608, 640, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(640, 80))
        self.frame.setMaximumSize(QtCore.QSize(640, 16777215))
        self.frame.setSizeIncrement(QtCore.QSize(0, 1))
        self.frame.setBaseSize(QtCore.QSize(0, 1))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMaximumSize(QtCore.QSize(250, 1000))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 0, 2, 2, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_2.setStyleSheet("QLabel {\n"
"   border: None;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMaximumSize(QtCore.QSize(250, 1000))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 0, 0, 2, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label.setStyleSheet("QLabel {\n"
"   border: None;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 1, 1, 1)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 631, 110))
        self.widget.setObjectName("widget")
        # self.gridLayoutLP = QtWidgets.QGridLayout(self.widget)
        # self.gridLayoutLP.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        # self.gridLayoutLP.setContentsMargins(0, 0, 0, 0)
        # self.gridLayoutLP.setObjectName("gridLayoutLP")
        # self.label_3 = QtWidgets.QLabel(self.widget)
        # self.label_3.setObjectName("label_3")
        # self.gridLayoutLP.addWidget(self.label_3, 0, 0, 1, 1)
        # self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.gridLayoutLP.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "Next >>"))
        self.label_2.setText(_translate("Dialog", "Total per page"))
        self.pushButton.setText(_translate("Dialog", "<< Previous"))
        self.label.setText(_translate("Dialog", "0"))
        # self.label_3.setText(_translate("Dialog", "TextLabel"))
        # self.pushButton_3.setText(_translate("Dialog", "PushButton"))




# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
