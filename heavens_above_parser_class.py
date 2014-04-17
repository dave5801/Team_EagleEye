'''
Parses website Heavens Above for daily predictions of brighter satellites for Daytona Beach
Code by: David Franklin, Team Eagle Eye, Senior Design, Embry-Riddle Aeronautical University
Spring 2014

'''

from BeautifulSoup import BeautifulSoup
import urllib2
import re

'''
MAIN Class
'''
class Parser(object):

	#constructor
	def __init__(self, url):	
		self.url = url
		#self.contents  = ''
	
	'''	
	This function dowloads and parses main page
	'''
	def download_page(self):
		url = urllib2.urlopen(self.url)
		page_data = url.read()
		page_data = page_data.decode(url.headers['content-type'].split('charset=')[-1])
		page_data = page_data.encode('ascii', 'ignore')

		soup = BeautifulSoup(page_data)

		#satellite information to be parsed
		categories = [
			'brightness',
			'start_time',
			'start_altitude',
			'start_azimuth',
			'highest_point_time',
			'highest_point_altitude',
			'highest_point_azimuth',
			'end_time',
			'end_altitude',
			'end_azimuth'
		]

		satellites = {}

		#go through table rows (tr) and table data (td) and find satellite data
		for tr in soup.findAll('tr'):
			if tr.has_key('class') and'clickableRow' in tr.get('class'):
				sat = {}
				trs = map(lambda x: str(x.text), tr.findAll('td'))
				for cat, td in zip(categories, trs[1:]):
					sat[cat] = td
				
				#use regular expression to eliminated Rocket Bodies (R/B) and space debris(DEB)	
				if not re.search(r'\s(R/B|DEB|Rocket|rocket|Rocket1)*(?:\([^\)]+\))?\s*\Z', trs[0]):
					satellites[trs[0]] = sat

		#get satellite names			
		sat_list = satellites.keys()

		return sat_list


if __name__ == '__main__':

	#heavens above url - website which provides daily prediction for specified location
	url = "http://www.heavens-above.com/AllSats.aspx?lat=29.2108&lng=-81.0228&loc=Daytona+Beach&alt=4&tz=EST"
	Parser = Parser(url)
	print Parser.download_page()
		