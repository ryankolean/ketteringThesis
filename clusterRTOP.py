#!/usr/bin/python2

import sys
from PyQt4 import QtGui, QtCore

class RtopPanel(QtGui.QDialog):

    def __init__(self):
        super(RtopPanel, self).__init__()
        self.font = QtGui.QFont()
        self.table = QtGui.QTableWidget()
        self.initUI()

    def closeClicked(self):
        self.close()
    
    def makeActionButton(self, name, tooltip, sizeX, sizeY):
        button = QtGui.QPushButton(name)
        button.setToolTip(tooltip)
        button.setMinimumSize(sizeX, sizeY)
        self.font.setBold(True)
        self.font.setPointSize(10)
        button.setFont(self.font)
        color = button.palette()
        color.setColor(button.backgroundRole(), QtGui.QColor(0,102,187))
        color.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255,255,255))
        button.setPalette(color)
        return button

    def initUI(self):
        # create high level layout for the window, everything is added to this
        self.layout = QtGui.QVBoxLayout()


        # bogus data
        rtopData = [ 'cluster: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'lcca: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade001: cpu=XX% mem=YY% rx=AAkb tx=BBkb',
                     'Blade002: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade003: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade004: cpu=XX% mem=YY% rx=AAkb tx=BBkb',
                     'Blade005: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade006: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade007: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade008: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade009: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade010: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade011: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade012: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade013: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade014: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade015: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade016: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade017: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade018: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade019: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade020: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade021: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade022: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade023: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade024: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade025: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade026: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade027: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade028: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade029: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade030: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade031: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade032: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade033: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade034: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade035: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade036: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade037: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade038: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade039: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade040: cpu=XX% mem=YY% rx=AAkb tx=BBkb',
                     'Blade041: cpu=XX% mem=YY% rx=AAkb tx=BBkb',
                     'Blade042: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade043: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade044: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade045: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade046: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade047: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade048: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade049: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade050: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade051: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade052: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade053: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade054: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade055: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade056: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade057: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade058: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade059: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade060: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade061: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade062: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade063: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade064: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade065: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade066: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade067: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade068: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade069: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade070: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade071: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade072: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade073: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade074: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade075: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade076: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade077: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade078: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade079: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade080: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade081: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade082: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade083: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade084: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade085: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade086: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade087: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade088: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade089: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade090: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade091: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade092: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade093: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade094: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade095: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade096: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade097: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade098: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade099: cpu=XX% mem=YY% rx=AAkb tx=BBkb', 
                     'Blade100: cpu=XX% mem=YY% rx=AAkb tx=BBkb' ]

        # Make the table and make it stretch to fit for the cells
        table = QtGui.QTableWidget()
        table.setMinimumSize(1250,400)
        hheader = table.horizontalHeader()
        vheader = table.verticalHeader()
        hheader.setResizeMode(QtGui.QHeaderView.Stretch)
        vheader.setResizeMode(QtGui.QHeaderView.Stretch)

        # Set up counter and endpount, this deals with automagically making columns and filling them even if there are empty spaces
        counter = 0
        endpoint = len(rtopData)

        # Setting up the grid using a check for columns that would have missing elements and adjusting for that
        numColumns = 5
        if len(rtopData) % numColumns == 0:
            numRows = len(rtopData) / 5
        else:
	    numRows = (len(rtopData) / 5) + 1
        table.setColumnCount(5)
        table.setRowCount(numRows)

        #Set the size font for the text in the grid.
        self.font.setPointSize(7)
        table.setFont(self.font)

        # This propicates the spreadsheet by columns
        for i in range(numColumns):
            for j in range(numRows):
                if counter == endpoint:
                    break
                else:
                    table.setItem(j, i, QtGui.QTableWidgetItem(rtopData[counter]))
                counter += 1
        self.layout.addWidget(table)

        # Add close button to the dialog window
        closeButton = self.makeActionButton('CLOSE', '', 1000, 25)
        closeButton.clicked.connect(self.closeClicked)
        self.layout.addWidget(closeButton) 

        # Finalize layout of window and display
        self.setLayout(self.layout)
        self.move(300, 150)
        self.setWindowTitle('RTOP INFO PANEL')
        self.setGeometry(5, 5, 1000, 850)
        self.show()

# Run as an independent application
def main():
    app = QtGui.QApplication(sys.argv)
    ex = RtopPanel()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
