# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StudentTableRowWidget.ui'
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

class Ui_ViewstudentRowWidget(object):
    def setupUi(self, ViewstudentRowWidget):
        if not ViewstudentRowWidget.objectName():
            ViewstudentRowWidget.setObjectName(u"ViewstudentRowWidget")
        ViewstudentRowWidget.resize(879, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ViewstudentRowWidget.sizePolicy().hasHeightForWidth())
        ViewstudentRowWidget.setSizePolicy(sizePolicy)
        ViewstudentRowWidget.setMinimumSize(QSize(0, 50))
        ViewstudentRowWidget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(ViewstudentRowWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.student_id_label = QLabel(ViewstudentRowWidget)
        self.student_id_label.setObjectName(u"student_id_label")

        self.horizontalLayout.addWidget(self.student_id_label)

        self.student_firstname_lbl = QLabel(ViewstudentRowWidget)
        self.student_firstname_lbl.setObjectName(u"student_firstname_lbl")

        self.horizontalLayout.addWidget(self.student_firstname_lbl)

        self.student_lastname_lbl = QLabel(ViewstudentRowWidget)
        self.student_lastname_lbl.setObjectName(u"student_lastname_lbl")

        self.horizontalLayout.addWidget(self.student_lastname_lbl)

        self.student_othername_lbl = QLabel(ViewstudentRowWidget)
        self.student_othername_lbl.setObjectName(u"student_othername_lbl")

        self.horizontalLayout.addWidget(self.student_othername_lbl)

        self.student_addminsion_nbr_lbl = QLabel(ViewstudentRowWidget)
        self.student_addminsion_nbr_lbl.setObjectName(u"student_addminsion_nbr_lbl")

        self.horizontalLayout.addWidget(self.student_addminsion_nbr_lbl)

        self.student_class_lbl = QLabel(ViewstudentRowWidget)
        self.student_class_lbl.setObjectName(u"student_class_lbl")

        self.horizontalLayout.addWidget(self.student_class_lbl)

        self.student_course_lbl = QLabel(ViewstudentRowWidget)
        self.student_course_lbl.setObjectName(u"student_course_lbl")

        self.horizontalLayout.addWidget(self.student_course_lbl)

        self.student_date_created_lbl = QLabel(ViewstudentRowWidget)
        self.student_date_created_lbl.setObjectName(u"student_date_created_lbl")

        self.horizontalLayout.addWidget(self.student_date_created_lbl)

        self.edit_student_button = QPushButton(ViewstudentRowWidget)
        self.edit_student_button.setObjectName(u"edit_student_button")
        self.edit_student_button.setStyleSheet(u"border:none;\n"
"background-color:none;")
        icon = QIcon()
        icon.addFile(u":/skyblue_icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_student_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.edit_student_button)

        self.delete_student_button = QPushButton(ViewstudentRowWidget)
        self.delete_student_button.setObjectName(u"delete_student_button")
        self.delete_student_button.setStyleSheet(u"border:none;\n"
"bckground-color:none;")
        icon1 = QIcon()
        icon1.addFile(u":/skyblue_icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_student_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.delete_student_button)


        self.retranslateUi(ViewstudentRowWidget)

        QMetaObject.connectSlotsByName(ViewstudentRowWidget)
    # setupUi

    def retranslateUi(self, ViewstudentRowWidget):
        ViewstudentRowWidget.setWindowTitle(QCoreApplication.translate("ViewstudentRowWidget", u"Form", None))
        self.student_id_label.setText(QCoreApplication.translate("ViewstudentRowWidget", u"N/O", None))
        self.student_firstname_lbl.setText(QCoreApplication.translate("ViewstudentRowWidget", u"N/O", None))
        self.student_lastname_lbl.setText(QCoreApplication.translate("ViewstudentRowWidget", u"N/O", None))
        self.student_othername_lbl.setText(QCoreApplication.translate("ViewstudentRowWidget", u"N/O", None))
        self.student_addminsion_nbr_lbl.setText(QCoreApplication.translate("ViewstudentRowWidget", u"N/O", None))
        self.student_class_lbl.setText(QCoreApplication.translate("ViewstudentRowWidget", u"N/O", None))
        self.student_course_lbl.setText(QCoreApplication.translate("ViewstudentRowWidget", u"N/O", None))
        self.student_date_created_lbl.setText(QCoreApplication.translate("ViewstudentRowWidget", u"N/O", None))
        self.edit_student_button.setText("")
        self.delete_student_button.setText("")
    # retranslateUi

