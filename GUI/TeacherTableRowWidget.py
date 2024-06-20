# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TeacherTableRowWidget.ui'
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

class Ui_TeachersTableRowWidget(object):
    def setupUi(self, TeachersTableRowWidget):
        if not TeachersTableRowWidget.objectName():
            TeachersTableRowWidget.setObjectName(u"TeachersTableRowWidget")
        TeachersTableRowWidget.resize(709, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TeachersTableRowWidget.sizePolicy().hasHeightForWidth())
        TeachersTableRowWidget.setSizePolicy(sizePolicy)
        TeachersTableRowWidget.setMinimumSize(QSize(0, 50))
        TeachersTableRowWidget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(TeachersTableRowWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.teacher_id = QLabel(TeachersTableRowWidget)
        self.teacher_id.setObjectName(u"teacher_id")

        self.horizontalLayout.addWidget(self.teacher_id)

        self.firstname_label = QLabel(TeachersTableRowWidget)
        self.firstname_label.setObjectName(u"firstname_label")

        self.horizontalLayout.addWidget(self.firstname_label)

        self.lastname_label = QLabel(TeachersTableRowWidget)
        self.lastname_label.setObjectName(u"lastname_label")

        self.horizontalLayout.addWidget(self.lastname_label)

        self.teachers_email_label = QLabel(TeachersTableRowWidget)
        self.teachers_email_label.setObjectName(u"teachers_email_label")

        self.horizontalLayout.addWidget(self.teachers_email_label)

        self.teacher_phonenumber_label = QLabel(TeachersTableRowWidget)
        self.teacher_phonenumber_label.setObjectName(u"teacher_phonenumber_label")

        self.horizontalLayout.addWidget(self.teacher_phonenumber_label)

        self.assigned_class_label = QLabel(TeachersTableRowWidget)
        self.assigned_class_label.setObjectName(u"assigned_class_label")

        self.horizontalLayout.addWidget(self.assigned_class_label)

        self.class_course_label = QLabel(TeachersTableRowWidget)
        self.class_course_label.setObjectName(u"class_course_label")

        self.horizontalLayout.addWidget(self.class_course_label)

        self.create_datelabel = QLabel(TeachersTableRowWidget)
        self.create_datelabel.setObjectName(u"create_datelabel")

        self.horizontalLayout.addWidget(self.create_datelabel)

        self.deleteTeacherpushButton = QPushButton(TeachersTableRowWidget)
        self.deleteTeacherpushButton.setObjectName(u"deleteTeacherpushButton")
        self.deleteTeacherpushButton.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/skyblue_icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteTeacherpushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.deleteTeacherpushButton)


        self.retranslateUi(TeachersTableRowWidget)

        QMetaObject.connectSlotsByName(TeachersTableRowWidget)
    # setupUi

    def retranslateUi(self, TeachersTableRowWidget):
        TeachersTableRowWidget.setWindowTitle("")
        self.teacher_id.setText(QCoreApplication.translate("TeachersTableRowWidget", u"N/O", None))
        self.firstname_label.setText(QCoreApplication.translate("TeachersTableRowWidget", u"N/O", None))
        self.lastname_label.setText(QCoreApplication.translate("TeachersTableRowWidget", u"N/O", None))
        self.teachers_email_label.setText(QCoreApplication.translate("TeachersTableRowWidget", u"N/O", None))
        self.teacher_phonenumber_label.setText(QCoreApplication.translate("TeachersTableRowWidget", u"N/O", None))
        self.assigned_class_label.setText(QCoreApplication.translate("TeachersTableRowWidget", u"N/O", None))
        self.class_course_label.setText(QCoreApplication.translate("TeachersTableRowWidget", u"N/O", None))
        self.create_datelabel.setText(QCoreApplication.translate("TeachersTableRowWidget", u"N/O", None))
        self.deleteTeacherpushButton.setText("")
    # retranslateUi

