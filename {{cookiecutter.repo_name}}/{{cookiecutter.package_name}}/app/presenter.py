import sys

from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtCore import Signal, Slot

from {{cookiecutter.package_name}}.app import view
from {{cookiecutter.package_name}}.app import model

class Presenter(QtCore.QObject):
    # something_happened = Signal()
    def __init__(self, view_:view.View, model:model.Greeting):
        super().__init__()  # This is required!

        self.model = model
        
        self.view = view_
        self.view.pushButton_clicked.connect(self.close_window)

    def close_window(self):
        self.model.goodbye('World')

    