# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewStudentattendanceRow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_StudentAttendanceRow(object):
    def setupUi(self, StudentAttendanceRow):
        if not StudentAttendanceRow.objectName():
            StudentAttendanceRow.setObjectName(u"StudentAttendanceRow")
        StudentAttendanceRow.resize(860, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StudentAttendanceRow.sizePolicy().hasHeightForWidth())
        StudentAttendanceRow.setSizePolicy(sizePolicy)
        StudentAttendanceRow.setMinimumSize(QSize(0, 50))
        StudentAttendanceRow.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(StudentAttendanceRow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.class_attendance_id = QLabel(StudentAttendanceRow)
        self.class_attendance_id.setObjectName(u"class_attendance_id")

        self.horizontalLayout.addWidget(self.class_attendance_id)

        self.class_attendance_firstname = QLabel(StudentAttendanceRow)
        self.class_attendance_firstname.setObjectName(u"class_attendance_firstname")

        self.horizontalLayout.addWidget(self.class_attendance_firstname)

        self.class_attendance_lastname = QLabel(StudentAttendanceRow)
        self.class_attendance_lastname.setObjectName(u"class_attendance_lastname")

        self.horizontalLayout.addWidget(self.class_attendance_lastname)

        self.class_attendance_othername = QLabel(StudentAttendanceRow)
        self.class_attendance_othername.setObjectName(u"class_attendance_othername")

        self.horizontalLayout.addWidget(self.class_attendance_othername)

        self.class_attendance_rollnumber = QLabel(StudentAttendanceRow)
        self.class_attendance_rollnumber.setObjectName(u"class_attendance_rollnumber")

        self.horizontalLayout.addWidget(self.class_attendance_rollnumber)

        self.class_attendance_class = QLabel(StudentAttendanceRow)
        self.class_attendance_class.setObjectName(u"class_attendance_class")

        self.horizontalLayout.addWidget(self.class_attendance_class)

        self.class_attendance_course = QLabel(StudentAttendanceRow)
        self.class_attendance_course.setObjectName(u"class_attendance_course")

        self.horizontalLayout.addWidget(self.class_attendance_course)

        self.class_attendance_session = QLabel(StudentAttendanceRow)
        self.class_attendance_session.setObjectName(u"class_attendance_session")

        self.horizontalLayout.addWidget(self.class_attendance_session)

        self.class_attendance_term = QLabel(StudentAttendanceRow)
        self.class_attendance_term.setObjectName(u"class_attendance_term")

        self.horizontalLayout.addWidget(self.class_attendance_term)

        self.class_attendance_status = QLabel(StudentAttendanceRow)
        self.class_attendance_status.setObjectName(u"class_attendance_status")

        self.horizontalLayout.addWidget(self.class_attendance_status)

        self.class_attendance_date = QLabel(StudentAttendanceRow)
        self.class_attendance_date.setObjectName(u"class_attendance_date")

        self.horizontalLayout.addWidget(self.class_attendance_date)


        self.retranslateUi(StudentAttendanceRow)

        QMetaObject.connectSlotsByName(StudentAttendanceRow)
    # setupUi

    def retranslateUi(self, StudentAttendanceRow):
        StudentAttendanceRow.setWindowTitle(QCoreApplication.translate("StudentAttendanceRow", u"Form", None))
        self.class_attendance_id.setText(QCoreApplication.translate("StudentAttendanceRow", u"{N/O}", None))
        self.class_attendance_firstname.setText(QCoreApplication.translate("StudentAttendanceRow", u"{N/O}", None))
        self.class_attendance_lastname.setText(QCoreApplication.translate("StudentAttendanceRow", u"{N/O}", None))
        self.class_attendance_othername.setText(QCoreApplication.translate("StudentAttendanceRow", u"{N/O}", None))
        self.class_attendance_rollnumber.setText(QCoreApplication.translate("StudentAttendanceRow", u"{N/O}", None))
        self.class_attendance_class.setText(QCoreApplication.translate("StudentAttendanceRow", u"{N/O}", None))
        self.class_attendance_course.setText(QCoreApplication.translate("StudentAttendanceRow", u"{N/O}", None))
        self.class_attendance_session.setText(QCoreApplication.translate("StudentAttendanceRow", u"{N/O}", None))
        self.class_attendance_term.setText(QCoreApplication.translate("StudentAttendanceRow", u"{N/O}", None))
        self.class_attendance_status.setText(QCoreApplication.translate("StudentAttendanceRow", u"{N/O}", None))
        self.class_attendance_date.setText(QCoreApplication.translate("StudentAttendanceRow", u"{N/O}", None))
    # retranslateUi

