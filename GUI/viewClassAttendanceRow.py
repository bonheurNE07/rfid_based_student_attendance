# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewClassattendanceRow.ui'
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

class Ui_ClassAttendanceRow(object):
    def setupUi(self, ClassAttendanceRow):
        if not ClassAttendanceRow.objectName():
            ClassAttendanceRow.setObjectName(u"ClassAttendanceRow")
        ClassAttendanceRow.resize(1121, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ClassAttendanceRow.sizePolicy().hasHeightForWidth())
        ClassAttendanceRow.setSizePolicy(sizePolicy)
        ClassAttendanceRow.setMinimumSize(QSize(0, 50))
        ClassAttendanceRow.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(ClassAttendanceRow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.class_attendance_id = QLabel(ClassAttendanceRow)
        self.class_attendance_id.setObjectName(u"class_attendance_id")

        self.horizontalLayout.addWidget(self.class_attendance_id)

        self.class_attendance_firstname = QLabel(ClassAttendanceRow)
        self.class_attendance_firstname.setObjectName(u"class_attendance_firstname")

        self.horizontalLayout.addWidget(self.class_attendance_firstname)

        self.class_attendance_lastname = QLabel(ClassAttendanceRow)
        self.class_attendance_lastname.setObjectName(u"class_attendance_lastname")

        self.horizontalLayout.addWidget(self.class_attendance_lastname)

        self.class_attendance_othername = QLabel(ClassAttendanceRow)
        self.class_attendance_othername.setObjectName(u"class_attendance_othername")

        self.horizontalLayout.addWidget(self.class_attendance_othername)

        self.class_attendance_rollnumber = QLabel(ClassAttendanceRow)
        self.class_attendance_rollnumber.setObjectName(u"class_attendance_rollnumber")

        self.horizontalLayout.addWidget(self.class_attendance_rollnumber)

        self.class_attendance_class = QLabel(ClassAttendanceRow)
        self.class_attendance_class.setObjectName(u"class_attendance_class")

        self.horizontalLayout.addWidget(self.class_attendance_class)

        self.class_attendance_course = QLabel(ClassAttendanceRow)
        self.class_attendance_course.setObjectName(u"class_attendance_course")

        self.horizontalLayout.addWidget(self.class_attendance_course)

        self.class_attendance_session = QLabel(ClassAttendanceRow)
        self.class_attendance_session.setObjectName(u"class_attendance_session")

        self.horizontalLayout.addWidget(self.class_attendance_session)

        self.class_attendance_term = QLabel(ClassAttendanceRow)
        self.class_attendance_term.setObjectName(u"class_attendance_term")

        self.horizontalLayout.addWidget(self.class_attendance_term)

        self.class_attendance_status = QLabel(ClassAttendanceRow)
        self.class_attendance_status.setObjectName(u"class_attendance_status")

        self.horizontalLayout.addWidget(self.class_attendance_status)

        self.class_attendance_date = QLabel(ClassAttendanceRow)
        self.class_attendance_date.setObjectName(u"class_attendance_date")

        self.horizontalLayout.addWidget(self.class_attendance_date)


        self.retranslateUi(ClassAttendanceRow)

        QMetaObject.connectSlotsByName(ClassAttendanceRow)
    # setupUi

    def retranslateUi(self, ClassAttendanceRow):
        ClassAttendanceRow.setWindowTitle("")
        self.class_attendance_id.setText(QCoreApplication.translate("ClassAttendanceRow", u"{N/O}", None))
        self.class_attendance_firstname.setText(QCoreApplication.translate("ClassAttendanceRow", u"{N/O}", None))
        self.class_attendance_lastname.setText(QCoreApplication.translate("ClassAttendanceRow", u"{N/O}", None))
        self.class_attendance_othername.setText(QCoreApplication.translate("ClassAttendanceRow", u"{N/O}", None))
        self.class_attendance_rollnumber.setText(QCoreApplication.translate("ClassAttendanceRow", u"{N/O}", None))
        self.class_attendance_class.setText(QCoreApplication.translate("ClassAttendanceRow", u"{N/O}", None))
        self.class_attendance_course.setText(QCoreApplication.translate("ClassAttendanceRow", u"{N/O}", None))
        self.class_attendance_session.setText(QCoreApplication.translate("ClassAttendanceRow", u"{N/O}", None))
        self.class_attendance_term.setText(QCoreApplication.translate("ClassAttendanceRow", u"{N/O}", None))
        self.class_attendance_status.setText(QCoreApplication.translate("ClassAttendanceRow", u"{N/O}", None))
        self.class_attendance_date.setText(QCoreApplication.translate("ClassAttendanceRow", u"{N/O}", None))
    # retranslateUi

