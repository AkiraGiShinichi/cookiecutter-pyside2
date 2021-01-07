import os
import sys

try: # PySide2
    from PySide2 import QtGui, QtWidgets, QtCore
    from PySide2.QtCore import Signal, Slot
    from PySide2.QtCore import Qt
    from PySide2.QtWidgets import QApplication, QMainWindow
    os.system("pyside2-rcc resources/ui/app_resources.qrc -o app_resources_rc.py")
    print("PySide2 was used")
except ImportError: # PyQt5
    from PyQt5 import QtGui, QtWidgets, QtCore
    from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
    from PyQt5.Qt import Qt
    from PyQt5.QtWidgets import QApplication, QMainWindow
    # os.system('pyrcc5 resources/ui/app_resources.qrc -o app_resources_rc.py')
    print("PyQt5 was used")
except ImportError:
    print('Qt for Python was not installed.')
    exit(1)

from .ui_untitled import Ui_Form

class View(QtWidgets.QWidget):
    pushButton_clicked = Signal()

    def __init__(self, parent=None):
        super(View, self).__init__(parent)

        # * Private properties
        self.isSignInTab = None

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # remove window default title bar
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)


# ------------------------------ Export signals ------------------------------ #
    def on_pushButton_clicked(self):
        self.pushButton_clicked.emit()
# ---------------------------------------------------------------------------- #
