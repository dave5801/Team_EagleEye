class Reader(object):

	def __init__(self):	
		self.contents  = ''


	def Read_TLE(self): 
		
		with open('Custom_TLE.txt') as f:
			stuff = f.read().split('\r\n')

		tle_list = []
		zero = '0 '
		sat = 'COSMOS 1174'
		tle_line_o = zero + sat
		index = stuff.index(tle_line_o)

		zero_line, first_line, second_line = stuff[index:index+3]
 
		tle_list.append(zero_line)
		tle_list.append(first_line)
		tle_list.append(second_line)

		text_file = open("TLE_Output.txt", "w")

		for item in tle_list:
			text_file.write("%s\n" % item)

		text_file.close()

		return tle_list

	def SAT_BIO(self): 
		
		with open('Satellite_Database_Line_Limited-3.txt') as f:
			bio_read = f.read().split('\r\n')

		#print stuff
		bio_list = []
		#sat = 'BRIXAS'
		bio_name = "TRMM"
		index = bio_read.index(bio_name)

		line1, line2, line3 = bio_read[index:index+3]
 
		bio_list.append(line1)
		bio_list.append(line2)
		bio_list.append(line3)

		return bio_list

if __name__ == '__main__':

	list1 = []
	Read1 = Reader()
	list1 = Read1.Read_TLE()
	#print list1
	for i in range(len(list1)):
		print list1[i]
	print ' '
	print Read1.SAT_BIO()
