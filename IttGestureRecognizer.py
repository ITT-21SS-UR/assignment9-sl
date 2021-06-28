import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from QDrawWidget import QDrawWidget


class IttGestureRecognizer(QMainWindow):
    def __init__(self):
        super(IttGestureRecognizer, self).__init__()
        self._drawWidget = QDrawWidget
        self._drawWidget


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    win = IttGestureRecognizer()

    win.show()
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        sys.exit(app.exec_())
