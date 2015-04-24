from mechanize import Browser  
import urllib2
from BeautifulSoup import BeautifulSoup

data = open('Docket.html')

soup = BeautifulSoup(data)
results_table = soup.find('table', attrs={'class': 'detailRecordTable'})

output = []

for tr in results_table.findAll('tr'):
	output_row = []

	for td in tr.findAll('b'):
		data = td.text

		output_row.append(data)
		output.append(output_row)

		print output
		print len(output)
		if len(output) > '107':
			print 'There is a new entry today.'
