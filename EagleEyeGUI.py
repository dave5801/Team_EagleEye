import sys
from PyQt4 import QtGui,QtCore

'''
Team Eagle Eye, GUI for Recieve-Only EarthStation
Allows user to select from list of downloaded Satellite information
This selection communicates azimuth and elevation to motor control, which tracks the Satellite
David Franklin, Senior Design, Embry-Riddle Aeronautical University
Spring 2014
'''

#basic layout idea from http://stackoverflow.com/questions/6792862/pyqt-qscrollarea-not-scrolling

class EagleEye_GUI(QtGui.QWidget):
    def __init__(self):
        super(EagleEye_GUI, self).__init__()
        self.horizontalLayout = QtGui.QVBoxLayout(self)
        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 280))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.gridLayout = QtGui.QGridLayout()
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.satBtn = QtGui.QPushButton("Find Satellites")

        #This will eventually cause the motor to perform callibration
        #by tracking the sun
        self.motorBtn = QtGui.QPushButton("Motor Callibration Test")
        self.horizontalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.satBtn)
        self.horizontalLayout.addWidget(self.motorBtn)

        #This will eventually trigger a web parser to get satellite data
        self.connect(self.satBtn, QtCore.SIGNAL("clicked()"), self.addButtons)
        self.setGeometry(300, 200, 500, 500)
        self.setWindowTitle('Team Eagle Eye: Recieve-Only EarthStation')
        

    def addButtons(self):
        for i in range(0, 50):
            #This will eventually parse an HTML page containing Satellite data and display as List
            self.r_button = QtGui.QPushButton("Satellite Name #### %s " % i)
            self.gridLayout.addWidget(self.r_button)
def run():

    app = QtGui.QApplication(sys.argv)
    ex = EagleEye_GUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()