# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createClassRowWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)
from .Resources import images
from .Resources.icons.grey import grey
from .Resources.icons.skyblue import skyblue
from .Resources.icons.wiht import wiht

class Ui_createClasseTableRowWidget(object):
    def setupUi(self, createClasseTableRowWidget):
        if not createClasseTableRowWidget.objectName():
            createClasseTableRowWidget.setObjectName(u"createClasseTableRowWidget")
        createClasseTableRowWidget.resize(370, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(createClasseTableRowWidget.sizePolicy().hasHeightForWidth())
        createClasseTableRowWidget.setSizePolicy(sizePolicy)
        createClasseTableRowWidget.setMinimumSize(QSize(0, 50))
        createClasseTableRowWidget.setMaximumSize(QSize(16777215, 50))
        self.gridLayout = QGridLayout(createClasseTableRowWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.editButton = QPushButton(createClasseTableRowWidget)
        self.editButton.setObjectName(u"editButton")
        icon = QIcon()
        icon.addFile(u":/skyblue_icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editButton.setIcon(icon)

        self.gridLayout.addWidget(self.editButton, 0, 2, 1, 1)

        self.classNameLabel = QLabel(createClasseTableRowWidget)
        self.classNameLabel.setObjectName(u"classNameLabel")

        self.gridLayout.addWidget(self.classNameLabel, 0, 1, 1, 1)

        self.classNumberLabel = QLabel(createClasseTableRowWidget)
        self.classNumberLabel.setObjectName(u"classNumberLabel")

        self.gridLayout.addWidget(self.classNumberLabel, 0, 0, 1, 1)

        self.deleteButton = QPushButton(createClasseTableRowWidget)
        self.deleteButton.setObjectName(u"deleteButton")
        icon1 = QIcon()
        icon1.addFile(u":/skyblue_icons/trash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteButton.setIcon(icon1)

        self.gridLayout.addWidget(self.deleteButton, 0, 3, 1, 1)


        self.retranslateUi(createClasseTableRowWidget)

        QMetaObject.connectSlotsByName(createClasseTableRowWidget)
    # setupUi

    def retranslateUi(self, createClasseTableRowWidget):
        createClasseTableRowWidget.setWindowTitle("")
        self.editButton.setText(QCoreApplication.translate("createClasseTableRowWidget", u"Edit", None))
        self.classNameLabel.setText(QCoreApplication.translate("createClasseTableRowWidget", u"N/O", None))
        self.classNumberLabel.setText(QCoreApplication.translate("createClasseTableRowWidget", u"N/O", None))
        self.deleteButton.setText(QCoreApplication.translate("createClasseTableRowWidget", u"Delete", None))
    # retranslateUi

