# Filename: pycalc.py
# A Simple calcuator built using Python and PyQt5

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

__version__ = '0.1'
__author__ = 'Jeff Henrichs'

# Create a subclass of QMainWindow to setup the calculator's GUI
class PyCalcUi(QMainWindow):
    #PyCalc's View (GUI)
    def __init__(self):
        # View initializer
        super().__init__()
        # Set some maion window's properties
        self.setWindowTitle('PyCalc')
        self.setFixedSize(350, 500)
        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

# Client code
def main():
    #Main function.
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyCalcUi()
    view.show()
    # Execute the calculator's main loop
    sys.exit(pycalc.exec())

if __name__ == '__main__':
    main()