# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'classCourseTableRow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)
from .Resources.icons.skyblue import skyblue

class Ui_ClassCourseTableRow(object):
    def setupUi(self, ClassCourseTableRow):
        if not ClassCourseTableRow.objectName():
            ClassCourseTableRow.setObjectName(u"ClassCourseTableRow")
        ClassCourseTableRow.resize(338, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ClassCourseTableRow.sizePolicy().hasHeightForWidth())
        ClassCourseTableRow.setSizePolicy(sizePolicy)
        ClassCourseTableRow.setMinimumSize(QSize(0, 50))
        ClassCourseTableRow.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(ClassCourseTableRow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.classNumberLabel = QLabel(ClassCourseTableRow)
        self.classNumberLabel.setObjectName(u"classNumberLabel")

        self.horizontalLayout.addWidget(self.classNumberLabel)

        self.classNameLabel = QLabel(ClassCourseTableRow)
        self.classNameLabel.setObjectName(u"classNameLabel")

        self.horizontalLayout.addWidget(self.classNameLabel)

        self.classCourselabel = QLabel(ClassCourseTableRow)
        self.classCourselabel.setObjectName(u"classCourselabel")

        self.horizontalLayout.addWidget(self.classCourselabel)

        self.classCoursestatus = QLabel(ClassCourseTableRow)
        self.classCoursestatus.setObjectName(u"classCoursestatus")

        self.horizontalLayout.addWidget(self.classCoursestatus)

        self.editButton = QPushButton(ClassCourseTableRow)
        self.editButton.setObjectName(u"editButton")
        icon = QIcon()
        icon.addFile(u":/skyblue_icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(ClassCourseTableRow)
        self.deleteButton.setObjectName(u"deleteButton")
        icon1 = QIcon()
        icon1.addFile(u":/skyblue_icons/trash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.deleteButton)


        self.retranslateUi(ClassCourseTableRow)

        QMetaObject.connectSlotsByName(ClassCourseTableRow)
    # setupUi

    def retranslateUi(self, ClassCourseTableRow):
        ClassCourseTableRow.setWindowTitle("")
        self.classNumberLabel.setText(QCoreApplication.translate("ClassCourseTableRow", u"N/O", None))
        self.classNameLabel.setText(QCoreApplication.translate("ClassCourseTableRow", u"N/O", None))
        self.classCourselabel.setText(QCoreApplication.translate("ClassCourseTableRow", u"N/O", None))
        self.classCoursestatus.setText(QCoreApplication.translate("ClassCourseTableRow", u"N/O", None))
        self.editButton.setText(QCoreApplication.translate("ClassCourseTableRow", u"Edit", None))
        self.deleteButton.setText(QCoreApplication.translate("ClassCourseTableRow", u"Delete", None))
    # retranslateUi

