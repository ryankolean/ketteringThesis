#!/usr/bin/python2

import sys
from PyQt4 import QtGui, QtCore 

from clusterAMMControl import AMMControl 
from clusterSwitchControl import SwitchControl
from clusterBladeControl import BladeControl
from clusterBladeCenterPanel import BladeCenterPanel
from clusterRTOP import RtopPanel
from clusterMediaTray import ClusterMediaTray

#############################
# 
# The input for this widget will be the pass in of "drilDownData" as specified in clusterTopoClusterLevel.py
# The current placeholder is, dynamicInfo
# 
############################

class TopoBCenterLevel(QtGui.QWidget):
    def __init__(self, data):
        super(TopoBCenterLevel, self).__init__()
        self.font = QtGui.QFont() 
        self.initUI(data)

    def slotBlade(self, dynamicData):
        self.blade = BladeControl(dynamicData)
        self.blade.exec_()

    def slotAMM(self):
        self.AMM = AMMControl()
        self.AMM.exec_()

    def slotSwitch(self):
        self.Switch = SwitchControl()
        self.Switch.exec_()

    def slotBCPanel(self):
        self.bcControl = BladeCenterPanel()
        self.bcControl.exec_()

    def slotRtop(self):
        self.Rtop = RtopPanel()
        self.Rtop.exec_()

    def slotMediaTray(self, bladeAssign):
        self.trayAssignment = ClusterMediaTray(bladeAssign)
        self.trayAssignment.exec_()

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

    def makeHardwareButton(self, label, state, sizeX, sizeY, drillDownData, statusInfoArray):
        button = QtGui.QPushButton(label)
        button.setMinimumSize(sizeX, sizeY)
        self.font.setBold(True)
        button.setFont(self.font)

        # Make Tooltip to display status of hardware button
        # checkIfLast - check if last element being added to the string; removes the '\n' from last line
        statusString = ''
        checkIfLast = 0
        for i in statusInfoArray:
            if checkIfLast != len(statusInfoArray) - 1:
                statusString += i + '\n'
            else:
                statusString += i
            checkIfLast += 1
        button.setToolTip(statusString)

        buttonsColor = button.palette()
        if state == 0: #HARDWARE UP AND GOOD STATE
            buttonsColor.setColor(button.backgroundRole(), QtGui.QColor(0,102,0))
            buttonsColor.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255,255,255))
        elif state == 1: #HARDWARE DOWN  OR BAD STATE
            buttonsColor.setColor(button.backgroundRole(), QtGui.QColor(221,0,0))
            buttonsColor.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255,255,255))
        elif state == 2: #HARDWARE HAS NON-CRITICAL ISSUES 
            buttonsColor.setColor(button.backgroundRole(), QtGui.QColor(255,221,68))
            buttonsColor.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255,255,255))
        elif state == 3: #NO HARDWARE PRESENT STATE
            button.setEnabled(False)
        button.setPalette(buttonsColor)

        # What are we connecting the button to?
        if ('ADVANCED\nMANAGEMENT\nMODULE' == label):
            button.clicked.connect(self.slotAMM)
        elif ('SWITCH\nMODULE\n001' == label):
            button.clicked.connect(self.slotSwitch)
        elif ('SWITCH\nMODULE\n002' == label):
            button.clicked.connect(self.slotSwitch)
        # The media tray is a special case and the drillDown data passed for its call
        # is meant to set a parameter to the first blade in the bladecenter as default
        # for the media tray assignment, this will need to be swapped for the actual assignment of
        # the media tray, when the backend in implemented
        elif ('MEDIA\nTRAY' == label):
            button.clicked.connect(lambda: self.slotMediaTray(drillDownData[0][0]))
        else:
            button.clicked.connect(lambda: self.slotBlade(drillDownData))            
        return button

    def initUI(self, data):
        # This will be used to to set the window's layout
        self.layout = QtGui.QVBoxLayout()

        topBarLayout = QtGui.QHBoxLayout()
        topLeftLayout = QtGui.QHBoxLayout()
        topRightLayout = QtGui.QHBoxLayout()

        topLeftFrame = QtGui.QFrame()
        topRightFrame = QtGui.QFrame()
        topLeftFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        topRightFrame.setFrameShape(QtGui.QFrame.StyledPanel)

        self.backButton = self.makeActionButton('BACK', 'Return to high-level view', 158, 60)
        self.bladeRebootButton = self.makeActionButton('REBOOT\nERROR BLADES', 'Perform automated shutdown\nand boot up procedures\nto all blades with errors\nin this blade center', 156, 60)
        self.bcPanelButton = self.makeActionButton('BLADE CENTER\nPANEL', 'Open information panel\nfor the blade center', 158, 60)
        self.rtopButton = self.makeActionButton('RTOP', 'Launch blade, LCCA,\nand management node\nmonitor utility', 158, 60)

        self.bcPanelButton.clicked.connect(self.slotBCPanel)
        self.rtopButton.clicked.connect(self.slotRtop)

        topLeftLayout.addWidget(self.backButton)
        topRightLayout.addWidget(self.bcPanelButton)
        topRightLayout.addWidget(self.bladeRebootButton)
        topRightLayout.addWidget(self.rtopButton)
        topLeftFrame.setLayout(topLeftLayout)
        topRightFrame.setLayout(topRightLayout)

        topBarLayout.addWidget(topLeftFrame)
        topBarLayout.addWidget(topRightFrame)

        # Make grid layout for the array buttons
        bladeGrid = QtGui.QGridLayout()
        hardwareGrid = QtGui.QGridLayout()

        # ----------------- THE DATA! ---------------------
        # machineDataArray - based on the data passed in
        #
        # Template, each entry - [ bladeNum, bladeState, [ cpuRate, memoryRate, rx, tx ] ]  
        #dynamicInfo = [ [ '1', 0, [ 100, 10, '85KB', '100KB' ], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ '2', 1, [ 100, 10, '85KB', '100KB' ], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ '3', 1, [ 100, 10, '85KB', '100KB' ], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ '4', 2, [ 100, 10, '85KB', '100KB' ], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ '5', 1, [ 100, 10, '85KB', '100KB' ], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ '6', 1, [ 100, 10, '85KB', '100KB' ], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ '7', 1, [ 100, 10, '85KB', '100KB' ], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ '8', 1, [ 100, 10, '85KB', '100KB' ], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ '9', 1, [ 100, 10, '85KB', '100KB' ], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ '10', 1, [ 100, 10, '85KB', '100KB' ], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ '11', 1, [ 100, 10, '85KB', '100KB' ], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ '12', 1, [ 100, 10, '85KB', '100KB' ], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ '13', 1, [ 100, 10, '85KB', '100KB' ], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ '14', 1, [ 100, 10, '85KB', '100KB' ], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ 'AMM', 1, [], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ 'SWITCH\nMODULE\n001', 1, [], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ 'SWITCH\nMODULE\n002', 1, [], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ],
        #                [ 'MEDIA\nTRAY', 1, [], ['ON', 'PING-ABLE', 'SSH-ABLE', 'NO ERRORS'] ] ]

        j = 0 # Check for the first 14 blades
        k = 0 # Incrementor
        machineDataArray = data[3] 
        mediaTrayAssignment = data[3][0][0] # NEEDS TO BE UPDATED (PLACEHOLDER)
        for i in machineDataArray:
            if (j < 14):
                button = self.makeHardwareButton(i[0], i[1], 43, 300, i, i[3])
                bladeGrid.addWidget(button, 0, j)
                j = j + 1
            else:
                if ('ADVANCED' in i[0]):
                    button = self.makeHardwareButton(i[0], i[1], 169, 135, i, i[3])
                elif ('SWITCH' in i[0]):
                    button = self.makeHardwareButton(i[0], i[1], 169, 135, i, i[3])
                elif ('MEDIA' in i[0]):
                    # MUST CHANGE: Defaulting to giving the first blade in a blade center as the
                    # assignment of the media tray. When the back end is implemented, this value
                    # will need to be changed to whatever the media tray gives back for its assignment 
                    button = self.makeHardwareButton(i[0], i[1], 169, 135, machineDataArray, i[3])
                # else: Throw an error
                hardwareGrid.addWidget(button, 0, k)
                k = k + 1

        # -------------Matryoshka Assembly!---------------------
        # Widgets: should each be contained in a layout
        # Layouts: each get added to the main layout
        self.layout.addLayout(topBarLayout)
        self.layout.addLayout(bladeGrid)
        self.layout.addLayout(hardwareGrid)

        # Finalize layout of window and show 
        self.setLayout(self.layout)
        self.move(300, 150)
        self.setWindowTitle('BLADE CENTER VIEW')
        self.setGeometry(50, 50, 700, 500)
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = TopoBCenterLevel()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
