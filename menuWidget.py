from PySide6.QtCore import QObject, Signal

class MenuLogic(QObject):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

    def setCurrentWidget(self, page):
        self.ui.MainStackedWidget.setCurrentWidget(page)

    def downloadReport(self):
        # process and download data in format of a xls file
        pass

