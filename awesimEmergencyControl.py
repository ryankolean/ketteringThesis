#!/usr/bin/python2

import sys
from PyQt4 import QtGui, QtCore

class EmergencyControl(QtGui.QDialog):

    def __init__(self, arrayName):
        super(EmergencyControl, self).__init__()
        self.font = QtGui.QFont()
        self.initUI(arrayName)

    def makeActionButton(self, name, tooltip, sizeX, sizeY):
        button = QtGui.QPushButton(name)
        button.setToolTip(tooltip)
        button.setMinimumSize(sizeX, sizeY)
        self.font.setBold(True)
        button.setFont(self.font)
        color = button.palette()
        color.setColor(button.backgroundRole(), QtGui.QColor(0,102,187))
        color.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255,255,255))
        button.setPalette(color)
        return button

    # closeClicked - called to close the panel on button click
    def closeClicked(self):
        self.close()

    def initUI(self, arrayName):

	#----------------init layouts----------------------
        # Create layout container to add layouts (addLayout)
        # This will be used to to set the window's layout
        self.layout = QtGui.QVBoxLayout()

        # Layout Boxes to Store things
        actionButtonsLayout = QtGui.QHBoxLayout()
        closeButtonLayout = QtGui.QHBoxLayout()

        actionButtonsLayout.addWidget(self.makeActionButton('START', 'Start %s' % (arrayName), 125, 65))
        actionButtonsLayout.addWidget(self.makeActionButton('STOP', 'Stop %s' % (arrayName), 125, 65))
        actionButtonsLayout.addWidget(self.makeActionButton('RESTART', 'Restart %s' % (arrayName), 125, 65))

        closeButton = self.makeActionButton('CLOSE', 'Close this panel', 375, 30)
        closeButton.clicked.connect(self.closeClicked)
        closeButtonLayout.addWidget(closeButton)


        # Set Overall Layout of the Window 
        self.layout.addLayout(actionButtonsLayout)        
        self.layout.addStretch(0)
        self.layout.addLayout(closeButtonLayout)       

        self.setLayout(self.layout)

        # Align the window's left corner on start
        self.move(300, 150)
        self.setWindowTitle('%s EMERGENCY CONTROL' %(arrayName))
        # Give the Window dimensions
        self.setGeometry(50, 50, 330, 60)
        # Draw the window
        self.show()

# Run as an independent application
def main():
    app = QtGui.QApplication(sys.argv)
    ex = EmergencyControl()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
