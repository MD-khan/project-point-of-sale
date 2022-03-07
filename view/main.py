
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import uic

from login_window import LoginWindow
from dashboard import Ui_MainWindow

# custom
# both can be use to load ui
#from user import Ui_user_login_form


class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Code start here
        # call and setup user login ui
        #self.login = LoginWindow()

        #self.login.btn_login.setStyleSheet('background-color: red')

        self.dash = Ui_MainWindow()

       # self.dash .show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
