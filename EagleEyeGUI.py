import sys
from PyQt4 import QtGui,QtCore

'''
Team Eagle Eye, GUI for Recieve-Only EarthStation
Allows user to select from list of downloaded Satellite information,
which can be uploaded to Orbitron (open sourced Satellite tracking software,
http://www.stoff.pl) Additionally, this GUI will open a motor control interface
developed by http://www.vk5dj.com/remote.html - which will control our antenna
David Franklin, Senior Design, Embry-Riddle Aeronautical University
Spring 2014
'''

#basic layout idea from http://stackoverflow.com/questions/6792862/pyqt-qscrollarea-not-scrolling

class EagleEye_GUI(QtGui.QWidget):
    def __init__(self):
        super(EagleEye_GUI, self).__init__()
        self.horizontalLayout = QtGui.QVBoxLayout(self)
        
        satLabel = QtGui.QLabel('This label will eventually display useful Satellite information including AZ/EL', self)
        self.horizontalLayout.addWidget(satLabel)
        satLabel.setWordWrap(True)

        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 280))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.gridLayout = QtGui.QGridLayout()
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.satBtn = QtGui.QPushButton("Find Satellites")

        #This will eventually open Orbitron
        self.OrbBtn = QtGui.QPushButton("Open Orbitron")

        #This will eventually the Orbitron Interface
        self.OrbIntBtn = QtGui.QPushButton("Open Motor Interface")
        
        self.horizontalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.satBtn)
        self.horizontalLayout.addWidget(self.OrbBtn)
        self.horizontalLayout.addWidget(self.OrbIntBtn)

        #This will eventually trigger a web parser to get satellite data
        self.satBtn.clicked.connect(self.findSats)
        self.OrbBtn.clicked.connect(self.openOrb)
        self.OrbIntBtn.clicked.connect(self.openInterface)
        self.setGeometry(300, 200, 500, 500)
        self.setWindowTitle('Team Eagle Eye: Recieve-Only EarthStation')
        
    #This will eventually parse an HTML page containing Satellite data and display as List
    def findSats(self):
        for i in range(0, 50):
            
            self.r_button = QtGui.QPushButton("Satellite Name #### %s " % i)
            self.gridLayout.addWidget(self.r_button)

    #This function will eventually open Orbitron        
    def openOrb(self):
        print ("This is where orbitron will open eventually")

    #This function will eventually open the Orbitron Motor Control Interface
    def openInterface(self):
        print("This is where the motor interface will open eventually")

def run():

    app = QtGui.QApplication(sys.argv)
    ex = EagleEye_GUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()