import sys
import os
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QMainWindow
from QDrawWidget import QDrawWidget


class IttGestureRecognizer(QMainWindow):
    def __init__(self):
        super(IttGestureRecognizer, self).__init__()
        self.draw_widget_width = 800
        self.draw_widget_height = 800
        self._init_ui()
        self.current_gesture_original = []
        self.curren_gesture_processed = []
        
    def _init_ui(self):
        self.setWindowTitle("$1 Gesture Recognizer")
        self.__ui = uic.loadUi("GestureRecognition.ui", self)
        self._drawWidget = QDrawWidget()
        self._drawWidget.setFixedSize(self.draw_widget_width, self.draw_widget_height)
        self.__ui.DrawWidgetContainer.addWidget(self._drawWidget)
        self.__ui.SaveGestureButton.clicked.connect(self.save_current_gesture)


    def save_current_gesture(self):
        self.current_gesture_original = self._drawWidget.points
        print(self.current_gesture_original)
        self.process_gesture()

    #processes the gesture for normalize size and other things
    def process_gesture(self):
        print("todo: processgesture")

if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    win = IttGestureRecognizer()

    win.show()
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        sys.exit(app.exec_())
