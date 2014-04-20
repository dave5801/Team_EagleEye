import os.path

class Reader(object):

	def __init__(self):	
		self.contents  = ''
		

	def Read_TLE(self,sat_name): 
		
		name = sat_name
		print "SAT NAME TEST: " +name

		#with open('Custom_TLE.txt') as f:
		with open('Custom_TLE.txt') as f:
			tle_reader = f.read().replace('\r', '').split("\n")
			
       
		#add a 0 to satellite name to parse the actual text file 
		print "OPEN ends"
		tle_list = []
		zero = "0 "
		tle_line_o = (zero + sat_name.upper()).replace('\n', '')
		index = tle_reader.index(tle_line_o)

		zero_line, first_line, second_line = tle_reader[index:index+3]
 
		tle_list.append(zero_line)
		tle_list.append(first_line)
		tle_list.append(second_line)

		print "PRINT TLE LIST"
		print tle_list

		sat_pc_path = "C:\Users\TeamEagleEye\AppData\Roaming\SatPC32\Kepler"
		file_name = os.path.join(sat_pc_path, "TLE_Output.txt")
		with open(file_name, "w") as text_file:
			for item in tle_list:
				text_file.write("%s\n" % item)

		print "TLE LIST PARSED: "
		print tle_list
		return tle_list

	def SAT_BIO(self, sat_name): 
		
		with open("Satellite_Database_Line_Limited-3.txt") as f:
			#bio_read = f.read().split("\r\n")
			bio_read = f.read().replace('\r', '').split("\n")
			#print bio_read

		bio_list = []
		index = bio_read.index(sat_name)

		line1, line2, line3 = bio_read[index:index+3]
 
		bio_list.append(line1)
		bio_list.append(line2)
		bio_list.append(line3)

		return bio_list


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
	
