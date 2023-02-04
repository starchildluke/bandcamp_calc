import requests
from bs4 import BeautifulSoup
import datetime
import argparse

# Create CL argument for URLs
parser = argparse.ArgumentParser(description=None)
parser.add_argument("-u", "--url", type=str)
args = parser.parse_args()
url = args.url

# Empty list for track lengths
tm = []

# Extract times from release page
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
times_list = soup.find_all('span', attrs={'class':'time secondaryText'})
cleaned_up_times_list = [time.text.replace('\n','').replace(' ','') for time in times_list]

# Convert and add times to `tm` list
for t in cleaned_up_times_list:
	(m, s) = t.split(':')
	d = datetime.timedelta(minutes=int(m), seconds=int(s))
	tm.append(d)

# Sum and print total length
total_time = sum(tm, start=datetime.timedelta())
print(f'Total length: {total_time}')