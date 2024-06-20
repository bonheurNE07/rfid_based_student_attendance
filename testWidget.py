import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow

from GUI.classCourseTableRow import Ui_ClassCourseTableRow
from GUI.createClassRowWidget import Ui_createClasseTableRowWidget
from GUI.loginWin import Ui_LoginWidget
from GUI.mainWindow import Ui_MainWindow
from GUI.sessionTermRowWidget import Ui_Form
from GUI.studentTableRowWidget import Ui_ViewstudentRowWidget
from GUI.TeacherTableRowWidget import Ui_TeachersTableRowWidget
from GUI.viewStudentAttendanceRow import Ui_StudentAttendanceRow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
