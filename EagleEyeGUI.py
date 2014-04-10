import sys
from PyQt4 import QtGui,QtCore
from heavens_above_parser_class import Parser
from Sat_Reader import Reader
import subprocess

'''
Team Eagle Eye, GUI for Recieve-Only EarthStation
Allows user to select from list of downloaded Satellite information,
which can be uploaded to SATPC32 (open sourced Satellite tracking software,
http://www.dk1tb.de/) Additionally, this GUI will open a motor control interface
developed by http://www.vk5dj.com/remote.html - which will control our antenna
David Franklin, Senior Design, Embry-Riddle Aeronautical University
Spring 2014
'''

'''
MAIN Gui layout
'''

class EagleEye_GUI(QtGui.QWidget, Reader):
    def __init__(self):
        super(EagleEye_GUI, self).__init__()
        self.horizontalLayout = QtGui.QVBoxLayout(self)
        
        self.satLabel = QtGui.QLabel('', self)
        self.horizontalLayout.addWidget(self.satLabel)
        self.satLabel.setWordWrap(True)

        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 280))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.gridLayout = QtGui.QGridLayout()
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.satBtn = QtGui.QPushButton("Find Satellites")
        
        self.horizontalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.satBtn)

        #This will eventually trigger a web parser to get satellite data
        self.satBtn.clicked.connect(self.findSats)
        #self.OrbIntBtn.clicked.connect(self.openInterface)
        self.setGeometry(300, 200, 500, 500)
        self.setWindowTitle('Team Eagle Eye: Recieve-Only EarthStation')

        #define parser class
        self.url = url
        self.parser = Parser(url)
        parse_list = [] 
        self.tle_list = []
        self.tle_line_o = ""
        self.text_file = open("TLE_Output.txt", "w")
        self.name = ' '
        
    '''
    This function parses an HTML page containing Satellite data and display as List
    It is called when 'Find Satellites' Button is pressed
    '''
   
    def findSats(self):

        parse_list = self.parser.download_page()
        
        print parse_list

        #populate list of buttons with satellites
        for i in range(len(parse_list)):
                
            self.r_button = QtGui.QPushButton(parse_list[i])
            self.gridLayout.addWidget(self.r_button)
            self.r_button.clicked.connect(self.list_btn)
            
            
            try:    
                self.tle_line_o = "0 " + parse_list[i]
            
            except ValueError:
                print parse_list[i] + " not in the list"
            except:
                print "Unexpected Error"
            
    

    '''

    This function will display parses an individual satellites TLE from a TLE master list
    It will also write TLE directly to SATPC32 
    It will open SATPC32 
    And finally it will provide a satellites' name, country, and purpose

    '''


    def list_btn(self):
     
        sender = self.sender()
        sat_string = sender.text()
        
        #Get TLE info and basic info to confirm Satellite's identity
        try:
            print sat_string
            print ' '
            tle_label = self.Read_TLE(sat_string)
            bio_label = self.SAT_BIO(sat_string)
            self.satLabel.setText('Satellite: ' +bio_label[0] + '\nCountry: ' +bio_label[1]+ '\nPurpose: ' +bio_label[2])
            print bio_label[0]
            print bio_label[1]
            print bio_label[2]
        except ValueError:
                print sat_string + " not in the list"
                self.satLabel.setText('No Two Line Element data available. Please Try again')

        except:
            print "Unexpected Error"
        print("TEST")

        #open SATPC32 executable file
        subprocess.call(["C:\Program Files (x86)\SatPC32\SatPC32.exe"])


'''
Function to run the GUI

'''
def run():

    app = QtGui.QApplication(sys.argv)
    ex = EagleEye_GUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    url = "http://www.heavens-above.com/AllSats.aspx?lat=29.2108&lng=-81.0228&loc=Daytona+Beach&alt=4&tz=EST"
    run()