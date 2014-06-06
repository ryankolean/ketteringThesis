#!/usr/bin/python2

import sys
from PyQt4 import QtGui, QtCore

class LCCAControl(QtGui.QDialog):

    def __init__(self):
        super(LCCAControl, self).__init__()
        self.font = QtGui.QFont()
        self.initUI()

    def closeClicked(self):
        self.close()
    
    def makeProgressBar(self, percentage):
        progressBar = QtGui.QProgressBar(self)
        progressBar.setValue(percentage)
        progressBar.setAlignment(QtCore.Qt.AlignCenter)
        return progressBar        

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
        # Check for Beacon button - must be a toggle button
        if 'BEACON' in name:
            button.setCheckable(True)
            #button.clicked[bool].connect(some_slot_goes_here)
        return button

    def makeInfoBox(self, name, string, fontSize):
        thisLayout = QtGui.QVBoxLayout()
        self.font.setPointSize(fontSize)
        label = QtGui.QLabel(name)
        self.font.setBold(True)
        label.setFont(self.font)
        thisLayout.addWidget(label)
        lineEdit = QtGui.QLineEdit(string)
        self.font.setBold(False)
        lineEdit.setFont(self.font)
        lineEdit.setReadOnly(True)
        thisLayout.addWidget(lineEdit)
        return thisLayout

    def makeInfoBoxExtended(self, name, string, fontSize):
        thisLayout = QtGui.QVBoxLayout()
        self.font.setPointSize(fontSize)
        label = QtGui.QLabel(name)
        self.font.setBold(True)
        label.setFont(self.font)
        thisLayout.addWidget(label)
        lineEdit = QtGui.QTextEdit()
        lineEdit.setPlainText(string)
        self.font.setBold(False)
        lineEdit.setFont(self.font)
        lineEdit.setReadOnly(True)
        lineEdit.lineWrapMode()
        lineEdit.setFixedWidth(135)
        thisLayout.addWidget(lineEdit)
        return thisLayout

    def makeInfoGroup(self, name, string, fontSize):
        thisLayout = QtGui.QVBoxLayout()
        self.font.setPointSize(fontSize)
        lineEdit = QtGui.QLineEdit(string)
        self.font.setBold(False)
        lineEdit.setFont(self.font)
        lineEdit.setReadOnly(True)
        thisLayout.addWidget(lineEdit)
        thisBox = QtGui.QGroupBox(name)
        self.font.setBold(True)
        thisBox.setFont(self.font)
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

        # -------------- THE DATA -------------------- #
        # Not actual data right now! This is static data.
        cpu = 50
        memory = 25
        rx = '120KB'
        tx = '25KB'

        # DYNAMIC DATA FRAME
        dynamicLayout = QtGui.QVBoxLayout()
        dynamicFrame = QtGui.QFrame()
        dynamicFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        # add new label to the dynamicLayout
        dynamicLayout.addWidget(QtGui.QLabel('<b>CPU RATE</b>'))
        # add new pbar to the dynamicLayout
        dynamicLayout.addWidget(self.makeProgressBar(cpu))
        # add new label to the dynamicLayout
        dynamicLayout.addWidget(QtGui.QLabel('<b>MEMORY RATE</b>'))
        # add new pbar to the dynamicLayout
        dynamicLayout.addWidget(self.makeProgressBar(memory))

        # Make gridLayout for rxtx
        rxtxLayout = QtGui.QHBoxLayout()
        # add label and data to gridLayout
        rxtxLayout.addWidget(self.makeInfoGroup('RX', rx, 8))
        # add label and data to gridLayout
        rxtxLayout.addWidget(self.makeInfoGroup('TX', tx, 8))
        # add the rxtxLayout to the dynamicLayout
        dynamicLayout.addLayout(rxtxLayout)
        
        dynamicFrame.setLayout(dynamicLayout)




        # ACTION BUTTONS FRAME
        actionFrame = QtGui.QFrame()
        actionFrame.setFrameShape(QtGui.QFrame.StyledPanel) 

        x = 69
        y = 55
        actionGrid = QtGui.QGridLayout()
        actionGrid.addWidget(self.makeActionButton('VIEW\nLOGS', 'Display log file', x, y), 0, 0)
        actionGrid.addWidget(self.makeActionButton('CLEAR\nLOGS', 'Clear current log file', x, y), 1, 0)
        actionGrid.addWidget(self.makeActionButton('BEACON', 'Turn on beacon light', x, y), 2, 0)
        actionGrid.addWidget(self.makeActionButton('POWER\nON', 'Execute power on\nand boot up machine', x, y), 0, 1)
        actionGrid.addWidget(self.makeActionButton('POWER\nOFF', 'Execute shutdown\nand power off machine', x, y), 1, 1)
        actionGrid.addWidget(self.makeActionButton('REBOOT', 'Perform automated\nshutdown and boot up\nprocedure', x, y), 2, 1)

        #actionGrid.addWidget(self.makeActionButton('BEACON\nON', 'Turn on beacon light\nfor this machine', x, y), 0, 2)
        #actionGrid.addWidget(self.makeActionButton('BEACON\nOFF', 'Turn off beacon light\nfor this machine', x, y), 1, 2)
        #actionGrid.addWidget(self.makeActionButton('BEACON\nFLASH', 'Turn the beacon light\n', x, y), 2, 2)
        
        actionFrame.setLayout(actionGrid)




        # add dynamicFrame and actionFrame into the UpperLayout
        upperLayout.addWidget(dynamicFrame)
        upperLayout.addWidget(actionFrame)




        # LOWER DATA FRAME
        lowerLayout = QtGui.QHBoxLayout()
        lowerFrame = QtGui.QFrame()
        lowerFrame.setFrameShape(QtGui.QFrame.StyledPanel)

        # make 3 vertical layouts for 3 "columns"
        col1Layout = QtGui.QVBoxLayout()
        col2Layout = QtGui.QVBoxLayout()
        col3Layout = QtGui.QVBoxLayout()
        # make 3 frames from those column layouts
        col1Frame = QtGui.QFrame()
        col1Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        col2Frame = QtGui.QFrame()
        col2Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        col3Frame = QtGui.QFrame()
        col3Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        # add data to col1Layout
        col1Layout.addLayout(self.makeInfoBox('IBM Machine Type', 'LCCA Input Node', 7))
        col1Layout.addLayout(self.makeInfoBox('Model Number', '123ABC45', 7))
        col1Layout.addLayout(self.makeInfoBox('Serial Number', '123456789', 7))
        col1Layout.addLayout(self.makeInfoBox('Firmware Version', 'abc123ef45', 7))
        col1Layout.addLayout(self.makeInfoBox('Physical Location', 'XXYY', 7))
        col1Frame.setLayout(col1Layout)
        # add data to col2Layout
        col2Layout.addLayout(self.makeInfoBox('DIMM Population', 'xxxxxx', 7))
        col2Layout.addLayout(self.makeInfoBox('Total Memory Available', 'yyyyyyy', 7))
        col2Layout.addLayout(self.makeInfoBox('HDD', 'YES', 7)) # THIS SHOULD BE A YES/NO BOOLEAN
        col2Layout.addLayout(self.makeInfoBox('HDD SIZE/REMAINING', '1.24G/1.1G', 7))
        col2Frame.setLayout(col2Layout)
        # add data to col3Layout
        col3Layout.addLayout(self.makeInfoBox('MAC Address', '01-23-45-67-89-AB-CD', 7))
        ipString = "eth0: %s \neth1: %s \neth2: %s \neth3: %s" % ('11.222.333.4444', '22.33.444.5555', '33.44.555.6666', '44.55.666.7777')
        col3Layout.addLayout(self.makeInfoBoxExtended('IP Address', ipString, 7))
        col3Layout.addLayout(self.makeInfoBox('NTP Status', 'GOOD', 7)) # SHOULD THIS BE A BOOLEAN TOO?
        col3Frame.setLayout(col3Layout)
        # Add each column layout to lowerLayout
        lowerLayout.addWidget(col1Frame)
        lowerLayout.addWidget(col2Frame)
        lowerLayout.addWidget(col3Frame)

        lowerFrame.setLayout(lowerLayout)



        # Add each layout into the overall layout
        self.layout.addLayout(upperLayout)        
        self.layout.addStretch(0)
        self.layout.addWidget(lowerFrame)
        closeButton = self.makeActionButton('CLOSE', '', 500, 25)
        closeButton.clicked.connect(self.closeClicked)
        self.layout.addWidget(closeButton) 

        # Finalize layout of window and display
        self.setLayout(self.layout)
        self.move(300, 150)
        self.setWindowTitle('LCCA HEAD NODE CONTROL PANEL')
        self.setGeometry(5, 5, 500, 200)
        self.show()

# Run as an independent application
def main():
    app = QtGui.QApplication(sys.argv)
    ex = LCCAControl()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
