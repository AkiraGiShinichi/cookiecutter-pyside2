import os
import sys
import pkg_resources
try: # PySide2
    from PySide2 import QtGui, QtWidgets, QtCore
    from PySide2.QtCore import Signal, Slot
    from PySide2.QtCore import Qt
    from PySide2.QtWidgets import QApplication, QMainWindow
    # os.system("PySide2-rcc resources/ui/app_resources.qrc -o app_resources_rc.py")
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

from {{cookiecutter.package_name}}.app import view
from {{cookiecutter.package_name}}.app import presenter
from {{cookiecutter.package_name}}.app import model

class SimpleGui(QMainWindow):
    """Create the main window that stores all of the widgets necessary for the application."""

    def __init__(self, parent=None):
        """Initialize the components of the main window."""
        super(SimpleGui, self).__init__(parent)

        # * I. Define MVP of Login
        self.model = model.Greeting()
        self.view = view.View()
        self.presenter = presenter.Presenter(self.view, self.model)
        
        view.show()


def main(args=sys.argv):
    application = QApplication([])
    main_window = SimpleGui()
    sys.exit(application.exec_())

if __name__ == "__main__":
    main()