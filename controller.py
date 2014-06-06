#!/usr/bin/python2

import sys
from PyQt4 import QtGui, QtCore

from clusterTopoClusterLevel import TopoClusterLevel
from clusterTopoBCenterLevel import TopoBCenterLevel

class Controller(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Controller, self).__init__(parent)

        # Make the stacked widget to house all the other widgets
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        # MAKE A STATE MACHINE
        # Set up a state machina for the Topo Widgets.
        # used to move back and forth between topo view and issue view widgets
        
        # Make the first widget that will be set at start-up 
        topoClusterView = TopoClusterLevel()
        # After Making the widget you can still call any of the objects, ex buttons, and set actions for them
        topoClusterView.bc1Button.clicked.connect(lambda: self.bc1Slot(topoClusterView.rackData[5]))
        topoClusterView.bc2Button.clicked.connect(lambda: self.bc2Slot(topoClusterView.rackData[4]))
        topoClusterView.bc3Button.clicked.connect(lambda: self.bc3Slot(topoClusterView.rackData[3]))
        topoClusterView.bc4Button.clicked.connect(lambda: self.bc4Slot(topoClusterView.rackData[2]))
        topoClusterView.bc5Button.clicked.connect(lambda: self.bc5Slot(topoClusterView.rackData[1]))
        topoClusterView.bc6Button.clicked.connect(lambda: self.bc6Slot(topoClusterView.rackData[0]))
        topoClusterView.bc7Button.clicked.connect(lambda: self.bc7Slot(topoClusterView.rackData[11]))
        topoClusterView.bc8Button.clicked.connect(lambda: self.bc8Slot(topoClusterView.rackData[10]))
        topoClusterView.bc9Button.clicked.connect(lambda: self.bc9Slot(topoClusterView.rackData[9]))
        topoClusterView.bc10Button.clicked.connect(lambda: self.bc10Slot(topoClusterView.rackData[8]))
        topoClusterView.bc11Button.clicked.connect(lambda: self.bc11Slot(topoClusterView.rackData[7]))
        topoClusterView.bc12Button.clicked.connect(lambda: self.bc12Slot(topoClusterView.rackData[6]))
        topoClusterView.bc13Button.clicked.connect(lambda: self.bc13Slot(topoClusterView.rackData[17]))
        topoClusterView.bc14Button.clicked.connect(lambda: self.bc14Slot(topoClusterView.rackData[16]))
        topoClusterView.bc15Button.clicked.connect(lambda: self.bc15Slot(topoClusterView.rackData[15]))
        topoClusterView.bc16Button.clicked.connect(lambda: self.bc16Slot(topoClusterView.rackData[14]))
        topoClusterView.bc17Button.clicked.connect(lambda: self.bc17Slot(topoClusterView.rackData[13]))
        topoClusterView.bc18Button.clicked.connect(lambda: self.bc18Slot(topoClusterView.rackData[12]))
        # Add the widget we created to the central widget that houses all the widgets
        self.central_widget.addWidget(topoClusterView)
        self.central_widget.setCurrentWidget(topoClusterView)
        self.setWindowTitle('CLUSTER HARDWARE MAIN VIEW')

    # TOPOGRAH VIEW - this is the main view of this app (!!THIS IS A COPY OF THE ABOVE CODE!!)
    def topoClusterSlot(self):
        topoClusterView = TopoClusterLevel()
        topoClusterView.bc1Button.clicked.connect(lambda: self.bc1Slot(topoClusterView.rackData[5]))
        topoClusterView.bc2Button.clicked.connect(lambda: self.bc2Slot(topoClusterView.rackData[4]))
        topoClusterView.bc3Button.clicked.connect(lambda: self.bc3Slot(topoClusterView.rackData[3]))
        topoClusterView.bc4Button.clicked.connect(lambda: self.bc4Slot(topoClusterView.rackData[2]))
        topoClusterView.bc5Button.clicked.connect(lambda: self.bc5Slot(topoClusterView.rackData[1]))
        topoClusterView.bc6Button.clicked.connect(lambda: self.bc6Slot(topoClusterView.rackData[0]))
        topoClusterView.bc7Button.clicked.connect(lambda: self.bc7Slot(topoClusterView.rackData[11]))
        topoClusterView.bc8Button.clicked.connect(lambda: self.bc8Slot(topoClusterView.rackData[10]))
        topoClusterView.bc9Button.clicked.connect(lambda: self.bc9Slot(topoClusterView.rackData[9]))
        topoClusterView.bc10Button.clicked.connect(lambda: self.bc10Slot(topoClusterView.rackData[8]))
        topoClusterView.bc11Button.clicked.connect(lambda: self.bc11Slot(topoClusterView.rackData[7]))
        topoClusterView.bc12Button.clicked.connect(lambda: self.bc12Slot(topoClusterView.rackData[6]))
        topoClusterView.bc13Button.clicked.connect(lambda: self.bc13Slot(topoClusterView.rackData[17]))
        topoClusterView.bc14Button.clicked.connect(lambda: self.bc14Slot(topoClusterView.rackData[16]))
        topoClusterView.bc15Button.clicked.connect(lambda: self.bc15Slot(topoClusterView.rackData[15]))
        topoClusterView.bc16Button.clicked.connect(lambda: self.bc16Slot(topoClusterView.rackData[14]))
        topoClusterView.bc17Button.clicked.connect(lambda: self.bc17Slot(topoClusterView.rackData[13]))
        topoClusterView.bc18Button.clicked.connect(lambda: self.bc18Slot(topoClusterView.rackData[12]))
        self.central_widget.addWidget(topoClusterView)
        self.central_widget.setCurrentWidget(topoClusterView)
        self.setWindowTitle('CLUSTER HARDWARE MAIN VIEW')

    # THESE ARE ALL THE DIFFERENT BLADE CENTERS SLOTS
    def bc1Slot(self, data):
        topoBCenter1View = TopoBCenterLevel(data)
        topoBCenter1View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter1View)
        self.central_widget.setCurrentWidget(topoBCenter1View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 001')
    def bc2Slot(self, data):
        topoBCenter2View = TopoBCenterLevel(data)
        topoBCenter2View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter2View)
        self.central_widget.setCurrentWidget(topoBCenter2View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 002')
    def bc3Slot(self, data):
        topoBCenter3View = TopoBCenterLevel(data)
        topoBCenter3View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter3View)
        self.central_widget.setCurrentWidget(topoBCenter3View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 003')
    def bc4Slot(self, data):
        topoBCenter4View = TopoBCenterLevel(data)
        topoBCenter4View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter4View)
        self.central_widget.setCurrentWidget(topoBCenter4View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 004')
    def bc5Slot(self, data):
        topoBCenter5View = TopoBCenterLevel(data)
        topoBCenter5View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter5View)
        self.central_widget.setCurrentWidget(topoBCenter5View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 005')
    def bc6Slot(self, data):
        topoBCenter6View = TopoBCenterLevel(data)
        topoBCenter6View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter6View)
        self.central_widget.setCurrentWidget(topoBCenter6View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 006')
    def bc7Slot(self, data):
        topoBCenter7View = TopoBCenterLevel(data)
        topoBCenter7View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter7View)
        self.central_widget.setCurrentWidget(topoBCenter7View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 007')
    def bc8Slot(self, data):
        topoBCenter8View = TopoBCenterLevel(data)
        topoBCenter8View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter8View)
        self.central_widget.setCurrentWidget(topoBCenter8View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 008')
    def bc9Slot(self, data):
        topoBCenter9View = TopoBCenterLevel(data)
        topoBCenter9View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter9View)
        self.central_widget.setCurrentWidget(topoBCenter9View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 009')
    def bc10Slot(self, data):
        topoBCenter10View = TopoBCenterLevel(data)
        topoBCenter10View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter10View)
        self.central_widget.setCurrentWidget(topoBCenter10View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 010')
    def bc11Slot(self, data):
        topoBCenter11View = TopoBCenterLevel(data)
        topoBCenter11View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter11View)
        self.central_widget.setCurrentWidget(topoBCenter11View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 011')
    def bc12Slot(self, data):
        topoBCenter12View = TopoBCenterLevel(data)
        topoBCenter12View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter12View)
        self.central_widget.setCurrentWidget(topoBCenter12View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 012')
    def bc13Slot(self, data):
        topoBCenter13View = TopoBCenterLevel(data)
        topoBCenter13View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter13View)
        self.central_widget.setCurrentWidget(topoBCenter13View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 013')
    def bc14Slot(self, data):
        topoBCenter14View = TopoBCenterLevel(data)
        topoBCenter14View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter14View)
        self.central_widget.setCurrentWidget(topoBCenter14View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 014')
    def bc15Slot(self, data):
        topoBCenter15View = TopoBCenterLevel(data)
        topoBCenter15View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter15View)
        self.central_widget.setCurrentWidget(topoBCenter15View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 015')
    def bc16Slot(self, data):
        topoBCenter16View = TopoBCenterLevel(data)
        topoBCenter16View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter16View)
        self.central_widget.setCurrentWidget(topoBCenter16View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 016')
    def bc17Slot(self, data):
        topoBCenter17View = TopoBCenterLevel(data)
        topoBCenter17View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter17View)
        self.central_widget.setCurrentWidget(topoBCenter17View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 017')
    def bc18Slot(self, data):
        topoBCenter18View = TopoBCenterLevel(data)
        topoBCenter18View.backButton.clicked.connect(self.topoClusterSlot)
        self.central_widget.addWidget(topoBCenter18View)
        self.central_widget.setCurrentWidget(topoBCenter18View)
        self.setWindowTitle('CLUSTER HARDWARE - BLADE CENTER 018')


if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = Controller()
    window.show()
    app.exec_()
