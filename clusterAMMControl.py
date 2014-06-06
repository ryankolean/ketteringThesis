#!/usr/bin/python2

import sys
from PyQt4 import QtGui, QtCore

class AMMControl(QtGui.QDialog):

    def __init__(self):
        super(AMMControl, self).__init__()
        self.font = QtGui.QFont()
        self.initUI()

    def closeClicked(self):
        self.close()
    
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
        if 'BEACON' in name:
            button.setCheckable(True)
            #button.clicked[bool].connect(some_slot_goes_here)
        return button

    def makeInfoBox(self, name, string, fontSize):
        thisLayout = QtGui.QVBoxLayout()
        self.font.setPointSize(fontSize)
        self.font.setBold(True)
        label = QtGui.QLabel('%s:' % (name))
        label.setFont(self.font)
        thisLayout.addWidget(label)
        lineEdit = QtGui.QLineEdit(string)
        self.font.setBold(False)
        lineEdit.setFont(self.font)
        lineEdit.setReadOnly(True)
        thisLayout.addWidget(lineEdit)
        return thisLayout

    def makeInfoGroup(self, name, string, fontSize):
        thisLayout = QtGui.QVBoxLayout()
        self.font.setPointSize(fontSize)
        lineEdit = QtGui.QLineEdit(string)
        lineEdit.setFont(self.font)
        lineEdit.setReadOnly(True)
        thisLayout.addWidget(lineEdit)
        thisBox = QtGui.QGroupBox(name)
        thisBox.setLayout(thisLayout)
        return thisBox

    def initUI(self):
        # This will be used to to set the window's overall layout
        self.layout = QtGui.QVBoxLayout()

        # Layouts/Frames to store the objects, ie. buttons, text, etc.
        upperLayout = QtGui.QHBoxLayout()

        lowerLayout = QtGui.QHBoxLayout()
        lowerFrame = QtGui.QFrame()
        lowerFrame.setFrameShape(QtGui.QFrame.StyledPanel)

        # ACTION BUTTONS FRAME
        actionFrame = QtGui.QFrame()
        actionFrame.setFrameShape(QtGui.QFrame.StyledPanel) 

        x = 80
        y = 55
        # make action buttons actionGrid
        actionGrid = QtGui.QGridLayout()
        # add viewLogButton to actionGrid 0,0
        actionGrid.addWidget(self.makeActionButton('VIEW\nLOGS', 'Display logs files', x, y), 0, 0)
        # add clearLogButton to actionGrid 1,0
        actionGrid.addWidget(self.makeActionButton('CLEAR\nLOGS', 'Clear current log files', x, y), 0, 1)
        # add beaconButton to actionGrid 2,0
        actionGrid.addWidget(self.makeActionButton('BEACON', 'Turn on beacon light', x, y), 0, 2)
        # add rebootButton to actionGrid 2,1
        actionGrid.addWidget(self.makeActionButton('REBOOT', 'Perform automated\nshutdown and boot up\nprocedure', x, y), 0, 3)
        
        actionFrame.setLayout(actionGrid)

        # add dynamicFrame and actionFrame into the UpperLayout
        upperLayout.addWidget(actionFrame)

        # LOWER DATA FRAME
        lowerLayout = QtGui.QHBoxLayout()
        lowerFrame = QtGui.QFrame()
        lowerFrame.setFrameShape(QtGui.QFrame.StyledPanel)

        # make 3 vertical layouts for 3 "columns"
        col1Layout = QtGui.QVBoxLayout()
        col2Layout = QtGui.QVBoxLayout()
        # make 3 frames from those column layouts
        col1Frame = QtGui.QFrame()
        col1Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        col2Frame = QtGui.QFrame()
        col2Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        # add data to col1Layout
        col1Layout.addLayout(self.makeInfoBox('SERIAL NUMBER', '123456789', 7))
        col1Layout.addLayout(self.makeInfoBox('FIRMWARE VERSION', 'abc123ef45', 7))
        col1Layout.addLayout(self.makeInfoBox('PHYSICAL LOCATION', 'XXYY', 7))
        col1Frame.setLayout(col1Layout)
        # add data to col2Layout
        col2Layout.addLayout(self.makeInfoBox('MAC ADDRESS', '01-23-45-67-89-AB-CD', 7))
        col2Layout.addLayout(self.makeInfoBox('IP ADDRESS', '11.222.333.4444', 7))
        col2Layout.addLayout(self.makeInfoBox('NTP STATUS', 'GOOD', 7))
        col2Frame.setLayout(col2Layout)
        # Add each column layout to lowerLayout
        lowerLayout.addWidget(col1Frame)
        lowerLayout.addWidget(col2Frame)
        lowerFrame.setLayout(lowerLayout)

        # Add each layout into the overall layout
        self.layout.addLayout(upperLayout)        
        self.layout.addStretch(0)
        self.layout.addWidget(lowerFrame)
        closeButton = self.makeActionButton('CLOSE', '', 365, 25)
        closeButton.clicked.connect(self.closeClicked)
        self.layout.addWidget(closeButton) 

        # Finalize layout of window and display
        self.setLayout(self.layout)
        self.move(300, 150)
        self.setWindowTitle('AMM CONTROL PANEL')
        self.setGeometry(5, 5, 365, 200)
        self.show()

# Run as an independent application
def main():
    app = QtGui.QApplication(sys.argv)
    ex = AMMControl()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
