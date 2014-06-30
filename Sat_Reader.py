import os.path

'''
Team Eagle Eye SAT READER class for EagleEyeGUI. 
Reads TLE master list and parses two line element data on a selected satellite
Returns an individual satellites TLE data
Code by: David Franklin, Senior Design, Spring 2014
'''



#Main Class
class Reader(object):

	def __init__(self):	
		self.contents  = ''
		


		'''

		This function read in satellite name and parses individual TLE data
		from TLE master list. It then writes a text file containing the individual TLE
		to SATPC32.

		'''

	def Read_TLE(self,sat_name): 
		
		name = sat_name
		

		#open TLE Master List
		with open('Custom_TLE.txt') as f:
			tle_reader = f.read().replace('\r', '').split("\n")
			
       
		#add a 0 to satellite name to parse the actual text file 
		#Each satellite name is on the 0-th line of TLE
		#thats why they need a zero.
		print "OPEN ends"
		tle_list = []
		zero = "0 "
		tle_line_o = (zero + sat_name.upper()).replace('\n', '')
		index = tle_reader.index(tle_line_o)

		#get the lines of TLE
		zero_line, first_line, second_line = tle_reader[index:index+3]
 
		tle_list.append(zero_line)
		tle_list.append(first_line)
		tle_list.append(second_line)

		
		#Write to SATPC32
		sat_pc_path = "C:\Users\TeamEagleEye\AppData\Roaming\SatPC32\Kepler"
		file_name = os.path.join(sat_pc_path, "TLE_Output.txt")
		with open(file_name, "w") as text_file:
			for item in tle_list:
				text_file.write("%s\n" % item)

		
		return tle_list


		'''
		This function gets a Satellite's name, country, and purpose
		and displays after the satellite has been selected
		it works the same way as Read_TLE()

		'''

	def SAT_BIO(self, sat_name): 

		#Open Satellite information file
		
		with open("Satellite_Database_Line_Limited-3.txt") as f:
			
			bio_read = f.read().replace('\r', '').split("\n")
	

		bio_list = []
		index = bio_read.index(sat_name)

		line1, line2, line3 = bio_read[index:index+3]
 
		bio_list.append(line1)
		bio_list.append(line2)
		bio_list.append(line3)

		return bio_list

##this is a test method where it injects values to verify proper outputs
if __name__ == '__main__':

	#test case
	sat = "METEOR-M"
	list1 = []
	Read1 = Reader()
	list1 = Read1.Read_TLE(sat)
	for i in range(len(list1)):
		print list1[i]
	print ' '
	#print Read1.SAT_BIO(sat)
	
