# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sessionTermRowWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)
from .Resources.icons.skyblue import skyblue

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(928, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 50))
        Form.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.session_term_id_label = QLabel(Form)
        self.session_term_id_label.setObjectName(u"session_term_id_label")

        self.horizontalLayout.addWidget(self.session_term_id_label)

        self.session_term_session_label = QLabel(Form)
        self.session_term_session_label.setObjectName(u"session_term_session_label")

        self.horizontalLayout.addWidget(self.session_term_session_label)

        self.session_term_term_lbl = QLabel(Form)
        self.session_term_term_lbl.setObjectName(u"session_term_term_lbl")

        self.horizontalLayout.addWidget(self.session_term_term_lbl)

        self.session_term_status_lbl = QLabel(Form)
        self.session_term_status_lbl.setObjectName(u"session_term_status_lbl")

        self.horizontalLayout.addWidget(self.session_term_status_lbl)

        self.session_term_date_lbl = QLabel(Form)
        self.session_term_date_lbl.setObjectName(u"session_term_date_lbl")

        self.horizontalLayout.addWidget(self.session_term_date_lbl)

        self.session_term_status_check = QCheckBox(Form)
        self.session_term_status_check.setObjectName(u"session_term_status_check")
        self.session_term_status_check.setStyleSheet(u"border:none;\n"
"background-color:none;")
        icon = QIcon()
        icon.addFile(u":/skyblue_icons/check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.session_term_status_check.setIcon(icon)

        self.horizontalLayout.addWidget(self.session_term_status_check)

        self.session_term_edit_btn = QPushButton(Form)
        self.session_term_edit_btn.setObjectName(u"session_term_edit_btn")
        self.session_term_edit_btn.setStyleSheet(u"border:none;\n"
"background-color:none;")
        icon1 = QIcon()
        icon1.addFile(u":/skyblue_icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.session_term_edit_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.session_term_edit_btn)

        self.session_term_delete_btn = QPushButton(Form)
        self.session_term_delete_btn.setObjectName(u"session_term_delete_btn")
        self.session_term_delete_btn.setStyleSheet(u"border:none;\n"
"background-color:none;")
        icon2 = QIcon()
        icon2.addFile(u":/skyblue_icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.session_term_delete_btn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.session_term_delete_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.session_term_id_label.setText(QCoreApplication.translate("Form", u"N/O", None))
        self.session_term_session_label.setText(QCoreApplication.translate("Form", u"N/O", None))
        self.session_term_term_lbl.setText(QCoreApplication.translate("Form", u"N/O", None))
        self.session_term_status_lbl.setText(QCoreApplication.translate("Form", u"N/O", None))
        self.session_term_date_lbl.setText(QCoreApplication.translate("Form", u"N/O", None))
        self.session_term_status_check.setText("")
        self.session_term_edit_btn.setText("")
        self.session_term_delete_btn.setText("")
    # retranslateUi

