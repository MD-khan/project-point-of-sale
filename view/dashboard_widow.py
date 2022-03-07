import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import uic

from dashboard import Ui_MainWindow


class Dashboard(qtw.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Code start here
        # call and setup user login ui
        #self.user_ui = UserLoginForm()
        #self.dash = Ui_MainWindow()
        self.setupUi(self)

        # Code End here
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    main_window = Dashboard()
    sys.exit(app.exec_())
