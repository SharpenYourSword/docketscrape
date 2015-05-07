from mechanize import Browser  
import urllib2, csv, os
from BeautifulSoup import BeautifulSoup
from apscheduler.scheduler import Scheduler

sched = Scheduler()
sched.start()

# data = open('Docket.html')

html = urllib2.urlopen('https://www.courts.mo.gov/casenet/cases/searchDockets.do?inputVO.caseNumber=14BA-CV01093&inputVO.courtId=CT13').read()

# br = Browser()
# br.open(url)

soup = BeautifulSoup(html)
results_table = soup.find('table', attrs={'class': 'detailRecordTable'})

output = []

if os.path.isfile('current.csv'):
	os.rename('current.csv', 'previous.csv')

for tr in results_table.findAll('tr'):
	output_row = []

	for td in tr.findAll('b'):
		data = td.text

		output_row.append(data)
		output.append(output_row)

with open('current.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter='|')
	writer.writerows(output)

with open('current.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter='|')
	cur_row_count = sum(1 for row in reader)
	print 'Current count:'
	print cur_row_count

with open('previous.csv', 'r') as csvfile: 
	reader = csv.reader(csvfile, delimiter='|')
	prev_row_count = sum(1 for row in reader)
	print "Previous count:"
	print prev_row_count

if cur_row_count > prev_row_count:
	print 'Good morning. There is a new entry in case number 14BA-CV01093 today.'
elif cur_row_count == prev_row_count:
	print 'Good morning. There are no new entries in case number 14BA-CV01093 today.'
