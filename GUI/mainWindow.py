# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QVBoxLayout,
    QWidget)

from .Resources import images
from .Resources.icons.grey import grey
from .Resources.icons.skyblue import skyblue
from .Resources.icons.wiht import wiht

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1262, 958)
        self.actionUser_Manual = QAction(MainWindow)
        self.actionUser_Manual.setObjectName(u"actionUser_Manual")
        self.actionAbout_2 = QAction(MainWindow)
        self.actionAbout_2.setObjectName(u"actionAbout_2")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionChange_Password = QAction(MainWindow)
        self.actionChange_Password.setObjectName(u"actionChange_Password")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionEdit_Attendance = QAction(MainWindow)
        self.actionEdit_Attendance.setObjectName(u"actionEdit_Attendance")
        self.actionExport_Attendance_Report = QAction(MainWindow)
        self.actionExport_Attendance_Report.setObjectName(u"actionExport_Attendance_Report")
        self.actionNew_Attendance_Session = QAction(MainWindow)
        self.actionNew_Attendance_Session.setObjectName(u"actionNew_Attendance_Session")
        self.actionOpen_Session = QAction(MainWindow)
        self.actionOpen_Session.setObjectName(u"actionOpen_Session")
        self.actionSave_Sassion = QAction(MainWindow)
        self.actionSave_Sassion.setObjectName(u"actionSave_Sassion")
        self.actionTake_Attendance_2 = QAction(MainWindow)
        self.actionTake_Attendance_2.setObjectName(u"actionTake_Attendance_2")
        self.actionView_Attendance_Report_2 = QAction(MainWindow)
        self.actionView_Attendance_Report_2.setObjectName(u"actionView_Attendance_Report_2")
        self.actionTake_Employee_Attendance = QAction(MainWindow)
        self.actionTake_Employee_Attendance.setObjectName(u"actionTake_Employee_Attendance")
        self.actionView_Employee_Attendance_Reports = QAction(MainWindow)
        self.actionView_Employee_Attendance_Reports.setObjectName(u"actionView_Employee_Attendance_Reports")
        self.actionTake_Course_Attendance = QAction(MainWindow)
        self.actionTake_Course_Attendance.setObjectName(u"actionTake_Course_Attendance")
        self.actionView_Course_Attendance = QAction(MainWindow)
        self.actionView_Course_Attendance.setObjectName(u"actionView_Course_Attendance")
        self.actionTake_Exam_Attendance = QAction(MainWindow)
        self.actionTake_Exam_Attendance.setObjectName(u"actionTake_Exam_Attendance")
        self.actionView_Exam_Attendance = QAction(MainWindow)
        self.actionView_Exam_Attendance.setObjectName(u"actionView_Exam_Attendance")
        self.actionTake_Home_Attendance = QAction(MainWindow)
        self.actionTake_Home_Attendance.setObjectName(u"actionTake_Home_Attendance")
        self.actionView_Home_Attendance = QAction(MainWindow)
        self.actionView_Home_Attendance.setObjectName(u"actionView_Home_Attendance")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.TopFrame = QFrame(self.centralwidget)
        self.TopFrame.setObjectName(u"TopFrame")
        self.TopFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.TopFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.TopFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.topframe_frame_2 = QFrame(self.TopFrame)
        self.topframe_frame_2.setObjectName(u"topframe_frame_2")
        self.topframe_frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.topframe_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topframe_frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.topframe_frame_2)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/images/LOGIN.png"))

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout.addWidget(self.topframe_frame_2)

        self.topframe_frame = QFrame(self.TopFrame)
        self.topframe_frame.setObjectName(u"topframe_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topframe_frame.sizePolicy().hasHeightForWidth())
        self.topframe_frame.setSizePolicy(sizePolicy)
        self.topframe_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.topframe_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.topframe_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.main_date_label = QLabel(self.topframe_frame)
        self.main_date_label.setObjectName(u"main_date_label")

        self.verticalLayout_2.addWidget(self.main_date_label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_2 = QLabel(self.topframe_frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.topframe_frame)

        self.topframe_frame_3 = QFrame(self.TopFrame)
        self.topframe_frame_3.setObjectName(u"topframe_frame_3")
        self.topframe_frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.topframe_frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.topframe_frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.main_profile_icon = QLabel(self.topframe_frame_3)
        self.main_profile_icon.setObjectName(u"main_profile_icon")
        self.main_profile_icon.setPixmap(QPixmap(u":/grey_icons/user.svg"))
        self.main_profile_icon.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.main_profile_icon, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)

        self.main_username_label = QLabel(self.topframe_frame_3)
        self.main_username_label.setObjectName(u"main_username_label")

        self.verticalLayout_3.addWidget(self.main_username_label, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout.addWidget(self.topframe_frame_3)


        self.verticalLayout.addWidget(self.TopFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.manu_frame = QFrame(self.centralwidget)
        self.manu_frame.setObjectName(u"manu_frame")
        self.manu_frame.setStyleSheet(u"/* Dashboard Button Style */\n"
"QPushButton#dashboardButton {\n"
"    background-color: #2c3e50; /* Dark blue background color */\n"
"    border: none; /* No border */\n"
"    color: white; /* Text color */\n"
"    padding: 10px 20px; /* Padding */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-size: 14px; /* Font size */\n"
"}\n"
"\n"
"/* Hover Style */\n"
"QPushButton#dashboardButton:hover {\n"
"    background-color: #34495e; /* Slightly lighter blue on hover */\n"
"}\n"
"\n"
"/* Pressed Style */\n"
"QPushButton#dashboardButton:pressed {\n"
"    background-color: #2c3e50; /* Dark blue when pressed */\n"
"}\n"
"\n"
"/* Menu Button Style */\n"
"QPushButton#menuButton {\n"
"    background-color: rgba(55, 71, 79, 0.8); /* Dark grey background color with transparency */\n"
"    border: none; /* No border */\n"
"    color: white; /* Text color */\n"
"    padding: 10px 20px; /* Padding */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-size: 14px; /* Font size */\n"
"}\n"
"\n"
"/* Ho"
                        "ver Style */\n"
"QPushButton#menuButton:hover {\n"
"    background-color: rgba(55, 71, 79, 0.9); /* Slightly darker grey on hover */\n"
"}\n"
"\n"
"/* Pressed Style */\n"
"QPushButton#menuButton:pressed {\n"
"    background-color: rgba(55, 71, 79, 0.8); /* Dark grey when pressed */\n"
"}\n"
"")
        self.manu_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.manu_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.manu_frame)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.dashboardButton = QPushButton(self.manu_frame)
        self.dashboardButton.setObjectName(u"dashboardButton")
        font = QFont()
        font.setBold(True)
        self.dashboardButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/grey_icons/cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboardButton.setIcon(icon)

        self.verticalLayout_6.addWidget(self.dashboardButton, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.menuButton = QPushButton(self.manu_frame)
        self.menuButton.setObjectName(u"menuButton")
        icon1 = QIcon()
        icon1.addFile(u":/grey_icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.menuButton, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.manu_frame, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.MainFrame = QFrame(self.centralwidget)
        self.MainFrame.setObjectName(u"MainFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MainFrame.sizePolicy().hasHeightForWidth())
        self.MainFrame.setSizePolicy(sizePolicy1)
        self.MainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.MainFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu_main_frame = QFrame(self.MainFrame)
        self.menu_main_frame.setObjectName(u"menu_main_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menu_main_frame.sizePolicy().hasHeightForWidth())
        self.menu_main_frame.setSizePolicy(sizePolicy2)
        self.menu_main_frame.setMinimumSize(QSize(300, 0))
        self.menu_main_frame.setMaximumSize(QSize(0, 16777215))
        self.menu_main_frame.setStyleSheet(u"QLabel{\n"
"color:rgb(93, 93, 93);\n"
"}\n"
"QPushButton {\n"
"    background-color: #2c3e50; /* Dark blue background color */\n"
"    border: none; /* No border */\n"
"    color: white; /* Text color */\n"
"    padding: 10px 20px; /* Padding */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-size: 14px; /* Font size */\n"
"}\n"
"\n"
"/* Hover Style */\n"
"QPushButton:hover {\n"
"    background-color: rgba(52, 73, 94, 0.8); /* Slightly lighter blue on hover */\n"
"}\n"
"\n"
"/* Pressed Style */\n"
"QPushButton:pressed {\n"
"    background-color: #2c3e50; /* Dark blue when pressed */\n"
"}")
        self.menu_main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu_main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.menu_main_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(self.menu_main_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -345, 263, 1042))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 42, 0, 0)
        self.Class_course_btn = QPushButton(self.scrollAreaWidgetContents)
        self.Class_course_btn.setObjectName(u"Class_course_btn")
        font1 = QFont()
        font1.setBold(False)
        self.Class_course_btn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/grey_icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Class_course_btn.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.Class_course_btn)

        self.CLASS_COURSE_F = QFrame(self.scrollAreaWidgetContents)
        self.CLASS_COURSE_F.setObjectName(u"CLASS_COURSE_F")
        self.CLASS_COURSE_F.setMaximumSize(QSize(16777215, 16777215))
        self.CLASS_COURSE_F.setFrameShape(QFrame.Shape.NoFrame)
        self.CLASS_COURSE_F.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.CLASS_COURSE_F)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.label_3 = QLabel(self.CLASS_COURSE_F)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_7.addWidget(self.label_3)

        self.Create_class_btn = QPushButton(self.CLASS_COURSE_F)
        self.Create_class_btn.setObjectName(u"Create_class_btn")
        self.Create_class_btn.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_7.addWidget(self.Create_class_btn)

        self.label_4 = QLabel(self.CLASS_COURSE_F)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_7.addWidget(self.label_4)

        self.Create_course_btn = QPushButton(self.CLASS_COURSE_F)
        self.Create_course_btn.setObjectName(u"Create_course_btn")
        self.Create_course_btn.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_7.addWidget(self.Create_course_btn)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)


        self.verticalLayout_5.addWidget(self.CLASS_COURSE_F)

        self.Teachers_btn = QPushButton(self.scrollAreaWidgetContents)
        self.Teachers_btn.setObjectName(u"Teachers_btn")
        self.Teachers_btn.setIcon(icon2)
        self.Teachers_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.Teachers_btn)

        self.TEACHERS_F = QFrame(self.scrollAreaWidgetContents)
        self.TEACHERS_F.setObjectName(u"TEACHERS_F")
        self.TEACHERS_F.setFrameShape(QFrame.Shape.NoFrame)
        self.TEACHERS_F.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.TEACHERS_F)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.TEACHERS_F)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_8.addWidget(self.label_5)

        self.Create_teacher_btn = QPushButton(self.TEACHERS_F)
        self.Create_teacher_btn.setObjectName(u"Create_teacher_btn")

        self.verticalLayout_8.addWidget(self.Create_teacher_btn)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_7)


        self.verticalLayout_5.addWidget(self.TEACHERS_F)

        self.Student_menu_button = QPushButton(self.scrollAreaWidgetContents)
        self.Student_menu_button.setObjectName(u"Student_menu_button")
        self.Student_menu_button.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.Student_menu_button)

        self.STUDENT_F = QFrame(self.scrollAreaWidgetContents)
        self.STUDENT_F.setObjectName(u"STUDENT_F")
        self.STUDENT_F.setFrameShape(QFrame.Shape.NoFrame)
        self.STUDENT_F.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.STUDENT_F)
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.STUDENT_F)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_9.addWidget(self.label_7)

        self.Create_Student_button = QPushButton(self.STUDENT_F)
        self.Create_Student_button.setObjectName(u"Create_Student_button")

        self.verticalLayout_9.addWidget(self.Create_Student_button)

        self.View_Student_m_button = QPushButton(self.STUDENT_F)
        self.View_Student_m_button.setObjectName(u"View_Student_m_button")

        self.verticalLayout_9.addWidget(self.View_Student_m_button)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)


        self.verticalLayout_5.addWidget(self.STUDENT_F)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.Attendance_btn = QPushButton(self.scrollAreaWidgetContents)
        self.Attendance_btn.setObjectName(u"Attendance_btn")
        self.Attendance_btn.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.Attendance_btn)

        self.ATTENDANCE_F = QFrame(self.scrollAreaWidgetContents)
        self.ATTENDANCE_F.setObjectName(u"ATTENDANCE_F")
        self.ATTENDANCE_F.setMaximumSize(QSize(16777215, 16777215))
        self.ATTENDANCE_F.setFrameShape(QFrame.Shape.NoFrame)
        self.ATTENDANCE_F.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.ATTENDANCE_F)
        self.verticalLayout_10.setSpacing(4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.ATTENDANCE_F)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_10.addWidget(self.label_8)

        self.Take_attendance_btn = QPushButton(self.ATTENDANCE_F)
        self.Take_attendance_btn.setObjectName(u"Take_attendance_btn")

        self.verticalLayout_10.addWidget(self.Take_attendance_btn)

        self.View_class_attendance_btn = QPushButton(self.ATTENDANCE_F)
        self.View_class_attendance_btn.setObjectName(u"View_class_attendance_btn")

        self.verticalLayout_10.addWidget(self.View_class_attendance_btn)

        self.View_student_attendance_btn = QPushButton(self.ATTENDANCE_F)
        self.View_student_attendance_btn.setObjectName(u"View_student_attendance_btn")

        self.verticalLayout_10.addWidget(self.View_student_attendance_btn)

        self.Today_attendance_report_btn = QPushButton(self.ATTENDANCE_F)
        self.Today_attendance_report_btn.setObjectName(u"Today_attendance_report_btn")

        self.verticalLayout_10.addWidget(self.Today_attendance_report_btn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)


        self.verticalLayout_5.addWidget(self.ATTENDANCE_F)

        self.Session_term_btn = QPushButton(self.scrollAreaWidgetContents)
        self.Session_term_btn.setObjectName(u"Session_term_btn")
        self.Session_term_btn.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.Session_term_btn)

        self.SESSION_TERM_F = QFrame(self.scrollAreaWidgetContents)
        self.SESSION_TERM_F.setObjectName(u"SESSION_TERM_F")
        self.SESSION_TERM_F.setFrameShape(QFrame.Shape.NoFrame)
        self.SESSION_TERM_F.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.SESSION_TERM_F)
        self.verticalLayout_11.setSpacing(4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.SESSION_TERM_F)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_11.addWidget(self.label_9)

        self.Create_Session_term_btn = QPushButton(self.SESSION_TERM_F)
        self.Create_Session_term_btn.setObjectName(u"Create_Session_term_btn")

        self.verticalLayout_11.addWidget(self.Create_Session_term_btn)


        self.verticalLayout_5.addWidget(self.SESSION_TERM_F)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.horizontalLayout_4.addWidget(self.menu_main_frame)

        self.principal_frame = QFrame(self.MainFrame)
        self.principal_frame.setObjectName(u"principal_frame")
        sizePolicy1.setHeightForWidth(self.principal_frame.sizePolicy().hasHeightForWidth())
        self.principal_frame.setSizePolicy(sizePolicy1)
        self.principal_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.principal_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.principal_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scrollArea_2 = QScrollArea(self.principal_frame)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1389, 678))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.MainStackedWidget = QStackedWidget(self.scrollAreaWidgetContents_2)
        self.MainStackedWidget.setObjectName(u"MainStackedWidget")
        sizePolicy1.setHeightForWidth(self.MainStackedWidget.sizePolicy().hasHeightForWidth())
        self.MainStackedWidget.setSizePolicy(sizePolicy1)
        self.Welcom_page = QWidget()
        self.Welcom_page.setObjectName(u"Welcom_page")
        sizePolicy1.setHeightForWidth(self.Welcom_page.sizePolicy().hasHeightForWidth())
        self.Welcom_page.setSizePolicy(sizePolicy1)
        self.MainStackedWidget.addWidget(self.Welcom_page)
        self.Create_class_page = QWidget()
        self.Create_class_page.setObjectName(u"Create_class_page")
        sizePolicy1.setHeightForWidth(self.Create_class_page.sizePolicy().hasHeightForWidth())
        self.Create_class_page.setSizePolicy(sizePolicy1)
        self.verticalLayout_28 = QVBoxLayout(self.Create_class_page)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.Create_class_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_10)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_29)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_29)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_29.addWidget(self.label_26, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_17.addWidget(self.frame_29)

        self.frame_27 = QFrame(self.frame_10)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_17.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_10)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.goHome_button_2 = QPushButton(self.frame_28)
        self.goHome_button_2.setObjectName(u"goHome_button_2")
        self.goHome_button_2.setFont(font)
        self.goHome_button_2.setStyleSheet(u"border:none;\n"
"background-color:none;")

        self.horizontalLayout_16.addWidget(self.goHome_button_2)

        self.label_25 = QLabel(self.frame_28)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_16.addWidget(self.label_25)


        self.horizontalLayout_17.addWidget(self.frame_28)


        self.verticalLayout_28.addWidget(self.frame_10, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_25 = QFrame(self.Create_class_page)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_25)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_30)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_32)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"color:skyblue;")

        self.horizontalLayout_22.addWidget(self.label_27)

        self.createClassStatusLabel = QLabel(self.frame_32)
        self.createClassStatusLabel.setObjectName(u"createClassStatusLabel")

        self.horizontalLayout_22.addWidget(self.createClassStatusLabel)


        self.verticalLayout_30.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #5cacee;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #4caf50;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}")
        self.frame_33.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_33)
        self.verticalLayout_32.setSpacing(6)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_33)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"color:rgb(93, 93, 93);\n"
"")

        self.verticalLayout_32.addWidget(self.label_28)

        self.create_class_name_entry = QLineEdit(self.frame_33)
        self.create_class_name_entry.setObjectName(u"create_class_name_entry")

        self.verticalLayout_32.addWidget(self.create_class_name_entry)

        self.CreateClassPushButton = QPushButton(self.frame_33)
        self.CreateClassPushButton.setObjectName(u"CreateClassPushButton")

        self.verticalLayout_32.addWidget(self.CreateClassPushButton, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_30.addWidget(self.frame_33)


        self.horizontalLayout_18.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_25)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy)
        self.frame_31.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_18.addWidget(self.frame_31)


        self.verticalLayout_28.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.Create_class_page)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy1.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy1)
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_26)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_34 = QFrame(self.frame_26)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"QLabel{\n"
"	font-size: 14px;\n"
"	color: #333;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"")
        self.frame_34.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_37 = QFrame(self.frame_34)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(208, 0))
        self.frame_37.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_37)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, -1)
        self.label_29 = QLabel(self.frame_37)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_34.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_37)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_34.addWidget(self.label_30)

        self.ShowEntriesNumberspinBox = QSpinBox(self.frame_37)
        self.ShowEntriesNumberspinBox.setObjectName(u"ShowEntriesNumberspinBox")
        self.ShowEntriesNumberspinBox.setMinimumSize(QSize(200, 0))
        self.ShowEntriesNumberspinBox.setStyleSheet(u"padding: 6px;\n"
"color: #333;\n"
"background-color: #f0f0f0;")

        self.verticalLayout_34.addWidget(self.ShowEntriesNumberspinBox)

        self.label_31 = QLabel(self.frame_37)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_34.addWidget(self.label_31)


        self.horizontalLayout_19.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.frame_34)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy)
        self.frame_38.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.label_39 = QLabel(self.frame_38)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(320, 100, 323, 75))

        self.horizontalLayout_19.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_34)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_39)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 9)
        self.label_32 = QLabel(self.frame_39)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_2.addWidget(self.label_32, 0, 0, 1, 1)

        self.view_class_search_entry = QLineEdit(self.frame_39)
        self.view_class_search_entry.setObjectName(u"view_class_search_entry")

        self.gridLayout_2.addWidget(self.view_class_search_entry, 1, 0, 1, 1)

        self.view_class_search_btn = QPushButton(self.frame_39)
        self.view_class_search_btn.setObjectName(u"view_class_search_btn")
        icon3 = QIcon()
        icon3.addFile(u":/grey_icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.view_class_search_btn.setIcon(icon3)

        self.gridLayout_2.addWidget(self.view_class_search_btn, 1, 1, 1, 1)


        self.horizontalLayout_19.addWidget(self.frame_39)


        self.verticalLayout_33.addWidget(self.frame_34)

        self.showclassTableFrame = QFrame(self.frame_26)
        self.showclassTableFrame.setObjectName(u"showclassTableFrame")
        sizePolicy1.setHeightForWidth(self.showclassTableFrame.sizePolicy().hasHeightForWidth())
        self.showclassTableFrame.setSizePolicy(sizePolicy1)
        self.showclassTableFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.showclassTableFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.showclassTableFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(4)
        self.gridLayout_5.setContentsMargins(-1, 3, -1, 4)
        self.tableTitlwrowwidget = QWidget(self.showclassTableFrame)
        self.tableTitlwrowwidget.setObjectName(u"tableTitlwrowwidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableTitlwrowwidget.sizePolicy().hasHeightForWidth())
        self.tableTitlwrowwidget.setSizePolicy(sizePolicy4)
        self.tableTitlwrowwidget.setMinimumSize(QSize(0, 50))
        self.tableTitlwrowwidget.setMaximumSize(QSize(16777215, 50))
        self.tableTitlwrowwidget.setStyleSheet(u"background-color:rgb(205, 243, 255)")
        self.gridLayout_4 = QGridLayout(self.tableTitlwrowwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_37 = QLabel(self.tableTitlwrowwidget)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_4.addWidget(self.label_37, 2, 3, 1, 1)

        self.label_36 = QLabel(self.tableTitlwrowwidget)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_4.addWidget(self.label_36, 2, 1, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.label_40 = QLabel(self.tableTitlwrowwidget)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_4.addWidget(self.label_40, 2, 2, 1, 1)

        self.label_35 = QLabel(self.tableTitlwrowwidget)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_4.addWidget(self.label_35, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.tableTitlwrowwidget, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_33.addWidget(self.showclassTableFrame)

        self.frame_36 = QFrame(self.frame_26)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"QLabel{\n"
"	font-size: 12px;\n"
"	color: #666;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: darkgrey;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}")
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_40 = QFrame(self.frame_36)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_40)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.classesNumberLabel = QLabel(self.frame_40)
        self.classesNumberLabel.setObjectName(u"classesNumberLabel")

        self.verticalLayout_35.addWidget(self.classesNumberLabel)


        self.horizontalLayout_20.addWidget(self.frame_40, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_43 = QFrame(self.frame_36)
        self.frame_43.setObjectName(u"frame_43")
        sizePolicy.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy)
        self.frame_43.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_43.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_20.addWidget(self.frame_43)

        self.frame_41 = QFrame(self.frame_36)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.create_class_preview_btn = QPushButton(self.frame_41)
        self.create_class_preview_btn.setObjectName(u"create_class_preview_btn")
        icon4 = QIcon()
        icon4.addFile(u":/skyblue_icons/corner-up-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.create_class_preview_btn.setIcon(icon4)

        self.horizontalLayout_21.addWidget(self.create_class_preview_btn)

        self.currentClassPageLabel = QLabel(self.frame_41)
        self.currentClassPageLabel.setObjectName(u"currentClassPageLabel")

        self.horizontalLayout_21.addWidget(self.currentClassPageLabel)

        self.create_class_next_btn = QPushButton(self.frame_41)
        self.create_class_next_btn.setObjectName(u"create_class_next_btn")
        icon5 = QIcon()
        icon5.addFile(u":/skyblue_icons/corner-up-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.create_class_next_btn.setIcon(icon5)

        self.horizontalLayout_21.addWidget(self.create_class_next_btn)


        self.horizontalLayout_20.addWidget(self.frame_41, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_42 = QFrame(self.frame_36)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy)
        self.frame_42.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_20.addWidget(self.frame_42)


        self.verticalLayout_33.addWidget(self.frame_36, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_28.addWidget(self.frame_26)

        self.MainStackedWidget.addWidget(self.Create_class_page)
        self.Create_course_page = QWidget()
        self.Create_course_page.setObjectName(u"Create_course_page")
        sizePolicy1.setHeightForWidth(self.Create_course_page.sizePolicy().hasHeightForWidth())
        self.Create_course_page.setSizePolicy(sizePolicy1)
        self.verticalLayout_41 = QVBoxLayout(self.Create_course_page)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_35 = QFrame(self.Create_course_page)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.frame_35)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_44)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_44)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_31.addWidget(self.label_38, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_23.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.frame_35)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy)
        self.frame_45.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_45.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_23.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.frame_35)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_46.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.goHome_button_3 = QPushButton(self.frame_46)
        self.goHome_button_3.setObjectName(u"goHome_button_3")
        self.goHome_button_3.setFont(font)
        self.goHome_button_3.setStyleSheet(u"border:none;\n"
"background-color:none;")

        self.horizontalLayout_24.addWidget(self.goHome_button_3)

        self.label_41 = QLabel(self.frame_46)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_24.addWidget(self.label_41)


        self.horizontalLayout_23.addWidget(self.frame_46)


        self.verticalLayout_41.addWidget(self.frame_35)

        self.frame_47 = QFrame(self.Create_course_page)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_47.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.frame_47)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_48.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_48)
        self.verticalLayout_36.setSpacing(4)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.frame_49)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"color:skyblue;")

        self.horizontalLayout_26.addWidget(self.label_42)

        self.createClassCourseStatusLabel = QLabel(self.frame_49)
        self.createClassCourseStatusLabel.setObjectName(u"createClassCourseStatusLabel")

        self.horizontalLayout_26.addWidget(self.createClassCourseStatusLabel)


        self.verticalLayout_36.addWidget(self.frame_49)

        self.verticalSpacer = QSpacerItem(20, 14, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_36.addItem(self.verticalSpacer)

        self.frame_50 = QFrame(self.frame_48)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.frame_62 = QFrame(self.frame_50)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setStyleSheet(u"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #5cacee;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #4caf50;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}QLineEdit:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #5cacee;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border-color: #5cacee;\n"
"}")
        self.frame_62.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_62.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_62)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.CreateClassCoursePushButton = QPushButton(self.frame_62)
        self.CreateClassCoursePushButton.setObjectName(u"CreateClassCoursePushButton")

        self.gridLayout_9.addWidget(self.CreateClassCoursePushButton, 2, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_55 = QLabel(self.frame_62)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"color:rgb(93, 93, 93);\n"
"")

        self.gridLayout_9.addWidget(self.label_55, 0, 0, 1, 1)

        self.label_56 = QLabel(self.frame_62)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_9.addWidget(self.label_56, 0, 1, 1, 1)

        self.selectClassCombobox = QComboBox(self.frame_62)
        self.selectClassCombobox.setObjectName(u"selectClassCombobox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.selectClassCombobox.sizePolicy().hasHeightForWidth())
        self.selectClassCombobox.setSizePolicy(sizePolicy5)

        self.gridLayout_9.addWidget(self.selectClassCombobox, 1, 0, 1, 1)

        self.create_class_course_name_entry = QLineEdit(self.frame_62)
        self.create_class_course_name_entry.setObjectName(u"create_class_course_name_entry")

        self.gridLayout_9.addWidget(self.create_class_course_name_entry, 1, 1, 1, 1)


        self.horizontalLayout_30.addWidget(self.frame_62)


        self.verticalLayout_36.addWidget(self.frame_50)


        self.horizontalLayout_25.addWidget(self.frame_48)

        self.frame_51 = QFrame(self.frame_47)
        self.frame_51.setObjectName(u"frame_51")
        sizePolicy.setHeightForWidth(self.frame_51.sizePolicy().hasHeightForWidth())
        self.frame_51.setSizePolicy(sizePolicy)
        self.frame_51.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_25.addWidget(self.frame_51)


        self.verticalLayout_41.addWidget(self.frame_47)

        self.frame_52 = QFrame(self.Create_course_page)
        self.frame_52.setObjectName(u"frame_52")
        sizePolicy1.setHeightForWidth(self.frame_52.sizePolicy().hasHeightForWidth())
        self.frame_52.setSizePolicy(sizePolicy1)
        self.frame_52.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_52)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setStyleSheet(u"QLabel{\n"
"	font-size: 14px;\n"
"	color: #333;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"")
        self.frame_53.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_53.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.frame_54 = QFrame(self.frame_53)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(208, 0))
        self.frame_54.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_54.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_54)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, -1)
        self.label_44 = QLabel(self.frame_54)
        self.label_44.setObjectName(u"label_44")

        self.verticalLayout_39.addWidget(self.label_44)

        self.label_45 = QLabel(self.frame_54)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_39.addWidget(self.label_45)

        self.showCoursesEnrtiesspinBox = QSpinBox(self.frame_54)
        self.showCoursesEnrtiesspinBox.setObjectName(u"showCoursesEnrtiesspinBox")
        self.showCoursesEnrtiesspinBox.setMinimumSize(QSize(200, 0))
        self.showCoursesEnrtiesspinBox.setStyleSheet(u"padding: 6px;\n"
"color: #333;\n"
"background-color: #f0f0f0;")

        self.verticalLayout_39.addWidget(self.showCoursesEnrtiesspinBox)

        self.label_46 = QLabel(self.frame_54)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_39.addWidget(self.label_46)


        self.horizontalLayout_27.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.frame_53)
        self.frame_55.setObjectName(u"frame_55")
        sizePolicy.setHeightForWidth(self.frame_55.sizePolicy().hasHeightForWidth())
        self.frame_55.setSizePolicy(sizePolicy)
        self.frame_55.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_55.setFrameShadow(QFrame.Shadow.Raised)
        self.label_47 = QLabel(self.frame_55)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(320, 100, 323, 75))

        self.horizontalLayout_27.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.frame_53)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_56.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_56)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 9)
        self.label_48 = QLabel(self.frame_56)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_6.addWidget(self.label_48, 0, 0, 1, 1)

        self.view_class_courses_search_entry = QLineEdit(self.frame_56)
        self.view_class_courses_search_entry.setObjectName(u"view_class_courses_search_entry")

        self.gridLayout_6.addWidget(self.view_class_courses_search_entry, 1, 0, 1, 1)

        self.view_class_course_search_btn = QPushButton(self.frame_56)
        self.view_class_course_search_btn.setObjectName(u"view_class_course_search_btn")
        self.view_class_course_search_btn.setIcon(icon3)

        self.gridLayout_6.addWidget(self.view_class_course_search_btn, 1, 1, 1, 1)


        self.horizontalLayout_27.addWidget(self.frame_56)


        self.verticalLayout_38.addWidget(self.frame_53)

        self.showclassCoursesTableFrame = QFrame(self.frame_52)
        self.showclassCoursesTableFrame.setObjectName(u"showclassCoursesTableFrame")
        sizePolicy1.setHeightForWidth(self.showclassCoursesTableFrame.sizePolicy().hasHeightForWidth())
        self.showclassCoursesTableFrame.setSizePolicy(sizePolicy1)
        self.showclassCoursesTableFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.showclassCoursesTableFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.showclassCoursesTableFrame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(4)
        self.gridLayout_7.setContentsMargins(-1, 3, -1, 4)
        self.ClassCoursestableTitlewrowwidget = QWidget(self.showclassCoursesTableFrame)
        self.ClassCoursestableTitlewrowwidget.setObjectName(u"ClassCoursestableTitlewrowwidget")
        sizePolicy4.setHeightForWidth(self.ClassCoursestableTitlewrowwidget.sizePolicy().hasHeightForWidth())
        self.ClassCoursestableTitlewrowwidget.setSizePolicy(sizePolicy4)
        self.ClassCoursestableTitlewrowwidget.setMinimumSize(QSize(0, 50))
        self.ClassCoursestableTitlewrowwidget.setMaximumSize(QSize(16777215, 50))
        self.ClassCoursestableTitlewrowwidget.setStyleSheet(u"background-color:rgb(205, 243, 255)")
        self.horizontalLayout_31 = QHBoxLayout(self.ClassCoursestableTitlewrowwidget)
        self.horizontalLayout_31.setSpacing(9)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(9, -1, 9, 9)
        self.label_52 = QLabel(self.ClassCoursestableTitlewrowwidget)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_31.addWidget(self.label_52)

        self.label_50 = QLabel(self.ClassCoursestableTitlewrowwidget)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_31.addWidget(self.label_50)

        self.label_57 = QLabel(self.ClassCoursestableTitlewrowwidget)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_31.addWidget(self.label_57)

        self.label_58 = QLabel(self.ClassCoursestableTitlewrowwidget)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_31.addWidget(self.label_58)

        self.label_51 = QLabel(self.ClassCoursestableTitlewrowwidget)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_31.addWidget(self.label_51)

        self.label_49 = QLabel(self.ClassCoursestableTitlewrowwidget)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_31.addWidget(self.label_49)


        self.gridLayout_7.addWidget(self.ClassCoursestableTitlewrowwidget, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_38.addWidget(self.showclassCoursesTableFrame)

        self.frame_57 = QFrame(self.frame_52)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setStyleSheet(u"QLabel{\n"
"	font-size: 12px;\n"
"	color: #666;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: darkgrey;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}")
        self.frame_57.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.frame_58 = QFrame(self.frame_57)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_58)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.coursespageNumber_label = QLabel(self.frame_58)
        self.coursespageNumber_label.setObjectName(u"coursespageNumber_label")

        self.verticalLayout_40.addWidget(self.coursespageNumber_label)


        self.horizontalLayout_28.addWidget(self.frame_58, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_59 = QFrame(self.frame_57)
        self.frame_59.setObjectName(u"frame_59")
        sizePolicy.setHeightForWidth(self.frame_59.sizePolicy().hasHeightForWidth())
        self.frame_59.setSizePolicy(sizePolicy)
        self.frame_59.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_28.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_57)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_60.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.create_class_course_preview_btn = QPushButton(self.frame_60)
        self.create_class_course_preview_btn.setObjectName(u"create_class_course_preview_btn")
        self.create_class_course_preview_btn.setIcon(icon4)

        self.horizontalLayout_29.addWidget(self.create_class_course_preview_btn)

        self.current_courses_page_label = QLabel(self.frame_60)
        self.current_courses_page_label.setObjectName(u"current_courses_page_label")

        self.horizontalLayout_29.addWidget(self.current_courses_page_label)

        self.create_class_course_next_btn = QPushButton(self.frame_60)
        self.create_class_course_next_btn.setObjectName(u"create_class_course_next_btn")
        self.create_class_course_next_btn.setIcon(icon5)

        self.horizontalLayout_29.addWidget(self.create_class_course_next_btn)


        self.horizontalLayout_28.addWidget(self.frame_60, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_61 = QFrame(self.frame_57)
        self.frame_61.setObjectName(u"frame_61")
        sizePolicy.setHeightForWidth(self.frame_61.sizePolicy().hasHeightForWidth())
        self.frame_61.setSizePolicy(sizePolicy)
        self.frame_61.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_61.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_28.addWidget(self.frame_61)


        self.verticalLayout_38.addWidget(self.frame_57, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_41.addWidget(self.frame_52)

        self.MainStackedWidget.addWidget(self.Create_course_page)
        self.Create_teacher_page = QWidget()
        self.Create_teacher_page.setObjectName(u"Create_teacher_page")
        sizePolicy1.setHeightForWidth(self.Create_teacher_page.sizePolicy().hasHeightForWidth())
        self.Create_teacher_page.setSizePolicy(sizePolicy1)
        self.verticalLayout_47 = QVBoxLayout(self.Create_teacher_page)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.frame_73 = QFrame(self.Create_teacher_page)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_73.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_74 = QFrame(self.frame_73)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_74.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_74)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.frame_74)
        self.label_68.setObjectName(u"label_68")

        self.verticalLayout_45.addWidget(self.label_68, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_36.addWidget(self.frame_74)

        self.frame_75 = QFrame(self.frame_73)
        self.frame_75.setObjectName(u"frame_75")
        sizePolicy.setHeightForWidth(self.frame_75.sizePolicy().hasHeightForWidth())
        self.frame_75.setSizePolicy(sizePolicy)
        self.frame_75.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_75.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_36.addWidget(self.frame_75)

        self.frame_76 = QFrame(self.frame_73)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_76.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.goHome_button_4 = QPushButton(self.frame_76)
        self.goHome_button_4.setObjectName(u"goHome_button_4")
        self.goHome_button_4.setFont(font)
        self.goHome_button_4.setStyleSheet(u"border:none;\n"
"background-color:none;")

        self.horizontalLayout_37.addWidget(self.goHome_button_4)

        self.label_69 = QLabel(self.frame_76)
        self.label_69.setObjectName(u"label_69")

        self.horizontalLayout_37.addWidget(self.label_69)


        self.horizontalLayout_36.addWidget(self.frame_76)


        self.verticalLayout_47.addWidget(self.frame_73)

        self.frame_77 = QFrame(self.Create_teacher_page)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_77.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_78 = QFrame(self.frame_77)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_78.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_78)
        self.verticalLayout_46.setSpacing(4)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_79 = QFrame(self.frame_78)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_79.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_70 = QLabel(self.frame_79)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"color:skyblue;")

        self.horizontalLayout_39.addWidget(self.label_70)

        self.createTeachersStatusLabel = QLabel(self.frame_79)
        self.createTeachersStatusLabel.setObjectName(u"createTeachersStatusLabel")

        self.horizontalLayout_39.addWidget(self.createTeachersStatusLabel)


        self.verticalLayout_46.addWidget(self.frame_79)

        self.verticalSpacer_8 = QSpacerItem(20, 14, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_46.addItem(self.verticalSpacer_8)

        self.frame_80 = QFrame(self.frame_78)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.frame_81 = QFrame(self.frame_80)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setStyleSheet(u"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #5cacee;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #4caf50;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}QLineEdit:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #5cacee;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border-color: #5cacee;\n"
"}")
        self.frame_81.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_81.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_81)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.frame_81)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_11.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.Class_courses_combobox = QComboBox(self.frame_81)
        self.Class_courses_combobox.setObjectName(u"Class_courses_combobox")
        sizePolicy.setHeightForWidth(self.Class_courses_combobox.sizePolicy().hasHeightForWidth())
        self.Class_courses_combobox.setSizePolicy(sizePolicy)

        self.gridLayout_11.addWidget(self.Class_courses_combobox, 5, 1, 1, 1)

        self.label_73 = QLabel(self.frame_81)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_11.addWidget(self.label_73, 2, 1, 1, 1)

        self.CreateTeacherPushButton = QPushButton(self.frame_81)
        self.CreateTeacherPushButton.setObjectName(u"CreateTeacherPushButton")

        self.gridLayout_11.addWidget(self.CreateTeacherPushButton, 6, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_72 = QLabel(self.frame_81)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_11.addWidget(self.label_72, 4, 1, 1, 1)

        self.label_33 = QLabel(self.frame_81)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_11.addWidget(self.label_33, 0, 0, 1, 1)

        self.label_71 = QLabel(self.frame_81)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"color:rgb(93, 93, 93);\n"
"")

        self.gridLayout_11.addWidget(self.label_71, 4, 0, 1, 1)

        self.label_34 = QLabel(self.frame_81)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_11.addWidget(self.label_34, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_81)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_11.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.selectClassCombobox_createTeacher = QComboBox(self.frame_81)
        self.selectClassCombobox_createTeacher.setObjectName(u"selectClassCombobox_createTeacher")
        sizePolicy5.setHeightForWidth(self.selectClassCombobox_createTeacher.sizePolicy().hasHeightForWidth())
        self.selectClassCombobox_createTeacher.setSizePolicy(sizePolicy5)

        self.gridLayout_11.addWidget(self.selectClassCombobox_createTeacher, 5, 0, 1, 1)

        self.label_74 = QLabel(self.frame_81)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_11.addWidget(self.label_74, 0, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_81)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_11.addWidget(self.lineEdit_3, 3, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_81)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_11.addWidget(self.lineEdit_4, 3, 0, 1, 1)


        self.horizontalLayout_40.addWidget(self.frame_81)


        self.verticalLayout_46.addWidget(self.frame_80)


        self.horizontalLayout_38.addWidget(self.frame_78)

        self.frame_82 = QFrame(self.frame_77)
        self.frame_82.setObjectName(u"frame_82")
        sizePolicy.setHeightForWidth(self.frame_82.sizePolicy().hasHeightForWidth())
        self.frame_82.setSizePolicy(sizePolicy)
        self.frame_82.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_82.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_38.addWidget(self.frame_82)


        self.verticalLayout_47.addWidget(self.frame_77)

        self.frame_63 = QFrame(self.Create_teacher_page)
        self.frame_63.setObjectName(u"frame_63")
        sizePolicy1.setHeightForWidth(self.frame_63.sizePolicy().hasHeightForWidth())
        self.frame_63.setSizePolicy(sizePolicy1)
        self.frame_63.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_63)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.frame_64 = QFrame(self.frame_63)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setStyleSheet(u"QLabel{\n"
"	font-size: 14px;\n"
"	color: #333;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"")
        self.frame_64.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_64.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.frame_65 = QFrame(self.frame_64)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(208, 0))
        self.frame_65.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_65.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_65)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, -1)
        self.label_53 = QLabel(self.frame_65)
        self.label_53.setObjectName(u"label_53")

        self.verticalLayout_43.addWidget(self.label_53)

        self.label_54 = QLabel(self.frame_65)
        self.label_54.setObjectName(u"label_54")

        self.verticalLayout_43.addWidget(self.label_54)

        self.showTeachersEnrtiesspinBox = QSpinBox(self.frame_65)
        self.showTeachersEnrtiesspinBox.setObjectName(u"showTeachersEnrtiesspinBox")
        self.showTeachersEnrtiesspinBox.setMinimumSize(QSize(200, 0))
        self.showTeachersEnrtiesspinBox.setStyleSheet(u"padding: 6px;\n"
"color: #333;\n"
"background-color: #f0f0f0;")

        self.verticalLayout_43.addWidget(self.showTeachersEnrtiesspinBox)

        self.label_59 = QLabel(self.frame_65)
        self.label_59.setObjectName(u"label_59")

        self.verticalLayout_43.addWidget(self.label_59)


        self.horizontalLayout_32.addWidget(self.frame_65)

        self.frame_66 = QFrame(self.frame_64)
        self.frame_66.setObjectName(u"frame_66")
        sizePolicy.setHeightForWidth(self.frame_66.sizePolicy().hasHeightForWidth())
        self.frame_66.setSizePolicy(sizePolicy)
        self.frame_66.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_66.setFrameShadow(QFrame.Shadow.Raised)
        self.label_60 = QLabel(self.frame_66)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(320, 100, 323, 75))

        self.horizontalLayout_32.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.frame_64)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_67.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_67)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 9)
        self.label_61 = QLabel(self.frame_67)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_8.addWidget(self.label_61, 0, 0, 1, 1)

        self.view_teachers_search_entry = QLineEdit(self.frame_67)
        self.view_teachers_search_entry.setObjectName(u"view_teachers_search_entry")

        self.gridLayout_8.addWidget(self.view_teachers_search_entry, 1, 0, 1, 1)

        self.view_teachers_search_btn = QPushButton(self.frame_67)
        self.view_teachers_search_btn.setObjectName(u"view_teachers_search_btn")
        self.view_teachers_search_btn.setIcon(icon3)

        self.gridLayout_8.addWidget(self.view_teachers_search_btn, 1, 1, 1, 1)


        self.horizontalLayout_32.addWidget(self.frame_67)


        self.verticalLayout_42.addWidget(self.frame_64)

        self.showTeachersTableFrame = QFrame(self.frame_63)
        self.showTeachersTableFrame.setObjectName(u"showTeachersTableFrame")
        sizePolicy1.setHeightForWidth(self.showTeachersTableFrame.sizePolicy().hasHeightForWidth())
        self.showTeachersTableFrame.setSizePolicy(sizePolicy1)
        self.showTeachersTableFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.showTeachersTableFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.showTeachersTableFrame)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setVerticalSpacing(4)
        self.gridLayout_10.setContentsMargins(-1, 3, -1, 4)
        self.ClassCoursestableTitlewrowwidget_2 = QWidget(self.showTeachersTableFrame)
        self.ClassCoursestableTitlewrowwidget_2.setObjectName(u"ClassCoursestableTitlewrowwidget_2")
        sizePolicy4.setHeightForWidth(self.ClassCoursestableTitlewrowwidget_2.sizePolicy().hasHeightForWidth())
        self.ClassCoursestableTitlewrowwidget_2.setSizePolicy(sizePolicy4)
        self.ClassCoursestableTitlewrowwidget_2.setMinimumSize(QSize(0, 50))
        self.ClassCoursestableTitlewrowwidget_2.setMaximumSize(QSize(16777215, 50))
        self.ClassCoursestableTitlewrowwidget_2.setStyleSheet(u"background-color:rgb(205, 243, 255)")
        self.horizontalLayout_33 = QHBoxLayout(self.ClassCoursestableTitlewrowwidget_2)
        self.horizontalLayout_33.setSpacing(9)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(9, -1, 9, 9)
        self.label_62 = QLabel(self.ClassCoursestableTitlewrowwidget_2)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_33.addWidget(self.label_62)

        self.label_63 = QLabel(self.ClassCoursestableTitlewrowwidget_2)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_33.addWidget(self.label_63)

        self.label_64 = QLabel(self.ClassCoursestableTitlewrowwidget_2)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_33.addWidget(self.label_64)

        self.label_65 = QLabel(self.ClassCoursestableTitlewrowwidget_2)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_33.addWidget(self.label_65)

        self.label_75 = QLabel(self.ClassCoursestableTitlewrowwidget_2)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_33.addWidget(self.label_75)

        self.label_66 = QLabel(self.ClassCoursestableTitlewrowwidget_2)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_33.addWidget(self.label_66)

        self.label_76 = QLabel(self.ClassCoursestableTitlewrowwidget_2)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_33.addWidget(self.label_76)

        self.label_67 = QLabel(self.ClassCoursestableTitlewrowwidget_2)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_33.addWidget(self.label_67)


        self.gridLayout_10.addWidget(self.ClassCoursestableTitlewrowwidget_2, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_42.addWidget(self.showTeachersTableFrame)

        self.frame_68 = QFrame(self.frame_63)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setStyleSheet(u"QLabel{\n"
"	font-size: 12px;\n"
"	color: #666;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: darkgrey;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}")
        self.frame_68.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.frame_69 = QFrame(self.frame_68)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_69.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_69)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.teachersPageNumber_label = QLabel(self.frame_69)
        self.teachersPageNumber_label.setObjectName(u"teachersPageNumber_label")

        self.verticalLayout_44.addWidget(self.teachersPageNumber_label)


        self.horizontalLayout_34.addWidget(self.frame_69, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_70 = QFrame(self.frame_68)
        self.frame_70.setObjectName(u"frame_70")
        sizePolicy.setHeightForWidth(self.frame_70.sizePolicy().hasHeightForWidth())
        self.frame_70.setSizePolicy(sizePolicy)
        self.frame_70.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_70.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_34.addWidget(self.frame_70)

        self.frame_71 = QFrame(self.frame_68)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_71.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.show_teacher_preview_btn = QPushButton(self.frame_71)
        self.show_teacher_preview_btn.setObjectName(u"show_teacher_preview_btn")
        self.show_teacher_preview_btn.setIcon(icon4)

        self.horizontalLayout_35.addWidget(self.show_teacher_preview_btn)

        self.currentpage_teacher_page_label = QLabel(self.frame_71)
        self.currentpage_teacher_page_label.setObjectName(u"currentpage_teacher_page_label")

        self.horizontalLayout_35.addWidget(self.currentpage_teacher_page_label)

        self.ciew_teachers_next_btn = QPushButton(self.frame_71)
        self.ciew_teachers_next_btn.setObjectName(u"ciew_teachers_next_btn")
        self.ciew_teachers_next_btn.setIcon(icon5)

        self.horizontalLayout_35.addWidget(self.ciew_teachers_next_btn)


        self.horizontalLayout_34.addWidget(self.frame_71, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_72 = QFrame(self.frame_68)
        self.frame_72.setObjectName(u"frame_72")
        sizePolicy.setHeightForWidth(self.frame_72.sizePolicy().hasHeightForWidth())
        self.frame_72.setSizePolicy(sizePolicy)
        self.frame_72.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_72.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_34.addWidget(self.frame_72)


        self.verticalLayout_42.addWidget(self.frame_68, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_47.addWidget(self.frame_63)

        self.MainStackedWidget.addWidget(self.Create_teacher_page)
        self.Create_student_page = QWidget()
        self.Create_student_page.setObjectName(u"Create_student_page")
        sizePolicy1.setHeightForWidth(self.Create_student_page.sizePolicy().hasHeightForWidth())
        self.Create_student_page.setSizePolicy(sizePolicy1)
        self.verticalLayout_53 = QVBoxLayout(self.Create_student_page)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.frame_83 = QFrame(self.Create_student_page)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_83.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_84 = QFrame(self.frame_83)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_84.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_84)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.frame_84)
        self.label_77.setObjectName(u"label_77")

        self.verticalLayout_48.addWidget(self.label_77, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_10 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_48.addItem(self.verticalSpacer_10)


        self.horizontalLayout_41.addWidget(self.frame_84)

        self.frame_85 = QFrame(self.frame_83)
        self.frame_85.setObjectName(u"frame_85")
        sizePolicy.setHeightForWidth(self.frame_85.sizePolicy().hasHeightForWidth())
        self.frame_85.setSizePolicy(sizePolicy)
        self.frame_85.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_85.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_41.addWidget(self.frame_85)

        self.frame_86 = QFrame(self.frame_83)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_86.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.goHome_button_5 = QPushButton(self.frame_86)
        self.goHome_button_5.setObjectName(u"goHome_button_5")
        self.goHome_button_5.setFont(font)
        self.goHome_button_5.setStyleSheet(u"border:none;\n"
"background-color:none;")

        self.horizontalLayout_42.addWidget(self.goHome_button_5)

        self.label_78 = QLabel(self.frame_86)
        self.label_78.setObjectName(u"label_78")

        self.horizontalLayout_42.addWidget(self.label_78)


        self.horizontalLayout_41.addWidget(self.frame_86)


        self.verticalLayout_53.addWidget(self.frame_83)

        self.frame_97 = QFrame(self.Create_student_page)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_97.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_98.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_98)
        self.verticalLayout_52.setSpacing(4)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_99 = QFrame(self.frame_98)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_99.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_92 = QLabel(self.frame_99)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setStyleSheet(u"color:skyblue;")

        self.horizontalLayout_48.addWidget(self.label_92)

        self.createTeachersStatusLabel_2 = QLabel(self.frame_99)
        self.createTeachersStatusLabel_2.setObjectName(u"createTeachersStatusLabel_2")

        self.horizontalLayout_48.addWidget(self.createTeachersStatusLabel_2)


        self.verticalLayout_52.addWidget(self.frame_99)

        self.verticalSpacer_9 = QSpacerItem(20, 14, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_52.addItem(self.verticalSpacer_9)

        self.frame_100 = QFrame(self.frame_98)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.frame_101 = QFrame(self.frame_100)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setStyleSheet(u"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #5cacee;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #4caf50;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}QLineEdit:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #5cacee;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border-color: #5cacee;\n"
"}")
        self.frame_101.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_101.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_101)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.student_lastname_entry = QLineEdit(self.frame_101)
        self.student_lastname_entry.setObjectName(u"student_lastname_entry")

        self.gridLayout_14.addWidget(self.student_lastname_entry, 1, 1, 1, 1)

        self.Class_courses_combobox_students = QComboBox(self.frame_101)
        self.Class_courses_combobox_students.setObjectName(u"Class_courses_combobox_students")
        sizePolicy.setHeightForWidth(self.Class_courses_combobox_students.sizePolicy().hasHeightForWidth())
        self.Class_courses_combobox_students.setSizePolicy(sizePolicy)

        self.gridLayout_14.addWidget(self.Class_courses_combobox_students, 5, 1, 1, 1)

        self.label_93 = QLabel(self.frame_101)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout_14.addWidget(self.label_93, 2, 1, 1, 1)

        self.CreateStudentPushButton = QPushButton(self.frame_101)
        self.CreateStudentPushButton.setObjectName(u"CreateStudentPushButton")

        self.gridLayout_14.addWidget(self.CreateStudentPushButton, 6, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_94 = QLabel(self.frame_101)
        self.label_94.setObjectName(u"label_94")

        self.gridLayout_14.addWidget(self.label_94, 4, 1, 1, 1)

        self.label_95 = QLabel(self.frame_101)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_14.addWidget(self.label_95, 0, 0, 1, 1)

        self.label_96 = QLabel(self.frame_101)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setStyleSheet(u"color:rgb(93, 93, 93);\n"
"")

        self.gridLayout_14.addWidget(self.label_96, 4, 0, 1, 1)

        self.label_97 = QLabel(self.frame_101)
        self.label_97.setObjectName(u"label_97")

        self.gridLayout_14.addWidget(self.label_97, 2, 0, 1, 1)

        self.student_firtname_entry = QLineEdit(self.frame_101)
        self.student_firtname_entry.setObjectName(u"student_firtname_entry")

        self.gridLayout_14.addWidget(self.student_firtname_entry, 1, 0, 1, 1)

        self.selectClassCombobox_createStudent = QComboBox(self.frame_101)
        self.selectClassCombobox_createStudent.setObjectName(u"selectClassCombobox_createStudent")
        sizePolicy5.setHeightForWidth(self.selectClassCombobox_createStudent.sizePolicy().hasHeightForWidth())
        self.selectClassCombobox_createStudent.setSizePolicy(sizePolicy5)

        self.gridLayout_14.addWidget(self.selectClassCombobox_createStudent, 5, 0, 1, 1)

        self.label_98 = QLabel(self.frame_101)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout_14.addWidget(self.label_98, 0, 1, 1, 1)

        self.student_admission_number_enty = QLineEdit(self.frame_101)
        self.student_admission_number_enty.setObjectName(u"student_admission_number_enty")

        self.gridLayout_14.addWidget(self.student_admission_number_enty, 3, 1, 1, 1)

        self.student_othername_entry = QLineEdit(self.frame_101)
        self.student_othername_entry.setObjectName(u"student_othername_entry")

        self.gridLayout_14.addWidget(self.student_othername_entry, 3, 0, 1, 1)


        self.horizontalLayout_49.addWidget(self.frame_101)


        self.verticalLayout_52.addWidget(self.frame_100)


        self.horizontalLayout_47.addWidget(self.frame_98)

        self.frame_102 = QFrame(self.frame_97)
        self.frame_102.setObjectName(u"frame_102")
        sizePolicy.setHeightForWidth(self.frame_102.sizePolicy().hasHeightForWidth())
        self.frame_102.setSizePolicy(sizePolicy)
        self.frame_102.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_102.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_47.addWidget(self.frame_102)


        self.verticalLayout_53.addWidget(self.frame_97)

        self.frame_87 = QFrame(self.Create_student_page)
        self.frame_87.setObjectName(u"frame_87")
        sizePolicy1.setHeightForWidth(self.frame_87.sizePolicy().hasHeightForWidth())
        self.frame_87.setSizePolicy(sizePolicy1)
        self.frame_87.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_87)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.frame_88 = QFrame(self.frame_87)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setStyleSheet(u"QLabel{\n"
"	font-size: 14px;\n"
"	color: #333;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"")
        self.frame_88.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_88.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_88)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.frame_89 = QFrame(self.frame_88)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(208, 0))
        self.frame_89.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_89.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_89)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, -1)
        self.label_79 = QLabel(self.frame_89)
        self.label_79.setObjectName(u"label_79")

        self.verticalLayout_50.addWidget(self.label_79)

        self.label_80 = QLabel(self.frame_89)
        self.label_80.setObjectName(u"label_80")

        self.verticalLayout_50.addWidget(self.label_80)

        self.showStudentsEnrtiesspinBox = QSpinBox(self.frame_89)
        self.showStudentsEnrtiesspinBox.setObjectName(u"showStudentsEnrtiesspinBox")
        self.showStudentsEnrtiesspinBox.setMinimumSize(QSize(200, 0))
        self.showStudentsEnrtiesspinBox.setStyleSheet(u"padding: 6px;\n"
"color: #333;\n"
"background-color: #f0f0f0;")

        self.verticalLayout_50.addWidget(self.showStudentsEnrtiesspinBox)

        self.label_81 = QLabel(self.frame_89)
        self.label_81.setObjectName(u"label_81")

        self.verticalLayout_50.addWidget(self.label_81)


        self.horizontalLayout_43.addWidget(self.frame_89)

        self.frame_90 = QFrame(self.frame_88)
        self.frame_90.setObjectName(u"frame_90")
        sizePolicy.setHeightForWidth(self.frame_90.sizePolicy().hasHeightForWidth())
        self.frame_90.setSizePolicy(sizePolicy)
        self.frame_90.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_90.setFrameShadow(QFrame.Shadow.Raised)
        self.label_82 = QLabel(self.frame_90)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(320, 100, 323, 75))

        self.horizontalLayout_43.addWidget(self.frame_90)

        self.frame_91 = QFrame(self.frame_88)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_91.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_91)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 9)
        self.label_83 = QLabel(self.frame_91)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_12.addWidget(self.label_83, 0, 0, 1, 1)

        self.view_students_search_entry = QLineEdit(self.frame_91)
        self.view_students_search_entry.setObjectName(u"view_students_search_entry")

        self.gridLayout_12.addWidget(self.view_students_search_entry, 1, 0, 1, 1)

        self.view_students_search_btn = QPushButton(self.frame_91)
        self.view_students_search_btn.setObjectName(u"view_students_search_btn")
        self.view_students_search_btn.setIcon(icon3)

        self.gridLayout_12.addWidget(self.view_students_search_btn, 1, 1, 1, 1)


        self.horizontalLayout_43.addWidget(self.frame_91)


        self.verticalLayout_49.addWidget(self.frame_88)

        self.showTeachersTableFrame_2 = QFrame(self.frame_87)
        self.showTeachersTableFrame_2.setObjectName(u"showTeachersTableFrame_2")
        sizePolicy1.setHeightForWidth(self.showTeachersTableFrame_2.sizePolicy().hasHeightForWidth())
        self.showTeachersTableFrame_2.setSizePolicy(sizePolicy1)
        self.showTeachersTableFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.showTeachersTableFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.showTeachersTableFrame_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setVerticalSpacing(4)
        self.gridLayout_13.setContentsMargins(-1, 3, -1, 4)
        self.ClassCoursestableTitlewrowwidget_3 = QWidget(self.showTeachersTableFrame_2)
        self.ClassCoursestableTitlewrowwidget_3.setObjectName(u"ClassCoursestableTitlewrowwidget_3")
        sizePolicy4.setHeightForWidth(self.ClassCoursestableTitlewrowwidget_3.sizePolicy().hasHeightForWidth())
        self.ClassCoursestableTitlewrowwidget_3.setSizePolicy(sizePolicy4)
        self.ClassCoursestableTitlewrowwidget_3.setMinimumSize(QSize(0, 50))
        self.ClassCoursestableTitlewrowwidget_3.setMaximumSize(QSize(16777215, 50))
        self.ClassCoursestableTitlewrowwidget_3.setStyleSheet(u"background-color:rgb(205, 243, 255)")
        self.horizontalLayout_44 = QHBoxLayout(self.ClassCoursestableTitlewrowwidget_3)
        self.horizontalLayout_44.setSpacing(9)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(9, -1, 9, 9)
        self.label_84 = QLabel(self.ClassCoursestableTitlewrowwidget_3)
        self.label_84.setObjectName(u"label_84")

        self.horizontalLayout_44.addWidget(self.label_84)

        self.label_85 = QLabel(self.ClassCoursestableTitlewrowwidget_3)
        self.label_85.setObjectName(u"label_85")

        self.horizontalLayout_44.addWidget(self.label_85)

        self.label_86 = QLabel(self.ClassCoursestableTitlewrowwidget_3)
        self.label_86.setObjectName(u"label_86")

        self.horizontalLayout_44.addWidget(self.label_86)

        self.label_87 = QLabel(self.ClassCoursestableTitlewrowwidget_3)
        self.label_87.setObjectName(u"label_87")

        self.horizontalLayout_44.addWidget(self.label_87)

        self.label_88 = QLabel(self.ClassCoursestableTitlewrowwidget_3)
        self.label_88.setObjectName(u"label_88")

        self.horizontalLayout_44.addWidget(self.label_88)

        self.label_89 = QLabel(self.ClassCoursestableTitlewrowwidget_3)
        self.label_89.setObjectName(u"label_89")

        self.horizontalLayout_44.addWidget(self.label_89)

        self.label_43 = QLabel(self.ClassCoursestableTitlewrowwidget_3)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_44.addWidget(self.label_43)

        self.label_90 = QLabel(self.ClassCoursestableTitlewrowwidget_3)
        self.label_90.setObjectName(u"label_90")

        self.horizontalLayout_44.addWidget(self.label_90)

        self.label_99 = QLabel(self.ClassCoursestableTitlewrowwidget_3)
        self.label_99.setObjectName(u"label_99")

        self.horizontalLayout_44.addWidget(self.label_99)

        self.label_91 = QLabel(self.ClassCoursestableTitlewrowwidget_3)
        self.label_91.setObjectName(u"label_91")

        self.horizontalLayout_44.addWidget(self.label_91)


        self.gridLayout_13.addWidget(self.ClassCoursestableTitlewrowwidget_3, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_49.addWidget(self.showTeachersTableFrame_2)

        self.frame_92 = QFrame(self.frame_87)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setStyleSheet(u"QLabel{\n"
"	font-size: 12px;\n"
"	color: #666;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: darkgrey;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}")
        self.frame_92.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.frame_93 = QFrame(self.frame_92)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_93.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_93)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.studentsPageNumber_label = QLabel(self.frame_93)
        self.studentsPageNumber_label.setObjectName(u"studentsPageNumber_label")

        self.verticalLayout_51.addWidget(self.studentsPageNumber_label)


        self.horizontalLayout_45.addWidget(self.frame_93, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_94 = QFrame(self.frame_92)
        self.frame_94.setObjectName(u"frame_94")
        sizePolicy.setHeightForWidth(self.frame_94.sizePolicy().hasHeightForWidth())
        self.frame_94.setSizePolicy(sizePolicy)
        self.frame_94.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_94.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_45.addWidget(self.frame_94)

        self.frame_95 = QFrame(self.frame_92)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_95.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_95)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.show_students_preview_btn = QPushButton(self.frame_95)
        self.show_students_preview_btn.setObjectName(u"show_students_preview_btn")
        self.show_students_preview_btn.setIcon(icon4)

        self.horizontalLayout_46.addWidget(self.show_students_preview_btn)

        self.currentpage_students_page_label = QLabel(self.frame_95)
        self.currentpage_students_page_label.setObjectName(u"currentpage_students_page_label")

        self.horizontalLayout_46.addWidget(self.currentpage_students_page_label)

        self.ciew_student_next_btn = QPushButton(self.frame_95)
        self.ciew_student_next_btn.setObjectName(u"ciew_student_next_btn")
        self.ciew_student_next_btn.setIcon(icon5)

        self.horizontalLayout_46.addWidget(self.ciew_student_next_btn)


        self.horizontalLayout_45.addWidget(self.frame_95, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_96 = QFrame(self.frame_92)
        self.frame_96.setObjectName(u"frame_96")
        sizePolicy.setHeightForWidth(self.frame_96.sizePolicy().hasHeightForWidth())
        self.frame_96.setSizePolicy(sizePolicy)
        self.frame_96.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_96.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_45.addWidget(self.frame_96)


        self.verticalLayout_49.addWidget(self.frame_92, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_53.addWidget(self.frame_87)

        self.MainStackedWidget.addWidget(self.Create_student_page)
        self.View_student_page = QWidget()
        self.View_student_page.setObjectName(u"View_student_page")
        sizePolicy1.setHeightForWidth(self.View_student_page.sizePolicy().hasHeightForWidth())
        self.View_student_page.setSizePolicy(sizePolicy1)
        self.View_student_page.setStyleSheet(u"")
        self.verticalLayout_64 = QVBoxLayout(self.View_student_page)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.frame_139 = QFrame(self.View_student_page)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_139.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_139)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frame_140 = QFrame(self.frame_139)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_140.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_140)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.teacher_m_title_lbl = QLabel(self.frame_140)
        self.teacher_m_title_lbl.setObjectName(u"teacher_m_title_lbl")

        self.verticalLayout_63.addWidget(self.teacher_m_title_lbl, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_13 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_63.addItem(self.verticalSpacer_13)


        self.horizontalLayout_66.addWidget(self.frame_140)

        self.frame_141 = QFrame(self.frame_139)
        self.frame_141.setObjectName(u"frame_141")
        sizePolicy.setHeightForWidth(self.frame_141.sizePolicy().hasHeightForWidth())
        self.frame_141.setSizePolicy(sizePolicy)
        self.frame_141.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_141.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_66.addWidget(self.frame_141)

        self.frame_142 = QFrame(self.frame_139)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_142.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_142)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.goHome_button_7 = QPushButton(self.frame_142)
        self.goHome_button_7.setObjectName(u"goHome_button_7")
        self.goHome_button_7.setFont(font)
        self.goHome_button_7.setStyleSheet(u"border:none;\n"
"background-color:none;")

        self.horizontalLayout_67.addWidget(self.goHome_button_7)

        self.label_140 = QLabel(self.frame_142)
        self.label_140.setObjectName(u"label_140")

        self.horizontalLayout_67.addWidget(self.label_140)


        self.horizontalLayout_66.addWidget(self.frame_142)


        self.verticalLayout_64.addWidget(self.frame_139)

        self.frame_123 = QFrame(self.View_student_page)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_123.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_123)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_124 = QFrame(self.frame_123)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_124.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_124)
        self.verticalLayout_59.setSpacing(4)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_125 = QFrame(self.frame_124)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_125.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_125)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_117 = QLabel(self.frame_125)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setStyleSheet(u"color:skyblue;")

        self.horizontalLayout_60.addWidget(self.label_117)


        self.verticalLayout_59.addWidget(self.frame_125)

        self.verticalSpacer_12 = QSpacerItem(20, 14, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_59.addItem(self.verticalSpacer_12)


        self.horizontalLayout_59.addWidget(self.frame_124)

        self.frame_128 = QFrame(self.frame_123)
        self.frame_128.setObjectName(u"frame_128")
        sizePolicy.setHeightForWidth(self.frame_128.sizePolicy().hasHeightForWidth())
        self.frame_128.setSizePolicy(sizePolicy)
        self.frame_128.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_128.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_59.addWidget(self.frame_128)


        self.verticalLayout_64.addWidget(self.frame_123)

        self.frame_129 = QFrame(self.View_student_page)
        self.frame_129.setObjectName(u"frame_129")
        sizePolicy1.setHeightForWidth(self.frame_129.sizePolicy().hasHeightForWidth())
        self.frame_129.setSizePolicy(sizePolicy1)
        self.frame_129.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_129)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.frame_130 = QFrame(self.frame_129)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setStyleSheet(u"QLabel{\n"
"	font-size: 14px;\n"
"	color: #333;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"")
        self.frame_130.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_130.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_130)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.frame_131 = QFrame(self.frame_130)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setMinimumSize(QSize(208, 0))
        self.frame_131.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_131.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_131)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, -1)
        self.label_125 = QLabel(self.frame_131)
        self.label_125.setObjectName(u"label_125")

        self.verticalLayout_61.addWidget(self.label_125)

        self.showStudentsListEnrtiesspinBox = QSpinBox(self.frame_131)
        self.showStudentsListEnrtiesspinBox.setObjectName(u"showStudentsListEnrtiesspinBox")
        self.showStudentsListEnrtiesspinBox.setMinimumSize(QSize(200, 0))
        self.showStudentsListEnrtiesspinBox.setStyleSheet(u"padding: 6px;\n"
"color: #333;\n"
"background-color: #f0f0f0;")

        self.verticalLayout_61.addWidget(self.showStudentsListEnrtiesspinBox)

        self.label_126 = QLabel(self.frame_131)
        self.label_126.setObjectName(u"label_126")

        self.verticalLayout_61.addWidget(self.label_126)


        self.horizontalLayout_62.addWidget(self.frame_131)

        self.frame_132 = QFrame(self.frame_130)
        self.frame_132.setObjectName(u"frame_132")
        sizePolicy.setHeightForWidth(self.frame_132.sizePolicy().hasHeightForWidth())
        self.frame_132.setSizePolicy(sizePolicy)
        self.frame_132.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_132.setFrameShadow(QFrame.Shadow.Raised)
        self.label_127 = QLabel(self.frame_132)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setGeometry(QRect(320, 100, 323, 75))

        self.horizontalLayout_62.addWidget(self.frame_132)

        self.frame_133 = QFrame(self.frame_130)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_133.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_133)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 9)
        self.label_128 = QLabel(self.frame_133)
        self.label_128.setObjectName(u"label_128")

        self.gridLayout_19.addWidget(self.label_128, 0, 0, 1, 1)

        self.view_studentsList_search_entry = QLineEdit(self.frame_133)
        self.view_studentsList_search_entry.setObjectName(u"view_studentsList_search_entry")

        self.gridLayout_19.addWidget(self.view_studentsList_search_entry, 1, 0, 1, 1)

        self.view_studentsList_search_btn = QPushButton(self.frame_133)
        self.view_studentsList_search_btn.setObjectName(u"view_studentsList_search_btn")
        self.view_studentsList_search_btn.setIcon(icon3)

        self.gridLayout_19.addWidget(self.view_studentsList_search_btn, 1, 1, 1, 1)


        self.horizontalLayout_62.addWidget(self.frame_133)


        self.verticalLayout_60.addWidget(self.frame_130)

        self.showTeachersTableFrame_3 = QFrame(self.frame_129)
        self.showTeachersTableFrame_3.setObjectName(u"showTeachersTableFrame_3")
        sizePolicy1.setHeightForWidth(self.showTeachersTableFrame_3.sizePolicy().hasHeightForWidth())
        self.showTeachersTableFrame_3.setSizePolicy(sizePolicy1)
        self.showTeachersTableFrame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.showTeachersTableFrame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_20 = QGridLayout(self.showTeachersTableFrame_3)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setVerticalSpacing(4)
        self.gridLayout_20.setContentsMargins(-1, 3, -1, 4)
        self.ClassCoursestableTitlewrowwidget_5 = QWidget(self.showTeachersTableFrame_3)
        self.ClassCoursestableTitlewrowwidget_5.setObjectName(u"ClassCoursestableTitlewrowwidget_5")
        sizePolicy4.setHeightForWidth(self.ClassCoursestableTitlewrowwidget_5.sizePolicy().hasHeightForWidth())
        self.ClassCoursestableTitlewrowwidget_5.setSizePolicy(sizePolicy4)
        self.ClassCoursestableTitlewrowwidget_5.setMinimumSize(QSize(0, 50))
        self.ClassCoursestableTitlewrowwidget_5.setMaximumSize(QSize(16777215, 50))
        self.ClassCoursestableTitlewrowwidget_5.setStyleSheet(u"background-color:rgb(205, 243, 255)")
        self.horizontalLayout_63 = QHBoxLayout(self.ClassCoursestableTitlewrowwidget_5)
        self.horizontalLayout_63.setSpacing(9)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(9, -1, 9, 9)
        self.label_129 = QLabel(self.ClassCoursestableTitlewrowwidget_5)
        self.label_129.setObjectName(u"label_129")

        self.horizontalLayout_63.addWidget(self.label_129)

        self.label_130 = QLabel(self.ClassCoursestableTitlewrowwidget_5)
        self.label_130.setObjectName(u"label_130")

        self.horizontalLayout_63.addWidget(self.label_130)

        self.label_131 = QLabel(self.ClassCoursestableTitlewrowwidget_5)
        self.label_131.setObjectName(u"label_131")

        self.horizontalLayout_63.addWidget(self.label_131)

        self.label_132 = QLabel(self.ClassCoursestableTitlewrowwidget_5)
        self.label_132.setObjectName(u"label_132")

        self.horizontalLayout_63.addWidget(self.label_132)

        self.label_133 = QLabel(self.ClassCoursestableTitlewrowwidget_5)
        self.label_133.setObjectName(u"label_133")

        self.horizontalLayout_63.addWidget(self.label_133)

        self.label_134 = QLabel(self.ClassCoursestableTitlewrowwidget_5)
        self.label_134.setObjectName(u"label_134")

        self.horizontalLayout_63.addWidget(self.label_134)

        self.label_135 = QLabel(self.ClassCoursestableTitlewrowwidget_5)
        self.label_135.setObjectName(u"label_135")

        self.horizontalLayout_63.addWidget(self.label_135)

        self.label_136 = QLabel(self.ClassCoursestableTitlewrowwidget_5)
        self.label_136.setObjectName(u"label_136")

        self.horizontalLayout_63.addWidget(self.label_136)


        self.gridLayout_20.addWidget(self.ClassCoursestableTitlewrowwidget_5, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_60.addWidget(self.showTeachersTableFrame_3)

        self.frame_134 = QFrame(self.frame_129)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setStyleSheet(u"QLabel{\n"
"	font-size: 12px;\n"
"	color: #666;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: darkgrey;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}")
        self.frame_134.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_134)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.frame_135 = QFrame(self.frame_134)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_135.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_135)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.studentsListPageNumber_label = QLabel(self.frame_135)
        self.studentsListPageNumber_label.setObjectName(u"studentsListPageNumber_label")

        self.verticalLayout_62.addWidget(self.studentsListPageNumber_label)


        self.horizontalLayout_64.addWidget(self.frame_135, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_136 = QFrame(self.frame_134)
        self.frame_136.setObjectName(u"frame_136")
        sizePolicy.setHeightForWidth(self.frame_136.sizePolicy().hasHeightForWidth())
        self.frame_136.setSizePolicy(sizePolicy)
        self.frame_136.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_136.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_64.addWidget(self.frame_136)

        self.frame_137 = QFrame(self.frame_134)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_137.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_137)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.show_studentsList_preview_btn = QPushButton(self.frame_137)
        self.show_studentsList_preview_btn.setObjectName(u"show_studentsList_preview_btn")
        self.show_studentsList_preview_btn.setIcon(icon4)

        self.horizontalLayout_65.addWidget(self.show_studentsList_preview_btn)

        self.currentpage_studentsList_page_label = QLabel(self.frame_137)
        self.currentpage_studentsList_page_label.setObjectName(u"currentpage_studentsList_page_label")

        self.horizontalLayout_65.addWidget(self.currentpage_studentsList_page_label)

        self.ciew_studentList_next_btn = QPushButton(self.frame_137)
        self.ciew_studentList_next_btn.setObjectName(u"ciew_studentList_next_btn")
        self.ciew_studentList_next_btn.setIcon(icon5)

        self.horizontalLayout_65.addWidget(self.ciew_studentList_next_btn)


        self.horizontalLayout_64.addWidget(self.frame_137, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_138 = QFrame(self.frame_134)
        self.frame_138.setObjectName(u"frame_138")
        sizePolicy.setHeightForWidth(self.frame_138.sizePolicy().hasHeightForWidth())
        self.frame_138.setSizePolicy(sizePolicy)
        self.frame_138.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_138.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_64.addWidget(self.frame_138)


        self.verticalLayout_60.addWidget(self.frame_134, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_64.addWidget(self.frame_129)

        self.MainStackedWidget.addWidget(self.View_student_page)
        self.sessions_terms_page = QWidget()
        self.sessions_terms_page.setObjectName(u"sessions_terms_page")
        self.verticalLayout_58 = QVBoxLayout(self.sessions_terms_page)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.frame_119 = QFrame(self.sessions_terms_page)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_119.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_119)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_120 = QFrame(self.frame_119)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_120.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_120)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_114 = QLabel(self.frame_120)
        self.label_114.setObjectName(u"label_114")

        self.verticalLayout_57.addWidget(self.label_114, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_57.addWidget(self.frame_120)

        self.frame_121 = QFrame(self.frame_119)
        self.frame_121.setObjectName(u"frame_121")
        sizePolicy.setHeightForWidth(self.frame_121.sizePolicy().hasHeightForWidth())
        self.frame_121.setSizePolicy(sizePolicy)
        self.frame_121.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_121.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_57.addWidget(self.frame_121)

        self.frame_122 = QFrame(self.frame_119)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_122.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_122)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.goHome_button_6 = QPushButton(self.frame_122)
        self.goHome_button_6.setObjectName(u"goHome_button_6")
        self.goHome_button_6.setFont(font)
        self.goHome_button_6.setStyleSheet(u"border:none;\n"
"background-color:none;")

        self.horizontalLayout_58.addWidget(self.goHome_button_6)

        self.label_115 = QLabel(self.frame_122)
        self.label_115.setObjectName(u"label_115")

        self.horizontalLayout_58.addWidget(self.label_115)


        self.horizontalLayout_57.addWidget(self.frame_122)


        self.verticalLayout_58.addWidget(self.frame_119)

        self.frame_103 = QFrame(self.sessions_terms_page)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_103.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_104 = QFrame(self.frame_103)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_104.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_104)
        self.verticalLayout_37.setSpacing(4)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_105 = QFrame(self.frame_104)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_105.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_100 = QLabel(self.frame_105)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setStyleSheet(u"color:skyblue;")

        self.horizontalLayout_51.addWidget(self.label_100)

        self.createSessionTermStatusLabel = QLabel(self.frame_105)
        self.createSessionTermStatusLabel.setObjectName(u"createSessionTermStatusLabel")

        self.horizontalLayout_51.addWidget(self.createSessionTermStatusLabel)


        self.verticalLayout_37.addWidget(self.frame_105)

        self.verticalSpacer_11 = QSpacerItem(20, 14, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_37.addItem(self.verticalSpacer_11)

        self.frame_106 = QFrame(self.frame_104)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.frame_107 = QFrame(self.frame_106)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setStyleSheet(u"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #5cacee;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #4caf50;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}QLineEdit:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #5cacee;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border-color: #5cacee;\n"
"}")
        self.frame_107.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_107.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_107)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.createSesionTermPushButton = QPushButton(self.frame_107)
        self.createSesionTermPushButton.setObjectName(u"createSesionTermPushButton")

        self.gridLayout_15.addWidget(self.createSesionTermPushButton, 2, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_101 = QLabel(self.frame_107)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setStyleSheet(u"color:rgb(93, 93, 93);\n"
"")

        self.gridLayout_15.addWidget(self.label_101, 0, 0, 1, 1)

        self.selectTermCombobox = QComboBox(self.frame_107)
        self.selectTermCombobox.addItem("")
        self.selectTermCombobox.addItem("")
        self.selectTermCombobox.addItem("")
        self.selectTermCombobox.setObjectName(u"selectTermCombobox")
        sizePolicy5.setHeightForWidth(self.selectTermCombobox.sizePolicy().hasHeightForWidth())
        self.selectTermCombobox.setSizePolicy(sizePolicy5)

        self.gridLayout_15.addWidget(self.selectTermCombobox, 1, 1, 1, 1)

        self.label_102 = QLabel(self.frame_107)
        self.label_102.setObjectName(u"label_102")

        self.gridLayout_15.addWidget(self.label_102, 0, 1, 1, 1)

        self.create_session_entry = QLineEdit(self.frame_107)
        self.create_session_entry.setObjectName(u"create_session_entry")

        self.gridLayout_15.addWidget(self.create_session_entry, 1, 0, 1, 1)


        self.horizontalLayout_52.addWidget(self.frame_107)


        self.verticalLayout_37.addWidget(self.frame_106)


        self.horizontalLayout_50.addWidget(self.frame_104)

        self.frame_108 = QFrame(self.frame_103)
        self.frame_108.setObjectName(u"frame_108")
        sizePolicy.setHeightForWidth(self.frame_108.sizePolicy().hasHeightForWidth())
        self.frame_108.setSizePolicy(sizePolicy)
        self.frame_108.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_108.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_50.addWidget(self.frame_108)


        self.verticalLayout_58.addWidget(self.frame_103)

        self.frame_109 = QFrame(self.sessions_terms_page)
        self.frame_109.setObjectName(u"frame_109")
        sizePolicy1.setHeightForWidth(self.frame_109.sizePolicy().hasHeightForWidth())
        self.frame_109.setSizePolicy(sizePolicy1)
        self.frame_109.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_109)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.frame_110 = QFrame(self.frame_109)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setStyleSheet(u"QLabel{\n"
"	font-size: 14px;\n"
"	color: #333;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"")
        self.frame_110.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_110.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_110)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.frame_111 = QFrame(self.frame_110)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setMinimumSize(QSize(208, 0))
        self.frame_111.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_111.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_111)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, -1)
        self.label_103 = QLabel(self.frame_111)
        self.label_103.setObjectName(u"label_103")

        self.verticalLayout_55.addWidget(self.label_103)

        self.label_104 = QLabel(self.frame_111)
        self.label_104.setObjectName(u"label_104")

        self.verticalLayout_55.addWidget(self.label_104)

        self.showSessionsEnrtiesspinBox = QSpinBox(self.frame_111)
        self.showSessionsEnrtiesspinBox.setObjectName(u"showSessionsEnrtiesspinBox")
        self.showSessionsEnrtiesspinBox.setMinimumSize(QSize(200, 0))
        self.showSessionsEnrtiesspinBox.setStyleSheet(u"padding: 6px;\n"
"color: #333;\n"
"background-color: #f0f0f0;")

        self.verticalLayout_55.addWidget(self.showSessionsEnrtiesspinBox)

        self.label_105 = QLabel(self.frame_111)
        self.label_105.setObjectName(u"label_105")

        self.verticalLayout_55.addWidget(self.label_105)


        self.horizontalLayout_53.addWidget(self.frame_111)

        self.frame_112 = QFrame(self.frame_110)
        self.frame_112.setObjectName(u"frame_112")
        sizePolicy.setHeightForWidth(self.frame_112.sizePolicy().hasHeightForWidth())
        self.frame_112.setSizePolicy(sizePolicy)
        self.frame_112.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_112.setFrameShadow(QFrame.Shadow.Raised)
        self.label_106 = QLabel(self.frame_112)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setGeometry(QRect(320, 100, 323, 75))

        self.horizontalLayout_53.addWidget(self.frame_112)

        self.frame_113 = QFrame(self.frame_110)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_113.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_113)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 9)
        self.view_session_term_search_btn = QPushButton(self.frame_113)
        self.view_session_term_search_btn.setObjectName(u"view_session_term_search_btn")
        self.view_session_term_search_btn.setIcon(icon3)

        self.gridLayout_16.addWidget(self.view_session_term_search_btn, 2, 1, 1, 1)

        self.label_107 = QLabel(self.frame_113)
        self.label_107.setObjectName(u"label_107")

        self.gridLayout_16.addWidget(self.label_107, 1, 0, 1, 1)

        self.view_session_term_search_entry = QLineEdit(self.frame_113)
        self.view_session_term_search_entry.setObjectName(u"view_session_term_search_entry")

        self.gridLayout_16.addWidget(self.view_session_term_search_entry, 2, 0, 1, 1)

        self.label_116 = QLabel(self.frame_113)
        self.label_116.setObjectName(u"label_116")

        self.gridLayout_16.addWidget(self.label_116, 0, 0, 1, 1)


        self.horizontalLayout_53.addWidget(self.frame_113)


        self.verticalLayout_54.addWidget(self.frame_110)

        self.showclassCoursesTableFrame_2 = QFrame(self.frame_109)
        self.showclassCoursesTableFrame_2.setObjectName(u"showclassCoursesTableFrame_2")
        sizePolicy1.setHeightForWidth(self.showclassCoursesTableFrame_2.sizePolicy().hasHeightForWidth())
        self.showclassCoursesTableFrame_2.setSizePolicy(sizePolicy1)
        self.showclassCoursesTableFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.showclassCoursesTableFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_17 = QGridLayout(self.showclassCoursesTableFrame_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setVerticalSpacing(4)
        self.gridLayout_17.setContentsMargins(-1, 3, -1, 4)
        self.ClassCoursestableTitlewrowwidget_4 = QWidget(self.showclassCoursesTableFrame_2)
        self.ClassCoursestableTitlewrowwidget_4.setObjectName(u"ClassCoursestableTitlewrowwidget_4")
        sizePolicy4.setHeightForWidth(self.ClassCoursestableTitlewrowwidget_4.sizePolicy().hasHeightForWidth())
        self.ClassCoursestableTitlewrowwidget_4.setSizePolicy(sizePolicy4)
        self.ClassCoursestableTitlewrowwidget_4.setMinimumSize(QSize(0, 50))
        self.ClassCoursestableTitlewrowwidget_4.setMaximumSize(QSize(16777215, 50))
        self.ClassCoursestableTitlewrowwidget_4.setStyleSheet(u"background-color:rgb(205, 243, 255)")
        self.horizontalLayout_54 = QHBoxLayout(self.ClassCoursestableTitlewrowwidget_4)
        self.horizontalLayout_54.setSpacing(9)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(9, -1, 9, 9)
        self.label_108 = QLabel(self.ClassCoursestableTitlewrowwidget_4)
        self.label_108.setObjectName(u"label_108")

        self.horizontalLayout_54.addWidget(self.label_108)

        self.label_109 = QLabel(self.ClassCoursestableTitlewrowwidget_4)
        self.label_109.setObjectName(u"label_109")

        self.horizontalLayout_54.addWidget(self.label_109)

        self.label_110 = QLabel(self.ClassCoursestableTitlewrowwidget_4)
        self.label_110.setObjectName(u"label_110")

        self.horizontalLayout_54.addWidget(self.label_110)

        self.label_111 = QLabel(self.ClassCoursestableTitlewrowwidget_4)
        self.label_111.setObjectName(u"label_111")

        self.horizontalLayout_54.addWidget(self.label_111)

        self.label_112 = QLabel(self.ClassCoursestableTitlewrowwidget_4)
        self.label_112.setObjectName(u"label_112")

        self.horizontalLayout_54.addWidget(self.label_112)

        self.label_113 = QLabel(self.ClassCoursestableTitlewrowwidget_4)
        self.label_113.setObjectName(u"label_113")

        self.horizontalLayout_54.addWidget(self.label_113)


        self.gridLayout_17.addWidget(self.ClassCoursestableTitlewrowwidget_4, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_54.addWidget(self.showclassCoursesTableFrame_2)

        self.frame_114 = QFrame(self.frame_109)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setStyleSheet(u"QLabel{\n"
"	font-size: 12px;\n"
"	color: #666;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: darkgrey;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}")
        self.frame_114.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_114)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.frame_115 = QFrame(self.frame_114)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_115.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_115)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.SessionTermpageNumber_label = QLabel(self.frame_115)
        self.SessionTermpageNumber_label.setObjectName(u"SessionTermpageNumber_label")

        self.verticalLayout_56.addWidget(self.SessionTermpageNumber_label)


        self.horizontalLayout_55.addWidget(self.frame_115, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_116 = QFrame(self.frame_114)
        self.frame_116.setObjectName(u"frame_116")
        sizePolicy.setHeightForWidth(self.frame_116.sizePolicy().hasHeightForWidth())
        self.frame_116.setSizePolicy(sizePolicy)
        self.frame_116.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_116.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_55.addWidget(self.frame_116)

        self.frame_117 = QFrame(self.frame_114)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_117.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.create_session_term_preview_btn = QPushButton(self.frame_117)
        self.create_session_term_preview_btn.setObjectName(u"create_session_term_preview_btn")
        self.create_session_term_preview_btn.setIcon(icon4)

        self.horizontalLayout_56.addWidget(self.create_session_term_preview_btn)

        self.current_session_terms_page_label = QLabel(self.frame_117)
        self.current_session_terms_page_label.setObjectName(u"current_session_terms_page_label")

        self.horizontalLayout_56.addWidget(self.current_session_terms_page_label)

        self.create_session_term_next_btn = QPushButton(self.frame_117)
        self.create_session_term_next_btn.setObjectName(u"create_session_term_next_btn")
        self.create_session_term_next_btn.setIcon(icon5)

        self.horizontalLayout_56.addWidget(self.create_session_term_next_btn)


        self.horizontalLayout_55.addWidget(self.frame_117, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_118 = QFrame(self.frame_114)
        self.frame_118.setObjectName(u"frame_118")
        sizePolicy.setHeightForWidth(self.frame_118.sizePolicy().hasHeightForWidth())
        self.frame_118.setSizePolicy(sizePolicy)
        self.frame_118.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_118.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_55.addWidget(self.frame_118)


        self.verticalLayout_54.addWidget(self.frame_114, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_58.addWidget(self.frame_109)

        self.MainStackedWidget.addWidget(self.sessions_terms_page)
        self.Take_attendance_page = QWidget()
        self.Take_attendance_page.setObjectName(u"Take_attendance_page")
        sizePolicy1.setHeightForWidth(self.Take_attendance_page.sizePolicy().hasHeightForWidth())
        self.Take_attendance_page.setSizePolicy(sizePolicy1)
        self.verticalLayout_66 = QVBoxLayout(self.Take_attendance_page)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.frame_143 = QFrame(self.Take_attendance_page)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_143.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_143)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.frame_144 = QFrame(self.frame_143)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_144.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_144)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.teacher_m_title_lbl_2 = QLabel(self.frame_144)
        self.teacher_m_title_lbl_2.setObjectName(u"teacher_m_title_lbl_2")

        self.verticalLayout_65.addWidget(self.teacher_m_title_lbl_2, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_14 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_65.addItem(self.verticalSpacer_14)


        self.horizontalLayout_68.addWidget(self.frame_144)

        self.frame_145 = QFrame(self.frame_143)
        self.frame_145.setObjectName(u"frame_145")
        sizePolicy.setHeightForWidth(self.frame_145.sizePolicy().hasHeightForWidth())
        self.frame_145.setSizePolicy(sizePolicy)
        self.frame_145.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_145.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_68.addWidget(self.frame_145)

        self.frame_146 = QFrame(self.frame_143)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_146.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_146)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.takeAttendGoHome_button = QPushButton(self.frame_146)
        self.takeAttendGoHome_button.setObjectName(u"takeAttendGoHome_button")
        self.takeAttendGoHome_button.setFont(font)
        self.takeAttendGoHome_button.setStyleSheet(u"border:none;\n"
"background-color:none;")

        self.horizontalLayout_69.addWidget(self.takeAttendGoHome_button)

        self.label_141 = QLabel(self.frame_146)
        self.label_141.setObjectName(u"label_141")

        self.horizontalLayout_69.addWidget(self.label_141)


        self.horizontalLayout_68.addWidget(self.frame_146)


        self.verticalLayout_66.addWidget(self.frame_143)

        self.frame_126 = QFrame(self.Take_attendance_page)
        self.frame_126.setObjectName(u"frame_126")
        sizePolicy1.setHeightForWidth(self.frame_126.sizePolicy().hasHeightForWidth())
        self.frame_126.setSizePolicy(sizePolicy1)
        self.frame_126.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_126)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.frame_127 = QFrame(self.frame_126)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_127)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_118 = QLabel(self.frame_127)
        self.label_118.setObjectName(u"label_118")

        self.horizontalLayout_61.addWidget(self.label_118)

        self.frame_148 = QFrame(self.frame_127)
        self.frame_148.setObjectName(u"frame_148")
        sizePolicy.setHeightForWidth(self.frame_148.sizePolicy().hasHeightForWidth())
        self.frame_148.setSizePolicy(sizePolicy)
        self.frame_148.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_148)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.label_120 = QLabel(self.frame_148)
        self.label_120.setObjectName(u"label_120")

        self.verticalLayout_68.addWidget(self.label_120)

        self.available_devices_combo = QComboBox(self.frame_148)
        self.available_devices_combo.setObjectName(u"available_devices_combo")
        self.available_devices_combo.setStyleSheet(u"background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;")

        self.verticalLayout_68.addWidget(self.available_devices_combo)


        self.horizontalLayout_61.addWidget(self.frame_148)

        self.label_119 = QLabel(self.frame_127)
        self.label_119.setObjectName(u"label_119")

        self.horizontalLayout_61.addWidget(self.label_119)


        self.verticalLayout_67.addWidget(self.frame_127)

        self.frame_147 = QFrame(self.frame_126)
        self.frame_147.setObjectName(u"frame_147")
        sizePolicy1.setHeightForWidth(self.frame_147.sizePolicy().hasHeightForWidth())
        self.frame_147.setSizePolicy(sizePolicy1)
        self.frame_147.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_147)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.frame_149 = QFrame(self.frame_147)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_149)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.frame_151 = QFrame(self.frame_149)
        self.frame_151.setObjectName(u"frame_151")
        sizePolicy.setHeightForWidth(self.frame_151.sizePolicy().hasHeightForWidth())
        self.frame_151.setSizePolicy(sizePolicy)
        self.frame_151.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_70.addWidget(self.frame_151)

        self.frame_152 = QFrame(self.frame_149)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_152)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_121 = QLabel(self.frame_152)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMinimumSize(QSize(250, 250))
        self.label_121.setMaximumSize(QSize(250, 250))

        self.horizontalLayout_71.addWidget(self.label_121, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_70.addWidget(self.frame_152)

        self.frame_153 = QFrame(self.frame_149)
        self.frame_153.setObjectName(u"frame_153")
        sizePolicy.setHeightForWidth(self.frame_153.sizePolicy().hasHeightForWidth())
        self.frame_153.setSizePolicy(sizePolicy)
        self.frame_153.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_70.addWidget(self.frame_153)


        self.verticalLayout_69.addWidget(self.frame_149)

        self.frame_150 = QFrame(self.frame_147)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_150)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.attendance_stdnt_number_lbl = QLabel(self.frame_150)
        self.attendance_stdnt_number_lbl.setObjectName(u"attendance_stdnt_number_lbl")

        self.gridLayout_3.addWidget(self.attendance_stdnt_number_lbl, 1, 0, 1, 1)

        self.label_142 = QLabel(self.frame_150)
        self.label_142.setObjectName(u"label_142")

        self.gridLayout_3.addWidget(self.label_142, 2, 1, 1, 1)

        self.label_123 = QLabel(self.frame_150)
        self.label_123.setObjectName(u"label_123")

        self.gridLayout_3.addWidget(self.label_123, 0, 1, 1, 1)

        self.label_122 = QLabel(self.frame_150)
        self.label_122.setObjectName(u"label_122")

        self.gridLayout_3.addWidget(self.label_122, 0, 0, 1, 1)

        self.attendance_student_class_option_lbl = QLabel(self.frame_150)
        self.attendance_student_class_option_lbl.setObjectName(u"attendance_student_class_option_lbl")

        self.gridLayout_3.addWidget(self.attendance_student_class_option_lbl, 1, 2, 1, 1)

        self.atendance_student_dep_lbl = QLabel(self.frame_150)
        self.atendance_student_dep_lbl.setObjectName(u"atendance_student_dep_lbl")

        self.gridLayout_3.addWidget(self.atendance_student_dep_lbl, 1, 1, 1, 1)

        self.label_124 = QLabel(self.frame_150)
        self.label_124.setObjectName(u"label_124")

        self.gridLayout_3.addWidget(self.label_124, 0, 2, 1, 1)

        self.attendance_student_status = QLabel(self.frame_150)
        self.attendance_student_status.setObjectName(u"attendance_student_status")

        self.gridLayout_3.addWidget(self.attendance_student_status, 3, 1, 1, 1)


        self.verticalLayout_69.addWidget(self.frame_150)


        self.verticalLayout_67.addWidget(self.frame_147)


        self.verticalLayout_66.addWidget(self.frame_126)

        self.MainStackedWidget.addWidget(self.Take_attendance_page)
        self.View_class_attendance_page = QWidget()
        self.View_class_attendance_page.setObjectName(u"View_class_attendance_page")
        sizePolicy1.setHeightForWidth(self.View_class_attendance_page.sizePolicy().hasHeightForWidth())
        self.View_class_attendance_page.setSizePolicy(sizePolicy1)
        self.View_class_attendance_page.setStyleSheet(u"")
        self.verticalLayout_75 = QVBoxLayout(self.View_class_attendance_page)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.frame_154 = QFrame(self.View_class_attendance_page)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_154.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_154)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.frame_155 = QFrame(self.frame_154)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_155.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_155)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.label_137 = QLabel(self.frame_155)
        self.label_137.setObjectName(u"label_137")

        self.verticalLayout_70.addWidget(self.label_137, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_72.addWidget(self.frame_155)

        self.frame_156 = QFrame(self.frame_154)
        self.frame_156.setObjectName(u"frame_156")
        sizePolicy.setHeightForWidth(self.frame_156.sizePolicy().hasHeightForWidth())
        self.frame_156.setSizePolicy(sizePolicy)
        self.frame_156.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_156.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_72.addWidget(self.frame_156)

        self.frame_157 = QFrame(self.frame_154)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_157.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_157)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.goHome_button_8 = QPushButton(self.frame_157)
        self.goHome_button_8.setObjectName(u"goHome_button_8")
        self.goHome_button_8.setFont(font)
        self.goHome_button_8.setStyleSheet(u"border:none;\n"
"background-color:none;")

        self.horizontalLayout_73.addWidget(self.goHome_button_8)

        self.label_138 = QLabel(self.frame_157)
        self.label_138.setObjectName(u"label_138")

        self.horizontalLayout_73.addWidget(self.label_138)


        self.horizontalLayout_72.addWidget(self.frame_157)


        self.verticalLayout_75.addWidget(self.frame_154)

        self.frame_158 = QFrame(self.View_class_attendance_page)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_158.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_158)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.frame_159 = QFrame(self.frame_158)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_159.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_159)
        self.verticalLayout_71.setSpacing(4)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.frame_160 = QFrame(self.frame_159)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_160.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_160)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.label_139 = QLabel(self.frame_160)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setStyleSheet(u"color:skyblue;")

        self.horizontalLayout_75.addWidget(self.label_139)

        self.createSessionTermStatusLabel_2 = QLabel(self.frame_160)
        self.createSessionTermStatusLabel_2.setObjectName(u"createSessionTermStatusLabel_2")

        self.horizontalLayout_75.addWidget(self.createSessionTermStatusLabel_2)


        self.verticalLayout_71.addWidget(self.frame_160)

        self.verticalSpacer_15 = QSpacerItem(20, 14, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_71.addItem(self.verticalSpacer_15)

        self.frame_161 = QFrame(self.frame_159)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_161)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.frame_162 = QFrame(self.frame_161)
        self.frame_162.setObjectName(u"frame_162")
        self.frame_162.setStyleSheet(u"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #5cacee;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #4caf50;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}QLineEdit:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #5cacee;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border-color: #5cacee;\n"
"}")
        self.frame_162.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_162.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_162)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_143 = QLabel(self.frame_162)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setStyleSheet(u"color:rgb(93, 93, 93);\n"
"")

        self.gridLayout_18.addWidget(self.label_143, 0, 0, 1, 1)

        self.ViewAttendanceDateedit = QDateEdit(self.frame_162)
        self.ViewAttendanceDateedit.setObjectName(u"ViewAttendanceDateedit")
        sizePolicy5.setHeightForWidth(self.ViewAttendanceDateedit.sizePolicy().hasHeightForWidth())
        self.ViewAttendanceDateedit.setSizePolicy(sizePolicy5)
        self.ViewAttendanceDateedit.setCalendarPopup(True)

        self.gridLayout_18.addWidget(self.ViewAttendanceDateedit, 1, 0, 1, 1)

        self.viewAttendanceBtn = QPushButton(self.frame_162)
        self.viewAttendanceBtn.setObjectName(u"viewAttendanceBtn")

        self.gridLayout_18.addWidget(self.viewAttendanceBtn, 2, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.ViewDatepopupPushButton = QPushButton(self.frame_162)
        self.ViewDatepopupPushButton.setObjectName(u"ViewDatepopupPushButton")
        self.ViewDatepopupPushButton.setStyleSheet(u"border: none;\n"
"background-color:none;")
        icon6 = QIcon()
        icon6.addFile(u":/skyblue_icons/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ViewDatepopupPushButton.setIcon(icon6)

        self.gridLayout_18.addWidget(self.ViewDatepopupPushButton, 1, 1, 1, 1)


        self.horizontalLayout_76.addWidget(self.frame_162)


        self.verticalLayout_71.addWidget(self.frame_161)


        self.horizontalLayout_74.addWidget(self.frame_159)

        self.frame_163 = QFrame(self.frame_158)
        self.frame_163.setObjectName(u"frame_163")
        sizePolicy.setHeightForWidth(self.frame_163.sizePolicy().hasHeightForWidth())
        self.frame_163.setSizePolicy(sizePolicy)
        self.frame_163.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_163.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_74.addWidget(self.frame_163)


        self.verticalLayout_75.addWidget(self.frame_158)

        self.frame_164 = QFrame(self.View_class_attendance_page)
        self.frame_164.setObjectName(u"frame_164")
        sizePolicy1.setHeightForWidth(self.frame_164.sizePolicy().hasHeightForWidth())
        self.frame_164.setSizePolicy(sizePolicy1)
        self.frame_164.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_164.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_164)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.frame_165 = QFrame(self.frame_164)
        self.frame_165.setObjectName(u"frame_165")
        self.frame_165.setStyleSheet(u"QLabel{\n"
"	font-size: 14px;\n"
"	color: #333;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"")
        self.frame_165.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_165.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_165)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.frame_166 = QFrame(self.frame_165)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setMinimumSize(QSize(208, 0))
        self.frame_166.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_166.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_166)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, -1)
        self.label_145 = QLabel(self.frame_166)
        self.label_145.setObjectName(u"label_145")

        self.verticalLayout_73.addWidget(self.label_145)

        self.label_146 = QLabel(self.frame_166)
        self.label_146.setObjectName(u"label_146")

        self.verticalLayout_73.addWidget(self.label_146)

        self.showClassAttendanceEnrtiesspinBox = QSpinBox(self.frame_166)
        self.showClassAttendanceEnrtiesspinBox.setObjectName(u"showClassAttendanceEnrtiesspinBox")
        self.showClassAttendanceEnrtiesspinBox.setMinimumSize(QSize(200, 0))
        self.showClassAttendanceEnrtiesspinBox.setStyleSheet(u"padding: 6px;\n"
"color: #333;\n"
"background-color: #f0f0f0;")

        self.verticalLayout_73.addWidget(self.showClassAttendanceEnrtiesspinBox)

        self.label_147 = QLabel(self.frame_166)
        self.label_147.setObjectName(u"label_147")

        self.verticalLayout_73.addWidget(self.label_147)


        self.horizontalLayout_77.addWidget(self.frame_166)

        self.frame_167 = QFrame(self.frame_165)
        self.frame_167.setObjectName(u"frame_167")
        sizePolicy.setHeightForWidth(self.frame_167.sizePolicy().hasHeightForWidth())
        self.frame_167.setSizePolicy(sizePolicy)
        self.frame_167.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_167.setFrameShadow(QFrame.Shadow.Raised)
        self.label_148 = QLabel(self.frame_167)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setGeometry(QRect(320, 100, 323, 75))

        self.horizontalLayout_77.addWidget(self.frame_167)

        self.frame_168 = QFrame(self.frame_165)
        self.frame_168.setObjectName(u"frame_168")
        self.frame_168.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_168.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_168)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 9)
        self.view_class_attendance_search_btn = QPushButton(self.frame_168)
        self.view_class_attendance_search_btn.setObjectName(u"view_class_attendance_search_btn")
        self.view_class_attendance_search_btn.setIcon(icon3)

        self.gridLayout_21.addWidget(self.view_class_attendance_search_btn, 1, 1, 1, 1)

        self.label_149 = QLabel(self.frame_168)
        self.label_149.setObjectName(u"label_149")

        self.gridLayout_21.addWidget(self.label_149, 0, 0, 1, 1)

        self.view_classattendance_search_entry = QLineEdit(self.frame_168)
        self.view_classattendance_search_entry.setObjectName(u"view_classattendance_search_entry")

        self.gridLayout_21.addWidget(self.view_classattendance_search_entry, 1, 0, 1, 1)


        self.horizontalLayout_77.addWidget(self.frame_168)


        self.verticalLayout_72.addWidget(self.frame_165)

        self.showclassCoursesTableFrame_3 = QFrame(self.frame_164)
        self.showclassCoursesTableFrame_3.setObjectName(u"showclassCoursesTableFrame_3")
        sizePolicy1.setHeightForWidth(self.showclassCoursesTableFrame_3.sizePolicy().hasHeightForWidth())
        self.showclassCoursesTableFrame_3.setSizePolicy(sizePolicy1)
        self.showclassCoursesTableFrame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.showclassCoursesTableFrame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_22 = QGridLayout(self.showclassCoursesTableFrame_3)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setVerticalSpacing(4)
        self.gridLayout_22.setContentsMargins(-1, 3, -1, 4)
        self.ClassCoursestableTitlewrowwidget_6 = QWidget(self.showclassCoursesTableFrame_3)
        self.ClassCoursestableTitlewrowwidget_6.setObjectName(u"ClassCoursestableTitlewrowwidget_6")
        sizePolicy4.setHeightForWidth(self.ClassCoursestableTitlewrowwidget_6.sizePolicy().hasHeightForWidth())
        self.ClassCoursestableTitlewrowwidget_6.setSizePolicy(sizePolicy4)
        self.ClassCoursestableTitlewrowwidget_6.setMinimumSize(QSize(0, 50))
        self.ClassCoursestableTitlewrowwidget_6.setMaximumSize(QSize(16777215, 50))
        self.ClassCoursestableTitlewrowwidget_6.setStyleSheet(u"background-color:rgb(205, 243, 255)")
        self.horizontalLayout_78 = QHBoxLayout(self.ClassCoursestableTitlewrowwidget_6)
        self.horizontalLayout_78.setSpacing(9)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(9, -1, 9, 9)
        self.label_151 = QLabel(self.ClassCoursestableTitlewrowwidget_6)
        self.label_151.setObjectName(u"label_151")

        self.horizontalLayout_78.addWidget(self.label_151)

        self.label_152 = QLabel(self.ClassCoursestableTitlewrowwidget_6)
        self.label_152.setObjectName(u"label_152")

        self.horizontalLayout_78.addWidget(self.label_152)

        self.label_153 = QLabel(self.ClassCoursestableTitlewrowwidget_6)
        self.label_153.setObjectName(u"label_153")

        self.horizontalLayout_78.addWidget(self.label_153)

        self.label_154 = QLabel(self.ClassCoursestableTitlewrowwidget_6)
        self.label_154.setObjectName(u"label_154")

        self.horizontalLayout_78.addWidget(self.label_154)

        self.label_155 = QLabel(self.ClassCoursestableTitlewrowwidget_6)
        self.label_155.setObjectName(u"label_155")

        self.horizontalLayout_78.addWidget(self.label_155)

        self.label_156 = QLabel(self.ClassCoursestableTitlewrowwidget_6)
        self.label_156.setObjectName(u"label_156")

        self.horizontalLayout_78.addWidget(self.label_156)

        self.label_144 = QLabel(self.ClassCoursestableTitlewrowwidget_6)
        self.label_144.setObjectName(u"label_144")

        self.horizontalLayout_78.addWidget(self.label_144)

        self.label_150 = QLabel(self.ClassCoursestableTitlewrowwidget_6)
        self.label_150.setObjectName(u"label_150")

        self.horizontalLayout_78.addWidget(self.label_150)

        self.label_157 = QLabel(self.ClassCoursestableTitlewrowwidget_6)
        self.label_157.setObjectName(u"label_157")

        self.horizontalLayout_78.addWidget(self.label_157)

        self.label_158 = QLabel(self.ClassCoursestableTitlewrowwidget_6)
        self.label_158.setObjectName(u"label_158")

        self.horizontalLayout_78.addWidget(self.label_158)

        self.label_159 = QLabel(self.ClassCoursestableTitlewrowwidget_6)
        self.label_159.setObjectName(u"label_159")

        self.horizontalLayout_78.addWidget(self.label_159)


        self.gridLayout_22.addWidget(self.ClassCoursestableTitlewrowwidget_6, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_72.addWidget(self.showclassCoursesTableFrame_3)

        self.frame_169 = QFrame(self.frame_164)
        self.frame_169.setObjectName(u"frame_169")
        self.frame_169.setStyleSheet(u"QLabel{\n"
"	font-size: 12px;\n"
"	color: #666;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: darkgrey;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}")
        self.frame_169.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_169.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_169)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.frame_170 = QFrame(self.frame_169)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_170.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_170)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.classAttendancePageNumber_label = QLabel(self.frame_170)
        self.classAttendancePageNumber_label.setObjectName(u"classAttendancePageNumber_label")

        self.verticalLayout_74.addWidget(self.classAttendancePageNumber_label)


        self.horizontalLayout_79.addWidget(self.frame_170, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_171 = QFrame(self.frame_169)
        self.frame_171.setObjectName(u"frame_171")
        sizePolicy.setHeightForWidth(self.frame_171.sizePolicy().hasHeightForWidth())
        self.frame_171.setSizePolicy(sizePolicy)
        self.frame_171.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_171.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_79.addWidget(self.frame_171)

        self.frame_172 = QFrame(self.frame_169)
        self.frame_172.setObjectName(u"frame_172")
        self.frame_172.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_172.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_172)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.view_class_attendance_preview_btn = QPushButton(self.frame_172)
        self.view_class_attendance_preview_btn.setObjectName(u"view_class_attendance_preview_btn")
        self.view_class_attendance_preview_btn.setIcon(icon4)

        self.horizontalLayout_80.addWidget(self.view_class_attendance_preview_btn)

        self.current_class_attendance_page_label = QLabel(self.frame_172)
        self.current_class_attendance_page_label.setObjectName(u"current_class_attendance_page_label")

        self.horizontalLayout_80.addWidget(self.current_class_attendance_page_label)

        self.view_class_attendance_next_btn = QPushButton(self.frame_172)
        self.view_class_attendance_next_btn.setObjectName(u"view_class_attendance_next_btn")
        self.view_class_attendance_next_btn.setIcon(icon5)

        self.horizontalLayout_80.addWidget(self.view_class_attendance_next_btn)


        self.horizontalLayout_79.addWidget(self.frame_172, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_173 = QFrame(self.frame_169)
        self.frame_173.setObjectName(u"frame_173")
        sizePolicy.setHeightForWidth(self.frame_173.sizePolicy().hasHeightForWidth())
        self.frame_173.setSizePolicy(sizePolicy)
        self.frame_173.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_173.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_79.addWidget(self.frame_173)


        self.verticalLayout_72.addWidget(self.frame_169, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_75.addWidget(self.frame_164)

        self.MainStackedWidget.addWidget(self.View_class_attendance_page)
        self.View_student_attendance_page = QWidget()
        self.View_student_attendance_page.setObjectName(u"View_student_attendance_page")
        sizePolicy1.setHeightForWidth(self.View_student_attendance_page.sizePolicy().hasHeightForWidth())
        self.View_student_attendance_page.setSizePolicy(sizePolicy1)
        self.verticalLayout_81 = QVBoxLayout(self.View_student_attendance_page)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.frame_174 = QFrame(self.View_student_attendance_page)
        self.frame_174.setObjectName(u"frame_174")
        self.frame_174.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_174.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_174)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.frame_175 = QFrame(self.frame_174)
        self.frame_175.setObjectName(u"frame_175")
        self.frame_175.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_175.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_175)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_160 = QLabel(self.frame_175)
        self.label_160.setObjectName(u"label_160")

        self.verticalLayout_76.addWidget(self.label_160, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_81.addWidget(self.frame_175)

        self.frame_176 = QFrame(self.frame_174)
        self.frame_176.setObjectName(u"frame_176")
        sizePolicy.setHeightForWidth(self.frame_176.sizePolicy().hasHeightForWidth())
        self.frame_176.setSizePolicy(sizePolicy)
        self.frame_176.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_176.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_81.addWidget(self.frame_176)

        self.frame_177 = QFrame(self.frame_174)
        self.frame_177.setObjectName(u"frame_177")
        self.frame_177.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_177.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_177)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.goHome_button_9 = QPushButton(self.frame_177)
        self.goHome_button_9.setObjectName(u"goHome_button_9")
        self.goHome_button_9.setFont(font)
        self.goHome_button_9.setStyleSheet(u"border:none;\n"
"background-color:none;")

        self.horizontalLayout_82.addWidget(self.goHome_button_9)

        self.label_161 = QLabel(self.frame_177)
        self.label_161.setObjectName(u"label_161")

        self.horizontalLayout_82.addWidget(self.label_161)


        self.horizontalLayout_81.addWidget(self.frame_177)


        self.verticalLayout_81.addWidget(self.frame_174)

        self.frame_178 = QFrame(self.View_student_attendance_page)
        self.frame_178.setObjectName(u"frame_178")
        self.frame_178.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_178.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_178)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.frame_179 = QFrame(self.frame_178)
        self.frame_179.setObjectName(u"frame_179")
        self.frame_179.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_179.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_179)
        self.verticalLayout_77.setSpacing(4)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.frame_180 = QFrame(self.frame_179)
        self.frame_180.setObjectName(u"frame_180")
        self.frame_180.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_180.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_180)
        self.horizontalLayout_84.setSpacing(0)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.label_162 = QLabel(self.frame_180)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setStyleSheet(u"color:skyblue;")

        self.horizontalLayout_84.addWidget(self.label_162)


        self.verticalLayout_77.addWidget(self.frame_180)

        self.verticalSpacer_16 = QSpacerItem(20, 14, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_77.addItem(self.verticalSpacer_16)

        self.frame_181 = QFrame(self.frame_179)
        self.frame_181.setObjectName(u"frame_181")
        self.frame_181.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_181)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.frame_182 = QFrame(self.frame_181)
        self.frame_182.setObjectName(u"frame_182")
        self.frame_182.setStyleSheet(u"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #5cacee;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #4caf50;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}QLineEdit:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #5cacee;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border-color: #5cacee;\n"
"}")
        self.frame_182.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_182.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_182)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_163 = QLabel(self.frame_182)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setStyleSheet(u"color:rgb(93, 93, 93);\n"
"")

        self.gridLayout_23.addWidget(self.label_163, 0, 0, 1, 1)

        self.viewStudentAttendanceBtn = QPushButton(self.frame_182)
        self.viewStudentAttendanceBtn.setObjectName(u"viewStudentAttendanceBtn")

        self.gridLayout_23.addWidget(self.viewStudentAttendanceBtn, 2, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.StudentscomboBox = QComboBox(self.frame_182)
        self.StudentscomboBox.setObjectName(u"StudentscomboBox")
        sizePolicy5.setHeightForWidth(self.StudentscomboBox.sizePolicy().hasHeightForWidth())
        self.StudentscomboBox.setSizePolicy(sizePolicy5)

        self.gridLayout_23.addWidget(self.StudentscomboBox, 1, 0, 1, 1)


        self.horizontalLayout_85.addWidget(self.frame_182)


        self.verticalLayout_77.addWidget(self.frame_181)


        self.horizontalLayout_83.addWidget(self.frame_179)

        self.frame_183 = QFrame(self.frame_178)
        self.frame_183.setObjectName(u"frame_183")
        sizePolicy.setHeightForWidth(self.frame_183.sizePolicy().hasHeightForWidth())
        self.frame_183.setSizePolicy(sizePolicy)
        self.frame_183.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_183.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_83.addWidget(self.frame_183)


        self.verticalLayout_81.addWidget(self.frame_178)

        self.frame_184 = QFrame(self.View_student_attendance_page)
        self.frame_184.setObjectName(u"frame_184")
        sizePolicy1.setHeightForWidth(self.frame_184.sizePolicy().hasHeightForWidth())
        self.frame_184.setSizePolicy(sizePolicy1)
        self.frame_184.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_184)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.frame_185 = QFrame(self.frame_184)
        self.frame_185.setObjectName(u"frame_185")
        self.frame_185.setStyleSheet(u"QLabel{\n"
"	font-size: 14px;\n"
"	color: #333;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"")
        self.frame_185.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_185.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_185)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.frame_186 = QFrame(self.frame_185)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setMinimumSize(QSize(208, 0))
        self.frame_186.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_186.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_186)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, -1)
        self.label_164 = QLabel(self.frame_186)
        self.label_164.setObjectName(u"label_164")

        self.verticalLayout_79.addWidget(self.label_164)

        self.label_165 = QLabel(self.frame_186)
        self.label_165.setObjectName(u"label_165")

        self.verticalLayout_79.addWidget(self.label_165)

        self.showStudentAttendanceEnrtiesspinBox = QSpinBox(self.frame_186)
        self.showStudentAttendanceEnrtiesspinBox.setObjectName(u"showStudentAttendanceEnrtiesspinBox")
        self.showStudentAttendanceEnrtiesspinBox.setMinimumSize(QSize(200, 0))
        self.showStudentAttendanceEnrtiesspinBox.setStyleSheet(u"padding: 6px;\n"
"color: #333;\n"
"background-color: #f0f0f0;")

        self.verticalLayout_79.addWidget(self.showStudentAttendanceEnrtiesspinBox)

        self.label_166 = QLabel(self.frame_186)
        self.label_166.setObjectName(u"label_166")

        self.verticalLayout_79.addWidget(self.label_166)


        self.horizontalLayout_86.addWidget(self.frame_186)

        self.frame_187 = QFrame(self.frame_185)
        self.frame_187.setObjectName(u"frame_187")
        sizePolicy.setHeightForWidth(self.frame_187.sizePolicy().hasHeightForWidth())
        self.frame_187.setSizePolicy(sizePolicy)
        self.frame_187.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_187.setFrameShadow(QFrame.Shadow.Raised)
        self.label_167 = QLabel(self.frame_187)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setGeometry(QRect(320, 100, 323, 75))

        self.horizontalLayout_86.addWidget(self.frame_187)


        self.verticalLayout_78.addWidget(self.frame_185)

        self.showclassCoursesTableFrame_4 = QFrame(self.frame_184)
        self.showclassCoursesTableFrame_4.setObjectName(u"showclassCoursesTableFrame_4")
        sizePolicy1.setHeightForWidth(self.showclassCoursesTableFrame_4.sizePolicy().hasHeightForWidth())
        self.showclassCoursesTableFrame_4.setSizePolicy(sizePolicy1)
        self.showclassCoursesTableFrame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.showclassCoursesTableFrame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_25 = QGridLayout(self.showclassCoursesTableFrame_4)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setVerticalSpacing(4)
        self.gridLayout_25.setContentsMargins(-1, 3, -1, 4)
        self.ClassCoursestableTitlewrowwidget_7 = QWidget(self.showclassCoursesTableFrame_4)
        self.ClassCoursestableTitlewrowwidget_7.setObjectName(u"ClassCoursestableTitlewrowwidget_7")
        sizePolicy4.setHeightForWidth(self.ClassCoursestableTitlewrowwidget_7.sizePolicy().hasHeightForWidth())
        self.ClassCoursestableTitlewrowwidget_7.setSizePolicy(sizePolicy4)
        self.ClassCoursestableTitlewrowwidget_7.setMinimumSize(QSize(0, 50))
        self.ClassCoursestableTitlewrowwidget_7.setMaximumSize(QSize(16777215, 50))
        self.ClassCoursestableTitlewrowwidget_7.setStyleSheet(u"background-color:rgb(205, 243, 255)")
        self.horizontalLayout_87 = QHBoxLayout(self.ClassCoursestableTitlewrowwidget_7)
        self.horizontalLayout_87.setSpacing(9)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(9, -1, 9, 9)
        self.label_169 = QLabel(self.ClassCoursestableTitlewrowwidget_7)
        self.label_169.setObjectName(u"label_169")

        self.horizontalLayout_87.addWidget(self.label_169)

        self.label_170 = QLabel(self.ClassCoursestableTitlewrowwidget_7)
        self.label_170.setObjectName(u"label_170")

        self.horizontalLayout_87.addWidget(self.label_170)

        self.label_171 = QLabel(self.ClassCoursestableTitlewrowwidget_7)
        self.label_171.setObjectName(u"label_171")

        self.horizontalLayout_87.addWidget(self.label_171)

        self.label_172 = QLabel(self.ClassCoursestableTitlewrowwidget_7)
        self.label_172.setObjectName(u"label_172")

        self.horizontalLayout_87.addWidget(self.label_172)

        self.label_173 = QLabel(self.ClassCoursestableTitlewrowwidget_7)
        self.label_173.setObjectName(u"label_173")

        self.horizontalLayout_87.addWidget(self.label_173)

        self.label_174 = QLabel(self.ClassCoursestableTitlewrowwidget_7)
        self.label_174.setObjectName(u"label_174")

        self.horizontalLayout_87.addWidget(self.label_174)

        self.label_175 = QLabel(self.ClassCoursestableTitlewrowwidget_7)
        self.label_175.setObjectName(u"label_175")

        self.horizontalLayout_87.addWidget(self.label_175)

        self.label_176 = QLabel(self.ClassCoursestableTitlewrowwidget_7)
        self.label_176.setObjectName(u"label_176")

        self.horizontalLayout_87.addWidget(self.label_176)

        self.label_177 = QLabel(self.ClassCoursestableTitlewrowwidget_7)
        self.label_177.setObjectName(u"label_177")

        self.horizontalLayout_87.addWidget(self.label_177)

        self.label_178 = QLabel(self.ClassCoursestableTitlewrowwidget_7)
        self.label_178.setObjectName(u"label_178")

        self.horizontalLayout_87.addWidget(self.label_178)

        self.label_179 = QLabel(self.ClassCoursestableTitlewrowwidget_7)
        self.label_179.setObjectName(u"label_179")

        self.horizontalLayout_87.addWidget(self.label_179)


        self.gridLayout_25.addWidget(self.ClassCoursestableTitlewrowwidget_7, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_78.addWidget(self.showclassCoursesTableFrame_4)

        self.frame_189 = QFrame(self.frame_184)
        self.frame_189.setObjectName(u"frame_189")
        self.frame_189.setStyleSheet(u"QLabel{\n"
"	font-size: 12px;\n"
"	color: #666;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: darkgrey;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}")
        self.frame_189.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_189)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.frame_190 = QFrame(self.frame_189)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_190.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_190)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.studentAttendancePageNumber_label = QLabel(self.frame_190)
        self.studentAttendancePageNumber_label.setObjectName(u"studentAttendancePageNumber_label")

        self.verticalLayout_80.addWidget(self.studentAttendancePageNumber_label)


        self.horizontalLayout_88.addWidget(self.frame_190, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_191 = QFrame(self.frame_189)
        self.frame_191.setObjectName(u"frame_191")
        sizePolicy.setHeightForWidth(self.frame_191.sizePolicy().hasHeightForWidth())
        self.frame_191.setSizePolicy(sizePolicy)
        self.frame_191.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_191.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_88.addWidget(self.frame_191)

        self.frame_192 = QFrame(self.frame_189)
        self.frame_192.setObjectName(u"frame_192")
        self.frame_192.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_192.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_192)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.view_student_attendance_preview_btn = QPushButton(self.frame_192)
        self.view_student_attendance_preview_btn.setObjectName(u"view_student_attendance_preview_btn")
        self.view_student_attendance_preview_btn.setIcon(icon4)

        self.horizontalLayout_89.addWidget(self.view_student_attendance_preview_btn)

        self.current_student_attendance_page_label = QLabel(self.frame_192)
        self.current_student_attendance_page_label.setObjectName(u"current_student_attendance_page_label")

        self.horizontalLayout_89.addWidget(self.current_student_attendance_page_label)

        self.view_student_attendance_next_btn = QPushButton(self.frame_192)
        self.view_student_attendance_next_btn.setObjectName(u"view_student_attendance_next_btn")
        self.view_student_attendance_next_btn.setIcon(icon5)

        self.horizontalLayout_89.addWidget(self.view_student_attendance_next_btn)


        self.horizontalLayout_88.addWidget(self.frame_192, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_193 = QFrame(self.frame_189)
        self.frame_193.setObjectName(u"frame_193")
        sizePolicy.setHeightForWidth(self.frame_193.sizePolicy().hasHeightForWidth())
        self.frame_193.setSizePolicy(sizePolicy)
        self.frame_193.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_193.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_88.addWidget(self.frame_193)


        self.verticalLayout_78.addWidget(self.frame_189, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_81.addWidget(self.frame_184)

        self.MainStackedWidget.addWidget(self.View_student_attendance_page)
        self.View_reports_page = QWidget()
        self.View_reports_page.setObjectName(u"View_reports_page")
        sizePolicy1.setHeightForWidth(self.View_reports_page.sizePolicy().hasHeightForWidth())
        self.View_reports_page.setSizePolicy(sizePolicy1)
        self.verticalLayout_87 = QVBoxLayout(self.View_reports_page)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.frame_188 = QFrame(self.View_reports_page)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_188.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_188)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.frame_194 = QFrame(self.frame_188)
        self.frame_194.setObjectName(u"frame_194")
        self.frame_194.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_194.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_194)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.label_168 = QLabel(self.frame_194)
        self.label_168.setObjectName(u"label_168")

        self.verticalLayout_82.addWidget(self.label_168, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_90.addWidget(self.frame_194)

        self.frame_195 = QFrame(self.frame_188)
        self.frame_195.setObjectName(u"frame_195")
        sizePolicy.setHeightForWidth(self.frame_195.sizePolicy().hasHeightForWidth())
        self.frame_195.setSizePolicy(sizePolicy)
        self.frame_195.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_195.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_90.addWidget(self.frame_195)

        self.frame_196 = QFrame(self.frame_188)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_196.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_196)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.goHome_button_10 = QPushButton(self.frame_196)
        self.goHome_button_10.setObjectName(u"goHome_button_10")
        self.goHome_button_10.setFont(font)
        self.goHome_button_10.setStyleSheet(u"border:none;\n"
"background-color:none;")

        self.horizontalLayout_91.addWidget(self.goHome_button_10)

        self.label_180 = QLabel(self.frame_196)
        self.label_180.setObjectName(u"label_180")

        self.horizontalLayout_91.addWidget(self.label_180)


        self.horizontalLayout_90.addWidget(self.frame_196)


        self.verticalLayout_87.addWidget(self.frame_188)

        self.frame_197 = QFrame(self.View_reports_page)
        self.frame_197.setObjectName(u"frame_197")
        self.frame_197.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_197.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_197)
        self.horizontalLayout_92.setSpacing(0)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.frame_198 = QFrame(self.frame_197)
        self.frame_198.setObjectName(u"frame_198")
        self.frame_198.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_198.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_198)
        self.verticalLayout_83.setSpacing(4)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.frame_199 = QFrame(self.frame_198)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_199.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_199)
        self.horizontalLayout_93.setSpacing(0)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.label_181 = QLabel(self.frame_199)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setStyleSheet(u"color:skyblue;")

        self.horizontalLayout_93.addWidget(self.label_181)


        self.verticalLayout_83.addWidget(self.frame_199)

        self.verticalSpacer_17 = QSpacerItem(20, 14, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_83.addItem(self.verticalSpacer_17)

        self.frame_200 = QFrame(self.frame_198)
        self.frame_200.setObjectName(u"frame_200")
        self.frame_200.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_200.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_200)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.frame_201 = QFrame(self.frame_200)
        self.frame_201.setObjectName(u"frame_201")
        self.frame_201.setStyleSheet(u"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #5cacee;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #4caf50;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}QLineEdit:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #5cacee;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border-color: #aaa;\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border-color: #5cacee;\n"
"}")
        self.frame_201.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_201.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_201)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.ViewSecurityAttendanceDateedit = QDateEdit(self.frame_201)
        self.ViewSecurityAttendanceDateedit.setObjectName(u"ViewSecurityAttendanceDateedit")
        sizePolicy5.setHeightForWidth(self.ViewSecurityAttendanceDateedit.sizePolicy().hasHeightForWidth())
        self.ViewSecurityAttendanceDateedit.setSizePolicy(sizePolicy5)
        self.ViewSecurityAttendanceDateedit.setCalendarPopup(True)

        self.gridLayout_24.addWidget(self.ViewSecurityAttendanceDateedit, 1, 0, 1, 1)

        self.label_182 = QLabel(self.frame_201)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setStyleSheet(u"color:rgb(93, 93, 93);\n"
"")

        self.gridLayout_24.addWidget(self.label_182, 0, 0, 1, 1)

        self.ViewSecurityDatepopupPushButton = QPushButton(self.frame_201)
        self.ViewSecurityDatepopupPushButton.setObjectName(u"ViewSecurityDatepopupPushButton")
        self.ViewSecurityDatepopupPushButton.setStyleSheet(u"border: none;\n"
"background-color:none;")
        self.ViewSecurityDatepopupPushButton.setIcon(icon6)

        self.gridLayout_24.addWidget(self.ViewSecurityDatepopupPushButton, 1, 1, 1, 1)

        self.viewSecurityAttendanceBtn = QPushButton(self.frame_201)
        self.viewSecurityAttendanceBtn.setObjectName(u"viewSecurityAttendanceBtn")

        self.gridLayout_24.addWidget(self.viewSecurityAttendanceBtn, 2, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_94.addWidget(self.frame_201)


        self.verticalLayout_83.addWidget(self.frame_200)


        self.horizontalLayout_92.addWidget(self.frame_198)

        self.frame_202 = QFrame(self.frame_197)
        self.frame_202.setObjectName(u"frame_202")
        sizePolicy.setHeightForWidth(self.frame_202.sizePolicy().hasHeightForWidth())
        self.frame_202.setSizePolicy(sizePolicy)
        self.frame_202.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_202.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_92.addWidget(self.frame_202)


        self.verticalLayout_87.addWidget(self.frame_197)

        self.frame_203 = QFrame(self.View_reports_page)
        self.frame_203.setObjectName(u"frame_203")
        sizePolicy1.setHeightForWidth(self.frame_203.sizePolicy().hasHeightForWidth())
        self.frame_203.setSizePolicy(sizePolicy1)
        self.frame_203.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_203.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_203)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.frame_204 = QFrame(self.frame_203)
        self.frame_204.setObjectName(u"frame_204")
        self.frame_204.setStyleSheet(u"QLabel{\n"
"	font-size: 14px;\n"
"	color: #333;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: #f0f0f0;\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 5px;\n"
"	padding: 6px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	border: 1px solid #4caf50;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}\n"
"")
        self.frame_204.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_204.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_204)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.frame_205 = QFrame(self.frame_204)
        self.frame_205.setObjectName(u"frame_205")
        self.frame_205.setMinimumSize(QSize(208, 0))
        self.frame_205.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_205.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_205)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, -1)
        self.label_183 = QLabel(self.frame_205)
        self.label_183.setObjectName(u"label_183")

        self.verticalLayout_85.addWidget(self.label_183)

        self.label_184 = QLabel(self.frame_205)
        self.label_184.setObjectName(u"label_184")

        self.verticalLayout_85.addWidget(self.label_184)

        self.showSecurityAttendanceEnrtiesspinBox = QSpinBox(self.frame_205)
        self.showSecurityAttendanceEnrtiesspinBox.setObjectName(u"showSecurityAttendanceEnrtiesspinBox")
        self.showSecurityAttendanceEnrtiesspinBox.setMinimumSize(QSize(200, 0))
        self.showSecurityAttendanceEnrtiesspinBox.setStyleSheet(u"padding: 6px;\n"
"color: #333;\n"
"background-color: #f0f0f0;")

        self.verticalLayout_85.addWidget(self.showSecurityAttendanceEnrtiesspinBox)

        self.label_185 = QLabel(self.frame_205)
        self.label_185.setObjectName(u"label_185")

        self.verticalLayout_85.addWidget(self.label_185)


        self.horizontalLayout_95.addWidget(self.frame_205)

        self.frame_206 = QFrame(self.frame_204)
        self.frame_206.setObjectName(u"frame_206")
        sizePolicy.setHeightForWidth(self.frame_206.sizePolicy().hasHeightForWidth())
        self.frame_206.setSizePolicy(sizePolicy)
        self.frame_206.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_206.setFrameShadow(QFrame.Shadow.Raised)
        self.label_186 = QLabel(self.frame_206)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setGeometry(QRect(320, 100, 323, 75))

        self.horizontalLayout_95.addWidget(self.frame_206)

        self.frame_207 = QFrame(self.frame_204)
        self.frame_207.setObjectName(u"frame_207")
        self.frame_207.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_207.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_207)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 9)
        self.view_security_attendance_search_btn = QPushButton(self.frame_207)
        self.view_security_attendance_search_btn.setObjectName(u"view_security_attendance_search_btn")
        self.view_security_attendance_search_btn.setIcon(icon3)

        self.gridLayout_26.addWidget(self.view_security_attendance_search_btn, 1, 1, 1, 1)

        self.label_187 = QLabel(self.frame_207)
        self.label_187.setObjectName(u"label_187")

        self.gridLayout_26.addWidget(self.label_187, 0, 0, 1, 1)

        self.view_securityattendance_search_entry = QLineEdit(self.frame_207)
        self.view_securityattendance_search_entry.setObjectName(u"view_securityattendance_search_entry")

        self.gridLayout_26.addWidget(self.view_securityattendance_search_entry, 1, 0, 1, 1)


        self.horizontalLayout_95.addWidget(self.frame_207)


        self.verticalLayout_84.addWidget(self.frame_204)

        self.showclassCoursesTableFrame_5 = QFrame(self.frame_203)
        self.showclassCoursesTableFrame_5.setObjectName(u"showclassCoursesTableFrame_5")
        sizePolicy1.setHeightForWidth(self.showclassCoursesTableFrame_5.sizePolicy().hasHeightForWidth())
        self.showclassCoursesTableFrame_5.setSizePolicy(sizePolicy1)
        self.showclassCoursesTableFrame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.showclassCoursesTableFrame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_27 = QGridLayout(self.showclassCoursesTableFrame_5)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setVerticalSpacing(4)
        self.gridLayout_27.setContentsMargins(-1, 3, -1, 4)
        self.ClassCoursestableTitlewrowwidget_8 = QWidget(self.showclassCoursesTableFrame_5)
        self.ClassCoursestableTitlewrowwidget_8.setObjectName(u"ClassCoursestableTitlewrowwidget_8")
        sizePolicy4.setHeightForWidth(self.ClassCoursestableTitlewrowwidget_8.sizePolicy().hasHeightForWidth())
        self.ClassCoursestableTitlewrowwidget_8.setSizePolicy(sizePolicy4)
        self.ClassCoursestableTitlewrowwidget_8.setMinimumSize(QSize(0, 50))
        self.ClassCoursestableTitlewrowwidget_8.setMaximumSize(QSize(16777215, 50))
        self.ClassCoursestableTitlewrowwidget_8.setStyleSheet(u"background-color:rgb(205, 243, 255)")
        self.horizontalLayout_96 = QHBoxLayout(self.ClassCoursestableTitlewrowwidget_8)
        self.horizontalLayout_96.setSpacing(9)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(9, -1, 9, 9)
        self.label_188 = QLabel(self.ClassCoursestableTitlewrowwidget_8)
        self.label_188.setObjectName(u"label_188")

        self.horizontalLayout_96.addWidget(self.label_188)

        self.label_189 = QLabel(self.ClassCoursestableTitlewrowwidget_8)
        self.label_189.setObjectName(u"label_189")

        self.horizontalLayout_96.addWidget(self.label_189)

        self.label_190 = QLabel(self.ClassCoursestableTitlewrowwidget_8)
        self.label_190.setObjectName(u"label_190")

        self.horizontalLayout_96.addWidget(self.label_190)

        self.label_191 = QLabel(self.ClassCoursestableTitlewrowwidget_8)
        self.label_191.setObjectName(u"label_191")

        self.horizontalLayout_96.addWidget(self.label_191)

        self.label_192 = QLabel(self.ClassCoursestableTitlewrowwidget_8)
        self.label_192.setObjectName(u"label_192")

        self.horizontalLayout_96.addWidget(self.label_192)

        self.label_193 = QLabel(self.ClassCoursestableTitlewrowwidget_8)
        self.label_193.setObjectName(u"label_193")

        self.horizontalLayout_96.addWidget(self.label_193)

        self.label_197 = QLabel(self.ClassCoursestableTitlewrowwidget_8)
        self.label_197.setObjectName(u"label_197")

        self.horizontalLayout_96.addWidget(self.label_197)

        self.label_198 = QLabel(self.ClassCoursestableTitlewrowwidget_8)
        self.label_198.setObjectName(u"label_198")

        self.horizontalLayout_96.addWidget(self.label_198)


        self.gridLayout_27.addWidget(self.ClassCoursestableTitlewrowwidget_8, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_84.addWidget(self.showclassCoursesTableFrame_5)

        self.frame_208 = QFrame(self.frame_203)
        self.frame_208.setObjectName(u"frame_208")
        self.frame_208.setStyleSheet(u"QLabel{\n"
"	font-size: 12px;\n"
"	color: #666;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: darkgrey;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	padding: 8px 16px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #45a049;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #3e8e41;\n"
"}")
        self.frame_208.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_208.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_208)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.frame_209 = QFrame(self.frame_208)
        self.frame_209.setObjectName(u"frame_209")
        self.frame_209.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_209.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_209)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.securityAttendancePageNumber_label = QLabel(self.frame_209)
        self.securityAttendancePageNumber_label.setObjectName(u"securityAttendancePageNumber_label")

        self.verticalLayout_86.addWidget(self.securityAttendancePageNumber_label)


        self.horizontalLayout_97.addWidget(self.frame_209, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_210 = QFrame(self.frame_208)
        self.frame_210.setObjectName(u"frame_210")
        sizePolicy.setHeightForWidth(self.frame_210.sizePolicy().hasHeightForWidth())
        self.frame_210.setSizePolicy(sizePolicy)
        self.frame_210.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_210.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_97.addWidget(self.frame_210)

        self.frame_211 = QFrame(self.frame_208)
        self.frame_211.setObjectName(u"frame_211")
        self.frame_211.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_211.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.frame_211)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.view_security_attendance_preview_btn = QPushButton(self.frame_211)
        self.view_security_attendance_preview_btn.setObjectName(u"view_security_attendance_preview_btn")
        self.view_security_attendance_preview_btn.setIcon(icon4)

        self.horizontalLayout_98.addWidget(self.view_security_attendance_preview_btn)

        self.current_security_attendance_page_label = QLabel(self.frame_211)
        self.current_security_attendance_page_label.setObjectName(u"current_security_attendance_page_label")

        self.horizontalLayout_98.addWidget(self.current_security_attendance_page_label)

        self.view_security_attendance_next_btn = QPushButton(self.frame_211)
        self.view_security_attendance_next_btn.setObjectName(u"view_security_attendance_next_btn")
        self.view_security_attendance_next_btn.setIcon(icon5)

        self.horizontalLayout_98.addWidget(self.view_security_attendance_next_btn)


        self.horizontalLayout_97.addWidget(self.frame_211, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_212 = QFrame(self.frame_208)
        self.frame_212.setObjectName(u"frame_212")
        sizePolicy.setHeightForWidth(self.frame_212.sizePolicy().hasHeightForWidth())
        self.frame_212.setSizePolicy(sizePolicy)
        self.frame_212.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_212.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_97.addWidget(self.frame_212)


        self.verticalLayout_84.addWidget(self.frame_208, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_87.addWidget(self.frame_203)

        self.MainStackedWidget.addWidget(self.View_reports_page)
        self.Dashboard_page = QWidget()
        self.Dashboard_page.setObjectName(u"Dashboard_page")
        sizePolicy1.setHeightForWidth(self.Dashboard_page.sizePolicy().hasHeightForWidth())
        self.Dashboard_page.setSizePolicy(sizePolicy1)
        self.verticalLayout_12 = QVBoxLayout(self.Dashboard_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.admin_dashboardLBframe = QFrame(self.Dashboard_page)
        self.admin_dashboardLBframe.setObjectName(u"admin_dashboardLBframe")
        self.admin_dashboardLBframe.setStyleSheet(u"")
        self.admin_dashboardLBframe.setFrameShape(QFrame.Shape.NoFrame)
        self.admin_dashboardLBframe.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.admin_dashboardLBframe)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_8 = QFrame(self.admin_dashboardLBframe)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_13.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_7.addWidget(self.frame_8, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.frame_9 = QFrame(self.admin_dashboardLBframe)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_7.addWidget(self.frame_9)

        self.admin_home_btn_frame = QFrame(self.admin_dashboardLBframe)
        self.admin_home_btn_frame.setObjectName(u"admin_home_btn_frame")
        self.admin_home_btn_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.admin_home_btn_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.admin_home_btn_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.goHome_button = QPushButton(self.admin_home_btn_frame)
        self.goHome_button.setObjectName(u"goHome_button")
        self.goHome_button.setFont(font)
        self.goHome_button.setStyleSheet(u"border:none;\n"
"background-color:none;")

        self.horizontalLayout_8.addWidget(self.goHome_button)

        self.label_10 = QLabel(self.admin_home_btn_frame)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)


        self.horizontalLayout_7.addWidget(self.admin_home_btn_frame, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_12.addWidget(self.admin_dashboardLBframe, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_6 = QWidget(self.Dashboard_page)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.widget_6.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(45)
        self.gridLayout.setVerticalSpacing(31)
        self.widget6_frame = QFrame(self.widget_6)
        self.widget6_frame.setObjectName(u"widget6_frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget6_frame.sizePolicy().hasHeightForWidth())
        self.widget6_frame.setSizePolicy(sizePolicy6)
        self.widget6_frame.setMinimumSize(QSize(300, 100))
        self.widget6_frame.setMaximumSize(QSize(300, 100))
        self.widget6_frame.setStyleSheet(u"background-color:white;")
        self.widget6_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.widget6_frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.widget6_frame.setLineWidth(1)
        self.horizontalLayout_9 = QHBoxLayout(self.widget6_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(4, 8, 4, 9)
        self.frame_11 = QFrame(self.widget6_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"border:none;")
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setSpacing(4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_11)
        self.label_11.setObjectName(u"label_11")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_11.setFont(font2)

        self.verticalLayout_15.addWidget(self.label_11)

        self.student_number_lbl = QLabel(self.frame_11)
        self.student_number_lbl.setObjectName(u"student_number_lbl")

        self.verticalLayout_15.addWidget(self.student_number_lbl, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_9.addWidget(self.frame_11, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.frame_12 = QFrame(self.widget6_frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"border:none;")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, -1, 0)
        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 0))
        self.label_13.setPixmap(QPixmap(u":/skyblue_icons/users.svg"))
        self.label_13.setScaledContents(False)

        self.verticalLayout_14.addWidget(self.label_13)


        self.horizontalLayout_9.addWidget(self.frame_12, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.gridLayout.addWidget(self.widget6_frame, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.frame_2 = QFrame(self.widget_6)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy6.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy6)
        self.frame_2.setMinimumSize(QSize(300, 100))
        self.frame_2.setMaximumSize(QSize(300, 100))
        self.frame_2.setStyleSheet(u"background-color:white;")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_13 = QFrame(self.frame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"border:none;")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_13)
        self.verticalLayout_16.setSpacing(4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.verticalLayout_16.addWidget(self.label_12, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.label_number_lbL = QLabel(self.frame_13)
        self.label_number_lbL.setObjectName(u"label_number_lbL")

        self.verticalLayout_16.addWidget(self.label_number_lbL, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_10.addWidget(self.frame_13, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.frame_14 = QFrame(self.frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"border:none;\n"
"")
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_14)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, -1, 0)
        self.label_14 = QLabel(self.frame_14)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 0))
        self.label_14.setPixmap(QPixmap(u":/skyblue_icons/users.svg"))
        self.label_14.setScaledContents(False)

        self.verticalLayout_17.addWidget(self.label_14, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_10.addWidget(self.frame_14, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.frame_3 = QFrame(self.widget_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(300, 100))
        self.frame_3.setMaximumSize(QSize(300, 100))
        self.frame_3.setStyleSheet(u"background-color:white;")
        self.horizontalLayout_11 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"border:none;\n"
"")
        self.frame_15.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_15)
        self.verticalLayout_18.setSpacing(4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.verticalLayout_18.addWidget(self.label_15, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.class_courses_number_lbl = QLabel(self.frame_15)
        self.class_courses_number_lbl.setObjectName(u"class_courses_number_lbl")

        self.verticalLayout_18.addWidget(self.class_courses_number_lbl, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_11.addWidget(self.frame_15, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.frame_16 = QFrame(self.frame_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"border:none;")
        self.frame_16.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_16)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, -1, 0)
        self.label_16 = QLabel(self.frame_16)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 0))
        self.label_16.setPixmap(QPixmap(u":/skyblue_icons/users.svg"))
        self.label_16.setScaledContents(False)

        self.verticalLayout_19.addWidget(self.label_16, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_11.addWidget(self.frame_16, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.gridLayout.addWidget(self.frame_3, 0, 2, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.frame_4 = QFrame(self.widget_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(300, 100))
        self.frame_4.setMaximumSize(QSize(300, 100))
        self.frame_4.setStyleSheet(u"background-color:white;")
        self.horizontalLayout_12 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_17 = QFrame(self.frame_4)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"border:none;")
        self.frame_17.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_17)
        self.verticalLayout_20.setSpacing(4)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_17)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.verticalLayout_20.addWidget(self.label_17, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.total_student_attendance_nbr_lbl = QLabel(self.frame_17)
        self.total_student_attendance_nbr_lbl.setObjectName(u"total_student_attendance_nbr_lbl")

        self.verticalLayout_20.addWidget(self.total_student_attendance_nbr_lbl, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_12.addWidget(self.frame_17, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.frame_18 = QFrame(self.frame_4)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"border:none;")
        self.frame_18.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_18)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, -1, 0)
        self.label_18 = QLabel(self.frame_18)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 0))
        self.label_18.setPixmap(QPixmap(u":/skyblue_icons/users.svg"))
        self.label_18.setScaledContents(False)

        self.verticalLayout_21.addWidget(self.label_18)


        self.horizontalLayout_12.addWidget(self.frame_18, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.gridLayout.addWidget(self.frame_4, 0, 3, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.frame_5 = QFrame(self.widget_6)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy6.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy6)
        self.frame_5.setMinimumSize(QSize(300, 100))
        self.frame_5.setMaximumSize(QSize(300, 100))
        self.frame_5.setStyleSheet(u"background-color:white;")
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_19 = QFrame(self.frame_5)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"border:none;")
        self.frame_19.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_19)
        self.verticalLayout_22.setSpacing(4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_19)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.verticalLayout_22.addWidget(self.label_19, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.class_teachers_nbr = QLabel(self.frame_19)
        self.class_teachers_nbr.setObjectName(u"class_teachers_nbr")

        self.verticalLayout_22.addWidget(self.class_teachers_nbr, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_13.addWidget(self.frame_19, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.frame_20 = QFrame(self.frame_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"border:none;")
        self.frame_20.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_20)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, -1, 0)
        self.label_20 = QLabel(self.frame_20)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setPixmap(QPixmap(u":/skyblue_icons/users.svg"))
        self.label_20.setScaledContents(False)

        self.verticalLayout_23.addWidget(self.label_20, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_13.addWidget(self.frame_20, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.frame_6 = QFrame(self.widget_6)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(30)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy7)
        self.frame_6.setMinimumSize(QSize(300, 100))
        self.frame_6.setMaximumSize(QSize(300, 100))
        self.frame_6.setStyleSheet(u"background-color:white;")
        self.horizontalLayout_14 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.middle_frame_21 = QFrame(self.frame_6)
        self.middle_frame_21.setObjectName(u"middle_frame_21")
        self.middle_frame_21.setStyleSheet(u"border:none;")
        self.middle_frame_21.setFrameShape(QFrame.Shape.NoFrame)
        self.middle_frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.middle_frame_21)
        self.verticalLayout_24.setSpacing(4)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.middle_frame_21)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)

        self.verticalLayout_24.addWidget(self.label_21, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.student_number_lbl_6 = QLabel(self.middle_frame_21)
        self.student_number_lbl_6.setObjectName(u"student_number_lbl_6")

        self.verticalLayout_24.addWidget(self.student_number_lbl_6, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_14.addWidget(self.middle_frame_21, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.frame_22 = QFrame(self.frame_6)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"border:none;")
        self.frame_22.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_22)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, -1, 0)
        self.label_22 = QLabel(self.frame_22)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 0))
        self.label_22.setPixmap(QPixmap(u":/skyblue_icons/users.svg"))
        self.label_22.setScaledContents(False)

        self.verticalLayout_25.addWidget(self.label_22, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_14.addWidget(self.frame_22, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.gridLayout.addWidget(self.frame_6, 1, 1, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.frame_7 = QFrame(self.widget_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy6.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy6)
        self.frame_7.setMinimumSize(QSize(300, 100))
        self.frame_7.setMaximumSize(QSize(300, 100))
        self.frame_7.setStyleSheet(u"background-color:white;")
        self.horizontalLayout_15 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_23 = QFrame(self.frame_7)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"border:none;\n"
"")
        self.frame_23.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_23)
        self.verticalLayout_26.setSpacing(4)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_23)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)

        self.verticalLayout_26.addWidget(self.label_23, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.student_number_lbl_7 = QLabel(self.frame_23)
        self.student_number_lbl_7.setObjectName(u"student_number_lbl_7")

        self.verticalLayout_26.addWidget(self.student_number_lbl_7, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_15.addWidget(self.frame_23, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.frame_24 = QFrame(self.frame_7)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"border:none;")
        self.frame_24.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_24)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, -1, 0)
        self.label_24 = QLabel(self.frame_24)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 0))
        self.label_24.setPixmap(QPixmap(u":/skyblue_icons/users.svg"))
        self.label_24.setScaledContents(False)

        self.verticalLayout_27.addWidget(self.label_24, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_15.addWidget(self.frame_24, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.gridLayout.addWidget(self.frame_7, 1, 2, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.widget6_frame.raise_()

        self.verticalLayout_12.addWidget(self.widget_6)

        self.MainStackedWidget.addWidget(self.Dashboard_page)

        self.horizontalLayout_6.addWidget(self.MainStackedWidget)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_5.addWidget(self.scrollArea_2)


        self.horizontalLayout_4.addWidget(self.principal_frame)


        self.verticalLayout.addWidget(self.MainFrame)

        self.FooterFrame = QFrame(self.centralwidget)
        self.FooterFrame.setObjectName(u"FooterFrame")
        self.FooterFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.FooterFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.FooterFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 2, 2, 2)
        self.copyright_label = QLabel(self.FooterFrame)
        self.copyright_label.setObjectName(u"copyright_label")

        self.horizontalLayout_3.addWidget(self.copyright_label, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.footer_extending_frame = QFrame(self.FooterFrame)
        self.footer_extending_frame.setObjectName(u"footer_extending_frame")
        sizePolicy.setHeightForWidth(self.footer_extending_frame.sizePolicy().hasHeightForWidth())
        self.footer_extending_frame.setSizePolicy(sizePolicy)
        self.footer_extending_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer_extending_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.footer_extending_frame, 0, Qt.AlignmentFlag.AlignBottom)

        self.qgriper = QWidget(self.FooterFrame)
        self.qgriper.setObjectName(u"qgriper")
        sizePolicy6.setHeightForWidth(self.qgriper.sizePolicy().hasHeightForWidth())
        self.qgriper.setSizePolicy(sizePolicy6)
        self.qgriper.setMinimumSize(QSize(20, 20))
        self.qgriper.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.qgriper, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.FooterFrame, 0, Qt.AlignmentFlag.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.menuButton, self.Create_course_btn)
        QWidget.setTabOrder(self.Create_course_btn, self.Create_teacher_btn)
        QWidget.setTabOrder(self.Create_teacher_btn, self.Create_Student_button)
        QWidget.setTabOrder(self.Create_Student_button, self.Create_class_btn)
        QWidget.setTabOrder(self.Create_class_btn, self.View_Student_m_button)
        QWidget.setTabOrder(self.View_Student_m_button, self.Take_attendance_btn)
        QWidget.setTabOrder(self.Take_attendance_btn, self.View_class_attendance_btn)
        QWidget.setTabOrder(self.View_class_attendance_btn, self.View_student_attendance_btn)
        QWidget.setTabOrder(self.View_student_attendance_btn, self.Today_attendance_report_btn)
        QWidget.setTabOrder(self.Today_attendance_report_btn, self.Create_Session_term_btn)
        QWidget.setTabOrder(self.Create_Session_term_btn, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.dashboardButton)
        QWidget.setTabOrder(self.dashboardButton, self.scrollArea_2)

        self.retranslateUi(MainWindow)
        self.ViewDatepopupPushButton.clicked.connect(self.ViewAttendanceDateedit.stepDown)

        self.MainStackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionUser_Manual.setText(QCoreApplication.translate("MainWindow", u"User Manual", None))
        self.actionAbout_2.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.actionChange_Password.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionEdit_Attendance.setText(QCoreApplication.translate("MainWindow", u"Edit Attendance", None))
        self.actionExport_Attendance_Report.setText(QCoreApplication.translate("MainWindow", u"Export Attendance Report", None))
        self.actionNew_Attendance_Session.setText(QCoreApplication.translate("MainWindow", u"New Attendance Session", None))
        self.actionOpen_Session.setText(QCoreApplication.translate("MainWindow", u"Open Session", None))
        self.actionSave_Sassion.setText(QCoreApplication.translate("MainWindow", u"Save Sassion", None))
        self.actionTake_Attendance_2.setText(QCoreApplication.translate("MainWindow", u"Take Gate Attendance", None))
        self.actionView_Attendance_Report_2.setText(QCoreApplication.translate("MainWindow", u"View Gate Attendance", None))
        self.actionTake_Employee_Attendance.setText(QCoreApplication.translate("MainWindow", u"Take Employee Attendance", None))
        self.actionView_Employee_Attendance_Reports.setText(QCoreApplication.translate("MainWindow", u"View Employee Attendance", None))
        self.actionTake_Course_Attendance.setText(QCoreApplication.translate("MainWindow", u"Take Course Attendance", None))
        self.actionView_Course_Attendance.setText(QCoreApplication.translate("MainWindow", u"View Course Attendance", None))
        self.actionTake_Exam_Attendance.setText(QCoreApplication.translate("MainWindow", u"Take Exam Attendance", None))
        self.actionView_Exam_Attendance.setText(QCoreApplication.translate("MainWindow", u"View Exam Attendance", None))
        self.actionTake_Home_Attendance.setText(QCoreApplication.translate("MainWindow", u"Take Home Attendance", None))
        self.actionView_Home_Attendance.setText(QCoreApplication.translate("MainWindow", u"View Home Attendance", None))
        self.label.setText("")
        self.main_date_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">{date}</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">ATTENDANCE</span><span style=\" font-size:16pt;\"> MANAGEMENT SYSTEM</span></p></body></html>", None))
        self.main_profile_icon.setText("")
        self.main_username_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">{user_name}</span></p></body></html>", None))
        self.dashboardButton.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.menuButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.Class_course_btn.setText(QCoreApplication.translate("MainWindow", u"CLASS AND COURSES", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Manage</span> Classes</p></body></html>", None))
        self.Create_class_btn.setText(QCoreApplication.translate("MainWindow", u"Create Class", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Manage</span> Courses</p></body></html>", None))
        self.Create_course_btn.setText(QCoreApplication.translate("MainWindow", u"Create Course", None))
        self.Teachers_btn.setText(QCoreApplication.translate("MainWindow", u"TEACHERS", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Manage</span> Teachers</p></body></html>", None))
        self.Create_teacher_btn.setText(QCoreApplication.translate("MainWindow", u"Create Teacher", None))
        self.Student_menu_button.setText(QCoreApplication.translate("MainWindow", u"STUDENTS", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Manage</span> Students</p></body></html>", None))
        self.Create_Student_button.setText(QCoreApplication.translate("MainWindow", u"Create Student", None))
        self.View_Student_m_button.setText(QCoreApplication.translate("MainWindow", u"View Student", None))
        self.Attendance_btn.setText(QCoreApplication.translate("MainWindow", u"ATTENDANCE", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Manage</span> Attendance</p></body></html>", None))
        self.Take_attendance_btn.setText(QCoreApplication.translate("MainWindow", u"Take Attendance", None))
        self.View_class_attendance_btn.setText(QCoreApplication.translate("MainWindow", u"View Class Attendance", None))
        self.View_student_attendance_btn.setText(QCoreApplication.translate("MainWindow", u"View Student Attendance", None))
        self.Today_attendance_report_btn.setText(QCoreApplication.translate("MainWindow", u"Today's Report", None))
        self.Session_term_btn.setText(QCoreApplication.translate("MainWindow", u"SESSIONS AND TERMS", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Manage</span> Session and Term</p></body></html>", None))
        self.Create_Session_term_btn.setText(QCoreApplication.translate("MainWindow", u"Create Session and Term", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Create </span><span style=\" font-size:18pt;\">Class</span></p></body></html>", None))
        self.goHome_button_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>/ Create Class</p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Create</span><span style=\" font-size:14pt;\"> Class</span></p></body></html>", None))
        self.createClassStatusLabel.setText(QCoreApplication.translate("MainWindow", u"N/O", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Class</span> Name</p></body></html>", None))
        self.create_class_name_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Class Name", None))
        self.CreateClassPushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#316293;\">All Classes</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Show</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Entries", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Search:</span></p></body></html>", None))
        self.view_class_search_btn.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Class Name", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.classesNumberLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#161616;\">Showing {n} to {nn} of {nnn} entries</span></p></body></html>", None))
        self.create_class_preview_btn.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.currentClassPageLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">{cp}</p></body></html>", None))
        self.create_class_next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Create </span><span style=\" font-size:18pt;\">Class Course</span></p></body></html>", None))
        self.goHome_button_3.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>/ Create Class Course</p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Create</span><span style=\" font-size:14pt;\"> Class</span></p></body></html>", None))
        self.createClassCourseStatusLabel.setText(QCoreApplication.translate("MainWindow", u"N/O", None))
        self.CreateClassCoursePushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select class <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Class Course Name <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.selectClassCombobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-- Select Class --", None))
        self.create_class_course_name_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Class Course Name", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#316293;\">All Classes</span></p></body></html>", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Show</span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Entries", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Search:</span></p></body></html>", None))
        self.view_class_course_search_btn.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Class Name", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Class Course Name", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.coursespageNumber_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#161616;\">Showing {n} to {nn} of {nnn} entries</span></p></body></html>", None))
        self.create_class_course_preview_btn.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.current_courses_page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">{cp}</p></body></html>", None))
        self.create_class_course_next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Create </span><span style=\" font-size:18pt;\">Teachears</span></p></body></html>", None))
        self.goHome_button_4.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>/ Create Teachers</p></body></html>", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Create</span><span style=\" font-size:14pt;\"> Class Teachers</span></p></body></html>", None))
        self.createTeachersStatusLabel.setText(QCoreApplication.translate("MainWindow", u"N/O", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.Class_courses_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-- Select course --", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Phone No <span style=\" vertical-align:super;\"/><span style=\" color:#aa0000; vertical-align:super;\">*</span></p></body></html>", None))
        self.CreateTeacherPushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Class Course Name <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Firstname <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select class <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Email Address <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.selectClassCombobox_createTeacher.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-- Select Class --", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Lastname <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.lineEdit_3.setInputMask(QCoreApplication.translate("MainWindow", u"+(xxx) xxx xxx xxx", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#316293;\">All Classes</span></p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Show</span></p></body></html>", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Entries", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Search:</span></p></body></html>", None))
        self.view_teachers_search_btn.setText("")
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Email Address", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Phone No", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Date Created", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.teachersPageNumber_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#161616;\">Showing {n} to {nn} of {nnn} entries</span></p></body></html>", None))
        self.show_teacher_preview_btn.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.currentpage_teacher_page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">{cp}</p></body></html>", None))
        self.ciew_teachers_next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Create </span><span style=\" font-size:18pt;\">Students</span></p></body></html>", None))
        self.goHome_button_5.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>/ Create Students</p></body></html>", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Create</span><span style=\" font-size:14pt;\"> Students</span></p></body></html>", None))
        self.createTeachersStatusLabel_2.setText(QCoreApplication.translate("MainWindow", u"N/O", None))
        self.student_lastname_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.Class_courses_combobox_students.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-- Select course --", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Admission number <span style=\" color:#aa0000; vertical-align:super;\">*</span></p></body></html>", None))
        self.CreateStudentPushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Class Course Name <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Firstname <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select class <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Other Name <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.student_firtname_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.selectClassCombobox_createStudent.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-- Select Class --", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Lastname <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.student_admission_number_enty.setInputMask(QCoreApplication.translate("MainWindow", u"xxxxxxxxx", None))
        self.student_admission_number_enty.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Students Addmission Number", None))
        self.student_othername_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Students Other Name", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#316293;\">All Classes</span></p></body></html>", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Show</span></p></body></html>", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Entries", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Search:</span></p></body></html>", None))
        self.view_students_search_btn.setText("")
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Other Name", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Admission No", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Date Created", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.studentsPageNumber_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#161616;\">Showing {n} to {nn} of {nnn} entries</span></p></body></html>", None))
        self.show_students_preview_btn.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.currentpage_students_page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">{cp}</p></body></html>", None))
        self.ciew_student_next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.teacher_m_title_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">All Student</span><span style=\" font-size:18pt;\"> In {class} Class</span></p></body></html>", None))
        self.goHome_button_7.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>/ View Students</p></body></html>", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">All Student</span><span style=\" font-size:14pt;\"> In Class</span></p></body></html>", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Show</span></p></body></html>", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"Entries", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Search:</span></p></body></html>", None))
        self.view_studentsList_search_btn.setText("")
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Other Name", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"Admission No", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"Date Created", None))
        self.studentsListPageNumber_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#161616;\">Showing {n} to {nn} of {nnn} entries</span></p></body></html>", None))
        self.show_studentsList_preview_btn.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.currentpage_studentsList_page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">{cp}</p></body></html>", None))
        self.ciew_studentList_next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Create </span><span style=\" font-size:18pt;\">Session and Term</span></p></body></html>", None))
        self.goHome_button_6.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>/ Create Session and Term</p></body></html>", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Create</span><span style=\" font-size:14pt;\"> Session and Term</span></p></body></html>", None))
        self.createSessionTermStatusLabel.setText(QCoreApplication.translate("MainWindow", u"N/O", None))
        self.createSesionTermPushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Session Name <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.selectTermCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"First", None))
        self.selectTermCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Second", None))
        self.selectTermCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Third", None))

        self.selectTermCombobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-- Select a Term --", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Term <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.create_session_entry.setInputMask(QCoreApplication.translate("MainWindow", u"xxxx/xxxx", None))
        self.create_session_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Session", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#316293;\">All Session and Term</span></p></body></html>", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Show</span></p></body></html>", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Entries", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.view_session_term_search_btn.setText("")
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Search:</span></p></body></html>", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; font-style:italic; color:#aa0000;\">Note</span><span style=\" font-style:italic; color:#aa0000;\"> : Click on the check symbol besides each tomake session and term active !!</span></p></body></html>", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Session", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Term", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.SessionTermpageNumber_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#161616;\">Showing {n} to {nn} of {nnn} entries</span></p></body></html>", None))
        self.create_session_term_preview_btn.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.current_session_terms_page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">{cp}</p></body></html>", None))
        self.create_session_term_next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.teacher_m_title_lbl_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Take</span><span style=\" font-size:18pt;\"> Attendance (Today's Date : {date})</span></p></body></html>", None))
        self.takeAttendGoHome_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>/ Take Attendance</p></body></html>", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#0083c5;\">All</span><span style=\" color:#0083c5;\"> Student In ({class}) Class</span></p></body></html>", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">SELECT THE </span><span style=\" font-size:16pt;\">DEVICE TO USE</span></p></body></html>", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#aa0000;\">Note</span><span style=\" color:#aa0000;\">: Make sure you have selected the device to use</span></p></body></html>", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">{N/O}</p></body></html>", None))
        self.attendance_stdnt_number_lbl.setText(QCoreApplication.translate("MainWindow", u"{N/O}", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"Attendance Statut", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Roll Number", None))
        self.attendance_student_class_option_lbl.setText(QCoreApplication.translate("MainWindow", u"{N/O}", None))
        self.atendance_student_dep_lbl.setText(QCoreApplication.translate("MainWindow", u"{N/O}", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"Class/Option", None))
        self.attendance_student_status.setText(QCoreApplication.translate("MainWindow", u"{N/O}", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">View </span><span style=\" font-size:18pt;\">Class Attendance</span><span style=\" font-size:18pt; font-weight:600;\"/></p></body></html>", None))
        self.goHome_button_8.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>/ View<span style=\" font-weight:600;\"/>Class Attendance<span style=\" font-weight:600;\"/></p></body></html>", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#0042c5;\">View</span><span style=\" color:#0042c5;\"> Class Attendance</span></p></body></html>", None))
        self.createSessionTermStatusLabel_2.setText(QCoreApplication.translate("MainWindow", u"N/O", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Session Date <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.viewAttendanceBtn.setText(QCoreApplication.translate("MainWindow", u"View Attendance", None))
        self.ViewDatepopupPushButton.setText("")
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#316293;\">Class </span><span style=\" font-size:12pt; color:#316293;\">Attendance</span></p></body></html>", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Show</span></p></body></html>", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"Entries", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.view_class_attendance_search_btn.setText("")
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Search:</span></p></body></html>", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"Other Name", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"Admission Number", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Session", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"Term", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.classAttendancePageNumber_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#161616;\">Showing {n} to {nn} of {nnn} entries</span></p></body></html>", None))
        self.view_class_attendance_preview_btn.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.current_class_attendance_page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">{cp}</p></body></html>", None))
        self.view_class_attendance_next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">View </span><span style=\" font-size:18pt;\">Student Attendance</span></p></body></html>", None))
        self.goHome_button_9.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>/ View<span style=\" font-weight:600;\"/>Class Attendance<span style=\" font-weight:600;\"/></p></body></html>", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#0042c5;\">View</span><span style=\" color:#0042c5;\"> Student Attendance</span></p></body></html>", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select Student <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.viewStudentAttendanceBtn.setText(QCoreApplication.translate("MainWindow", u"View Attendance", None))
        self.StudentscomboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-- Select Student --", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#316293;\">Class </span><span style=\" font-size:12pt; color:#316293;\">Attendance</span></p></body></html>", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Show</span></p></body></html>", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"Entries", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"Other Name", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"Admission Number", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"Session", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"Term", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.studentAttendancePageNumber_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#161616;\">Showing {n} to {nn} of {nnn} entries</span></p></body></html>", None))
        self.view_student_attendance_preview_btn.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.current_student_attendance_page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">{cp}</p></body></html>", None))
        self.view_student_attendance_next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">View </span><span style=\" font-size:18pt;\">Security Attendance</span></p></body></html>", None))
        self.goHome_button_10.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>/ View<span style=\" font-weight:600;\"/>Class Attendance<span style=\" font-weight:600;\"/></p></body></html>", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#0042c5;\">View</span><span style=\" color:#0042c5;\"> Security Attendance</span></p></body></html>", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select Date <span style=\" color:#aa0000;\">*</span></p></body></html>", None))
        self.ViewSecurityDatepopupPushButton.setText("")
        self.viewSecurityAttendanceBtn.setText(QCoreApplication.translate("MainWindow", u"View Attendance", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#316293;\">Security </span><span style=\" font-size:12pt; color:#316293;\">Attendance</span></p></body></html>", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Show</span></p></body></html>", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"Entries", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.view_security_attendance_search_btn.setText("")
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Search:</span></p></body></html>", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"Other Name", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"Admission Number", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.securityAttendancePageNumber_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#161616;\">Showing {n} to {nn} of {nnn} entries</span></p></body></html>", None))
        self.view_security_attendance_preview_btn.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.current_security_attendance_page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">{cp}</p></body></html>", None))
        self.view_security_attendance_next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Administrator</span><span style=\" font-size:16pt;\"> Dashboard</span></p></body></html>", None))
        self.goHome_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>/ Dashboard</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"STUDENTS", None))
        self.student_number_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">{S/N}</span></p></body></html>", None))
        self.label_13.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CLASSES", None))
        self.label_number_lbL.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">{S/N}</span></p></body></html>", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"CLASSES COURSES", None))
        self.class_courses_number_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">{S/N}</span></p></body></html>", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"TOTAL STUDENT ATTENDANCE", None))
        self.total_student_attendance_nbr_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">{S/N}</span></p></body></html>", None))
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"CLASS TEACHERS", None))
        self.class_teachers_nbr.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">{S/N}</span></p></body></html>", None))
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"SESSION & TERMS", None))
        self.student_number_lbl_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">{S/N}</span></p></body></html>", None))
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"TERMS", None))
        self.student_number_lbl_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">{S/N}</span></p></body></html>", None))
        self.label_24.setText("")
        self.copyright_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">\u00a9 Ndeze Bonheur 2024</span> | ULK(UPI) | All Rights Reserved</p></body></html>", None))
    # retranslateUi

