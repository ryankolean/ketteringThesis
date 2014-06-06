#!/usr/bin/python2

import sys
from PyQt4 import QtGui, QtCore 

from clusterLCCAControl import LCCAControl
from clusterManageNodeControl import ClusterNodeControl
from clusterRTOP import RtopPanel

from clusterData import ClusterData

class TopoClusterLevel(QtGui.QWidget):
    def __init__(self):
        super(TopoClusterLevel, self).__init__()
        self.font = QtGui.QFont()
        self.initUI()

    def slotLCCA(self):
         self.lccaControl = LCCAControl()
         self.lccaControl.exec_()

    def slotClusterNode(self):
        self.clusterNodeControl = ClusterNodeControl()
        self.clusterNodeControl.exec_()

    def slotRtop(self):
        self.Rtop = RtopPanel()
        self.Rtop.exec_()

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

    def makeHardwareButton(self, label, tooltip, state, sizeX, sizeY, drillDownData):
        button = QtGui.QPushButton(label)
        button.setToolTip(tooltip)
        button.setMinimumSize(sizeX, sizeY)
        self.font.setBold(True)
        button.setFont(self.font)
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
        return button

    def makeBCButton(self, machine, rack, state,  sizeX, sizeY, drillDownData, firstBlade, lastBlade):
        if ('001' in machine):
            whichBlades = 'Blade Center 1: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc1Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc1Button, rack)
        elif ('002' in machine):
            whichBlades = 'Blade Center 2: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc2Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc2Button, rack)
        elif ('003' in machine):
            whichBlades = 'Blade Center 3: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc3Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc3Button, rack)
        elif ('004' in machine):
            whichBlades = 'Blade Center 4: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc4Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc4Button, rack)
        elif ('005' in machine):
            whichBlades = 'Blade Center 5: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc5Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc5Button, rack)
        elif ('006' in machine):
            whichBlades = 'Blade Center 6: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc6Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc6Button, rack)
        elif ('007' in machine):
            whichBlades = 'Blade Center 7: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc7Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc7Button, rack)
        elif ('008' in machine):
            whichBlades = 'Blade Center 8: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc8Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc8Button, rack)
        elif ('009' in machine):
            whichBlades = 'Blade Center 9: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc9Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc9Button, rack)
        elif ('010' in machine):
            whichBlades = 'Blade Center 10: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc10Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc10Button, rack)
        elif ('011' in machine):
            whichBlades = 'Blade Center 11: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc11Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc11Button, rack)
        elif ('012' in machine):
            whichBlades = 'Blade Center 12: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc12Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc12Button, rack)
        elif ('013' in machine):
            whichBlades = 'Blade Center 13: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc13Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc13Button, rack)
        elif ('014' in machine):
            whichBlades = 'Blade Center 14: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc14Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc14Button, rack)
        elif ('015' in machine):
            whichBlades = 'Blade Center 15: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc15Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc15Button, rack)
        elif ('016' in machine):
            whichBlades = 'Blade Center 16: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc16Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc16Button, rack)
        elif ('017' in machine):
            whichBlades = 'Blade Center 17: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc17Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc17Button, rack)
        elif ('018' in machine):
            whichBlades = 'Blade Center 18: Blades %i-%i' % (firstBlade, lastBlade)
            self.bc18Button = self.makeHardwareButton(machine, whichBlades, state, sizeX, sizeY, drillDownData)
            self.placeBCButton(self.bc18Button, rack)


    def placeBCButton(self, button, rack):
        if (rack == 1):
            self.rack1Layout.addWidget(button)
        elif (rack == 2):
            self.rack2Layout.addWidget(button)
        elif (rack == 3):
            self.rack3Layout.addWidget(button)

    def initUI(self):
        # This will be used to to set the window's layout
        self.layout = QtGui.QVBoxLayout()

        # Make the top nav bar for switching views and opening rtop
        topBarLayout = QtGui.QHBoxLayout()
        topBarFrame = QtGui.QFrame()
        topBarFrame.setFrameShape(QtGui.QFrame.StyledPanel)

        self.rtopButton = self.makeActionButton('RTOP', 'Launch blade, LCCA,\nand management node\nmonitor utility', 330, 60)
        self.rtopButton.clicked.connect(self.slotRtop)

        topBarLayout.addWidget(self.rtopButton)
        topBarFrame.setLayout(topBarLayout)

        hardwareLayout = QtGui.QHBoxLayout()
        self.hardwareList = ClusterData.managementNodeData

        for i in self.hardwareList:
            if ('LCCA' in i[0]):
                lccaButton = self.makeHardwareButton(i[0], 'Open LCCA Control Panel', i[1], 130, 440, i[2])
                lccaButton.clicked.connect(self.slotLCCA)
            else:
                clusterManageButton = self.makeHardwareButton(i[0], 'Open Cluster Management Control Panel', i[1], 130, 440, i[2])
                clusterManageButton.clicked.connect(self.slotClusterNode)
        # Placement requires that the Cluster Management button be placed farthest left.
        # followed by the LCCA and then the Blade Racks with the Blade Center buttons stacked vertically
        hardwareLayout.addWidget(clusterManageButton)
        hardwareLayout.addWidget(lccaButton)
        #lccaButton.clicked.connect(lambda: self.slotLCCA(*PASS DATA THROUGH HERE*))
        #clusterManagementButton.clicked.connect(lambda: self.slotClusterNode(*PASS DATA THROUGH HERE*))

        self.rack1Layout = QtGui.QVBoxLayout()
        rack1Frame = QtGui.QFrame()
        rack1Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.rack2Layout = QtGui.QVBoxLayout()
        rack2Frame = QtGui.QFrame()
        rack2Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.rack3Layout = QtGui.QVBoxLayout()
        rack3Frame = QtGui.QFrame()
        rack3Frame.setFrameShape(QtGui.QFrame.StyledPanel)

        self.rackData = ClusterData.topographData

        sizeX = 115
        sizeY = 65
        for i in self.rackData:
            #self.makeBCButton(machine, rack, state, sizeX, sizeY, drilldownData, firstBlade, lastBlade)
            self.makeBCButton(i[0], i[1], i[2], sizeX, sizeY, i[3], i[4], i[5])

        rack1Frame.setLayout(self.rack1Layout)
        rack2Frame.setLayout(self.rack2Layout)
        rack3Frame.setLayout(self.rack3Layout)
        hardwareLayout.addWidget(rack1Frame)
        hardwareLayout.addWidget(rack2Frame)
        hardwareLayout.addWidget(rack3Frame)

        # Pack widgets and layouts
        self.layout.addWidget(topBarFrame)
        self.layout.addLayout(hardwareLayout)

        # Finalize layout of window and show 
        self.setLayout(self.layout)
        self.move(300, 150)
        self.setWindowTitle('CLUSTER MAIN VIEW')
        self.setGeometry(50, 50, 725, 500)
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = TopoClusterLevel()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
