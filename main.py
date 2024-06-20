import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QSplashScreen, QLabel
from PySide6.QtCore import Qt, QTimer, QCoreApplication, QDate
from PySide6.QtGui import QPixmap, QIcon

from GUI.mainWindow import Ui_MainWindow
from GUI.loginWin import Ui_LoginWidget

from tests import cryptogen
from menuWidget import MenuLogic


class SplashScreen(QSplashScreen):
    def __init__(self, pixmap):
        super().__init__(pixmap)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWidget()
        self.ui.setupUi(self)

        self.ui.login_pushButton.clicked.connect(lambda: self.checkLogin())

        # SECRET
        self.credentials_filename = "credentials.enc"

        __secret_password = "bonheurNDEZEemmanuel37"
        self.credentials_key = cryptogen.generateKey(__secret_password.encode())
        
    def checkLogin(self):
        user_role = self.ui.userRoleComboBox.currentText()
        user_name = self.ui.Username_lineEdit.text()
        user_password = self.ui.passwrod_lineEdit.text()
        user_email = self.ui.email_lineEdit.text()

        #########################
        # MASTER ADMIN CHECKING #
        #########################
        credentials = cryptogen.readCredentials(self.credentials_filename, self.credentials_key)

        if user_role == "Administrator" and user_email == credentials[2]:
            if user_name == credentials[0] and user_password == credentials[1]:
                self.loginSuccess(user_name,user_role)
        #########################
        # OTHER USERS CHECKING  #
        #########################
        # here i will use database check
        else:
            self.loginFail()
    
    def loginSuccess(self,user_name,user_role):
        user_name = user_name
        user_role = user_role

        window.setUserName(user_name)
        window.setUserRole(user_role)
        window.show()
        self.hide()

    def loginFail(self):
        window.hide()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.menu_logic = MenuLogic(self.ui)

        self.initializeGUI()
        self.manageMenu()

    def setUserName(self, name):
        self.ui.main_username_label.setText(name)

    def setUserRole(self, role):
        self.user_role = role

    
    def initializeGUI(self):
        global __USER_NAME
        # GET INITAL HEIGHT OF MENU FRAMES
        self.initial_course_frame_h = self.ui.CLASS_COURSE_F.height()
        self.initial_attendance_frame_h = self.ui.ATTENDANCE_F.height()
        self.initial_session_term_frame_h = self.ui.SESSION_TERM_F.height()
        self.initial_student_frame_h = self.ui.STUDENT_F.height()
        self.initial_teachers_frame_h = self.ui.TEACHERS_F.height()

        current_date =  QDate.currentDate()
        date_string = current_date.toString("yyyy-MM-dd")

        self.ui.main_date_label.setText(date_string)
        pass

    def manageMenu(self):
        # set as Current Page The Create a new Class Course Page
        self.ui.Create_class_btn.clicked.connect(lambda:self.menu_logic.setCurrentWidget(
            self.ui.Create_class_page
        ))
        # set as Current Page The Create a new Class Course Page
        self.ui.Create_course_btn.clicked.connect(lambda:self.menu_logic.setCurrentWidget(
            self.ui.Create_course_page
        ))
        # set as Current Page The Create a New Teacher Page
        self.ui.Create_teacher_btn.clicked.connect(lambda:self.menu_logic.setCurrentWidget(
            self.ui.Create_teacher_page
        ))
        # set as Current Page The Create a new  Student Page
        self.ui.Create_Student_button.clicked.connect(lambda:self.menu_logic.setCurrentWidget(
            self.ui.Create_student_page
        ))
        # set as Current Page The View Student Report Page
        self.ui.View_Student_m_button.clicked.connect(lambda:self.menu_logic.setCurrentWidget(
            self.ui.View_student_page
        ))
        # set as Current Page The Take Students Attendance Page
        self.ui.Take_attendance_btn.clicked.connect(lambda:self.menu_logic.setCurrentWidget(
            self.ui.Take_attendance_page
        ))
        # set as Current Page The View Class Attendance Page
        self.ui.View_class_attendance_btn.clicked.connect(lambda:self.menu_logic.setCurrentWidget(
            self.ui.View_class_attendance_page
        ))
        # set as Current Page The View Student Attendance Page
        self.ui.View_student_attendance_btn.clicked.connect(lambda:self.menu_logic.setCurrentWidget(
            self.ui.View_student_attendance_page
        ))
        # set as Current Page The Create Sessions and Term Page
        self.ui.Create_Session_term_btn.clicked.connect(lambda:self.menu_logic.setCurrentWidget(
            self.ui.sessions_terms_page
        ))

        self.ui.Today_attendance_report_btn.clicked.connect(lambda:self.menu_logic.downloadReport())

        initial_width = 300

        def annumateMenu():
            # check the actual size dimension of the frame
            current_height = self.ui.menu_main_frame.height()
            current_width = self.ui.menu_main_frame.width()

            print(f"menu frame actual size ({current_width},{current_height})")

            if current_width == initial_width:
                self.ui.menu_main_frame.setMaximumSize(0, current_height)
                self.ui.menu_main_frame.setMinimumSize(0, current_height) # Set minimum size (width, height) in pixels
            elif current_width != initial_width:
                self.ui.menu_main_frame.setMaximumSize(initial_width, current_height)
                self.ui.menu_main_frame.setMinimumSize(initial_width, current_height) # Set minimum size (width, height) in pixels

        def annumateMenuFrames(index:int):
            up_icon = QIcon("GUI/Resources/icons/skyblue/chevron-up.svg")
            down_icon = QIcon("GUI/Resources/icons/skyblue/chevron-down.svg")

            if index == 1:
                # change icon
                icon = QIcon()
                # annumate the CLASS_COURSE_F frame
                current_height = self.ui.CLASS_COURSE_F.height()
                current_width = self.ui.CLASS_COURSE_F.width()

                if current_height == self.initial_course_frame_h:
                    self.ui.CLASS_COURSE_F.setMaximumSize(current_width, 0)
                    self.ui.Class_course_btn.setIcon(up_icon)
                elif current_height != self.initial_course_frame_h:
                    self.ui.CLASS_COURSE_F.setMaximumSize(current_width, self.initial_course_frame_h)
                    self.ui.Class_course_btn.setIcon(down_icon)

            elif index == 2:
                # annumate the TEACHERS_F frame
                current_height = self.ui.TEACHERS_F.height()
                current_width = self.ui.TEACHERS_F.width()

                if current_height == self.initial_teachers_frame_h:
                    self.ui.TEACHERS_F.setMaximumSize(current_width, 0)
                    self.ui.Teachers_btn.setIcon(up_icon)
                elif current_height != self.initial_teachers_frame_h:
                    self.ui.TEACHERS_F.setMaximumSize(current_width, self.initial_teachers_frame_h)
                    self.ui.Teachers_btn.setIcon(down_icon)
                
            elif index == 3:
                # annumate the STUDENT_F frame
                current_height = self.ui.STUDENT_F.height()
                current_width = self.ui.STUDENT_F.width()

                if current_height == self.initial_student_frame_h:
                    self.ui.STUDENT_F.setMaximumSize(current_width, 0)
                    self.ui.Student_menu_button.setIcon(up_icon)
                elif current_height != self.initial_student_frame_h:
                    self.ui.STUDENT_F.setMaximumSize(current_width, self.initial_student_frame_h)
                    self.ui.Student_menu_button.setIcon(down_icon)
            elif index == 4:
                # annumate the ATTENDANCE_F frame
                current_height = self.ui.ATTENDANCE_F.height()
                current_width = self.ui.ATTENDANCE_F.width()

                if current_height == self.initial_attendance_frame_h:
                    self.ui.ATTENDANCE_F.setMaximumSize(current_width, 0)
                    self.ui.Attendance_btn.setIcon(up_icon)
                elif current_height != self.initial_attendance_frame_h:
                    self.ui.ATTENDANCE_F.setMaximumSize(current_width, self.initial_attendance_frame_h)
                    self.ui.Attendance_btn.setIcon(down_icon)
            elif index == 5:
                # annumate the SESSION_TERM_F frame
                current_height = self.ui.SESSION_TERM_F.height()
                current_width = self.ui.SESSION_TERM_F.width()

                if current_height == self.initial_session_term_frame_h:
                    self.ui.SESSION_TERM_F.setMaximumSize(current_width, 0)
                    self.ui.Session_term_btn.setIcon(up_icon)
                elif current_height != self.initial_session_term_frame_h:
                    self.ui.SESSION_TERM_F.setMaximumSize(current_width, self.initial_session_term_frame_h)
                    self.ui.Session_term_btn.setIcon(down_icon)
            pass

        self.ui.menuButton.clicked.connect(lambda:annumateMenu())
        
        self.ui.Class_course_btn.clicked.connect(lambda:annumateMenuFrames(1))
        self.ui.Teachers_btn.clicked.connect(lambda:annumateMenuFrames(2))
        self.ui.Student_menu_button.clicked.connect(lambda:annumateMenuFrames(3))
        self.ui.Attendance_btn.clicked.connect(lambda:annumateMenuFrames(4))
        self.ui.Session_term_btn.clicked.connect(lambda:annumateMenuFrames(5))




if __name__ == "__main__":
    app = QApplication(sys.argv)

    # create and show the splash screen
    splash_pix = QPixmap("GUI/Resources/tempsnip.png")
    splash = SplashScreen(splash_pix)
    splash.show()
    
    splash.showMessage("Loading ...")
    app.processEvents()

window = MainWindow()
#window.show()
login_widget = LoginWindow()
login_widget.show()

splash.finish(window)    
sys.exit(app.exec())

    


