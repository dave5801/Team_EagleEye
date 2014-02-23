'''
Parses website Heavens Above for daily predictions of brighter satellites for Daytona Beach
Code by: David Franklin, Team Eagle Eye, Senior Design, Embry-Riddle Aeronautical University
Spring 2014

'''

from BeautifulSoup import BeautifulSoup
import urllib2

class parser(object):

				def __init__(self, url):
                			
                			self.url = url
                			self.contents  = ''
                	
    				def download_page(self):
    			
    					#open the page
						page=urllib2.urlopen(self.url)
						soup = BeautifulSoup(page.read())

						page_find=soup.findAll('td')
						
						#lists for storing page data and satellite names
						page_list = []
						sat_names = []

						#Store HTML table data into list
						for page_data in page_find:
   							 page_list.append(page_data.string)
   						

   						#range function to count by 11s through the page's table data
   						#satellite names occur at specific location on table data and occur at every eleventh element
   						def my_range(start, end, step):
    							while start <= end:
        							yield start
        							start += step

        					#count by 11s from the 36th element - which is the first satellite name
        					for index in my_range(36, len(page_list)-1, 11):

    							#add the names from page_list to this list
    							sat_names.append(page_list[index])
    
						print sat_names

if __name__ == '__main__':
		url = "http://www.heavens-above.com/AllSats.aspx?lat=29.2108&lng=-81.0228&loc=Daytona+Beach&alt=4&tz=EST"
		parser = parser(url)
		parser.download_page()
		

