# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginWin.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
from .Resources.icons.black import black
from .Resources import images
from .Resources.icons.grey import grey
from .Resources.icons.skyblue import skyblue
from .Resources.icons.wiht import wiht

class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        if not LoginWidget.objectName():
            LoginWidget.setObjectName(u"LoginWidget")
        LoginWidget.resize(363, 410)
        LoginWidget.setStyleSheet(u"QWidget {\n"
"    background-color: rgba(30, 30, 30, 0.9); /* Dark background with 80% opacity */\n"
"	\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(LoginWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.HeaderFrame = QFrame(LoginWidget)
        self.HeaderFrame.setObjectName(u"HeaderFrame")
        self.HeaderFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.HeaderFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.HeaderFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.login_label = QLabel(self.HeaderFrame)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setPixmap(QPixmap(u":/images/LOGIN.png"))

        self.verticalLayout_2.addWidget(self.login_label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_2 = QLabel(self.HeaderFrame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.HeaderFrame)

        self.MainFrame = QFrame(LoginWidget)
        self.MainFrame.setObjectName(u"MainFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainFrame.sizePolicy().hasHeightForWidth())
        self.MainFrame.setSizePolicy(sizePolicy)
        self.MainFrame.setStyleSheet(u"QComboBox#userRoleComboBox {\n"
"	color: rgb(0, 0, 0);\n"
"    /* Set background color */\n"
"    background-color: rgb(255, 255, 255); \n"
"    /* Set border style */\n"
"	border:1px solid;\n"
"     border-color: rgb(61, 61, 61);  ;\n"
"    border-radius: 1px;\n"
"    /* Set padding */\n"
"\n"
"    padding: 5px;\n"
"    /* Set text alignment */\n"
"    text-align: center;\n"
"	font-size: 14px;\n"
"    font-family: \"Times New Roman\", serif; \n"
"  \n"
"    /* Set dropdown button style */\n"
"    QComboBox::drop-down {\n"
"        width: 20px;\n"
"        height: 20px;\n"
"        border: none;\n"
"        background-color: rgb(255, 255, 255); \n"
"    }\n"
"    /* Set item height */\n"
"    QComboBox::item {\n"
"        height: 25px;\n"
"    }\n"
"    /* Set hover and selection colors */\n"
"    QComboBox::item:hover {\n"
"         background-color: rgb(255, 255, 255); \n"
"    }\n"
"    QComboBox::item:selected {\n"
"         background-color: rgb(255, 255, 255); \n"
"    }\n"
"}\n"
"\n"
"QLineEdit {\n"
"	c"
                        "olor: rgb(255, 255, 255);\n"
"    border-style: none;\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width: 1px;\n"
"    border-color: rgb(61, 61, 61); /* Adjust the color as needed */\n"
"    background-color: transparent;\n"
"	font-size: 14px;\n"
"    font-family: \"Times New Roman\", serif; \n"
"}\n"
"")
        self.MainFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.MainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.MainFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(6)
        self.email_lineEdit = QLineEdit(self.MainFrame)
        self.email_lineEdit.setObjectName(u"email_lineEdit")

        self.gridLayout.addWidget(self.email_lineEdit, 3, 4, 1, 1)

        self.label_4 = QLabel(self.MainFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/grey_icons/lock.svg"))

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)

        self.passwrod_lineEdit = QLineEdit(self.MainFrame)
        self.passwrod_lineEdit.setObjectName(u"passwrod_lineEdit")
        self.passwrod_lineEdit.setMaxLength(12)
        self.passwrod_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.passwrod_lineEdit, 2, 4, 1, 1)

        self.label_5 = QLabel(self.MainFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/grey_icons/mail.svg"))

        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)

        self.Username_lineEdit = QLineEdit(self.MainFrame)
        self.Username_lineEdit.setObjectName(u"Username_lineEdit")

        self.gridLayout.addWidget(self.Username_lineEdit, 1, 4, 1, 1)

        self.label_3 = QLabel(self.MainFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/grey_icons/user.svg"))

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)

        self.userRoleComboBox = QComboBox(self.MainFrame)
        self.userRoleComboBox.addItem("")
        self.userRoleComboBox.addItem("")
        self.userRoleComboBox.addItem("")
        self.userRoleComboBox.setObjectName(u"userRoleComboBox")
        self.userRoleComboBox.setStyleSheet(u" background-color: rgb(255, 255, 255); ")

        self.gridLayout.addWidget(self.userRoleComboBox, 0, 4, 1, 1)


        self.verticalLayout.addWidget(self.MainFrame)

        self.BottomFrame = QFrame(LoginWidget)
        self.BottomFrame.setObjectName(u"BottomFrame")
        self.BottomFrame.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #4CAF50; /* Green border */\n"
"    color: #ffffff; /* White text color */\n"
"    background-color: #4CAF50; /* Green background */\n"
"    padding: 10px 20px; /* Padding around text */\n"
"    font-size: 16px; /* Font size */\n"
"    font-weight: bold; /* Bold text */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* Darker green on hover */\n"
"    border-color: #45a049; /* Darker green border on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3e8e41; /* Dark green when pressed */\n"
"    border-color: #3e8e41; /* Dark green border when pressed */\n"
"}\n"
"")
        self.BottomFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.BottomFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.BottomFrame)
        self.verticalLayout_3.setSpacing(18)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.login_pushButton = QPushButton(self.BottomFrame)
        self.login_pushButton.setObjectName(u"login_pushButton")
        icon = QIcon()
        icon.addFile(u":/black_icons/log-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.login_pushButton.setIcon(icon)

        self.verticalLayout_3.addWidget(self.login_pushButton)

        self.label = QLabel(self.BottomFrame)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.BottomFrame)

        QWidget.setTabOrder(self.userRoleComboBox, self.Username_lineEdit)
        QWidget.setTabOrder(self.Username_lineEdit, self.passwrod_lineEdit)
        QWidget.setTabOrder(self.passwrod_lineEdit, self.email_lineEdit)
        QWidget.setTabOrder(self.email_lineEdit, self.login_pushButton)

        self.retranslateUi(LoginWidget)

        QMetaObject.connectSlotsByName(LoginWidget)
    # setupUi

    def retranslateUi(self, LoginWidget):
        LoginWidget.setWindowTitle(QCoreApplication.translate("LoginWidget", u"Login Window", None))
        self.login_label.setText("")
        self.label_2.setText(QCoreApplication.translate("LoginWidget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#636363;\">LOGIN TO </span><span style=\" font-size:16pt; color:#3a3a3a;\">YOUR ACCOUNT</span></p></body></html>", None))
        self.email_lineEdit.setInputMask("")
        self.email_lineEdit.setPlaceholderText(QCoreApplication.translate("LoginWidget", u"Enter your email address", None))
        self.label_4.setText("")
        self.passwrod_lineEdit.setInputMask("")
        self.passwrod_lineEdit.setPlaceholderText(QCoreApplication.translate("LoginWidget", u"Enter your password", None))
        self.label_5.setText("")
        self.Username_lineEdit.setPlaceholderText(QCoreApplication.translate("LoginWidget", u"Enter your username", None))
        self.label_3.setText("")
        self.userRoleComboBox.setItemText(0, QCoreApplication.translate("LoginWidget", u"Administrator", None))
        self.userRoleComboBox.setItemText(1, QCoreApplication.translate("LoginWidget", u"Class Teacher", None))
        self.userRoleComboBox.setItemText(2, QCoreApplication.translate("LoginWidget", u"Security", None))

        self.userRoleComboBox.setPlaceholderText(QCoreApplication.translate("LoginWidget", u"-- Select User Rroles --", None))
        self.login_pushButton.setText(QCoreApplication.translate("LoginWidget", u"Login", None))
        self.label.setText(QCoreApplication.translate("LoginWidget", u"<html><head/><body><p><span style=\" font-weight:700; color:#aaaaaa;\">\u00a9 2024 Ndeze Bonheur.</span><span style=\" color:#9e9e9e;\"> All rights reserved.</span></p></body></html>", None))
    # retranslateUi

