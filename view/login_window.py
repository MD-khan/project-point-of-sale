import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.uic import loadUi

#UserLoginForm, baseClass = uic.loadUiType('user_login.ui')


class LoginWindow(qtw.QWidget):
    # Define Signal
    user_autenticated = qtc.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Code start here
        # call and setup user login ui
        loadUi('register.ui', self)
        self.setupUi(self)

        #
        self.btn_login.clicked.connect(self.authUser)
        self.input_user_id.textChanged.connect(self.setButtonText)
        self.btn_cancel_login.clicked.connect(self.close)

        # show the logged in user name
        self.user_autenticated.connect(self.userLoggedIn)

        # Code End here
        self.show()

    def authUser(self):
        user_name = self.input_user_id.text()
        user_password = self.input_password.text()

        if user_name == 'admin' and user_password == '1234':
            qtw.QMessageBox.information(self, 'Success', "Logged in")
            # emit the signal
            self.user_autenticated.emit(user_name)
        else:
            qtw.QMessageBox.critical(self, 'Failed', 'Not Logged in')

    # @qtc.pyqtSlot(str)
    def setButtonText(self, text):
        if text:
            self.btn_login.setText(f'Log in {text}')
        else:
            self.btn_login.setText('Log in')

    def userLoggedIn(self, user_name):
        qtw.QMessageBox.information(
            self, 'Logged in', f'{user_name} is logged in')


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    main_window = LoginWindow()
    sys.exit(app.exec_())
