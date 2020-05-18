import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd


def load_page_content(url):	
	#url = 'https://vnexpress.net/dai-hoc-quoc-gia-tp-hcm-to-chuc-mot-dot-danh-gia-nang-luc-4100144.html'
	uClient = uReq(url)

	page_html = uClient.read()

	uClient.close()

	page_soup = soup(page_html,"html.parser")

	page_content = ''

	containers = page_soup.findAll("p",{"class":"description"})

	for string in containers:
		page_content = page_content + ' ' + string.get_text()

	containers = page_soup.findAll("p",{"class":"Normal"})

	for string in containers:
		page_content = page_content + ' ' + string.get_text()

	return page_content


txt_file = ['giao-duc-link.txt','phap-luat-link.txt','suc-khoe-link.txt']
all_contents = []
label = []
data = {}
i = 0
for file in txt_file:
	with open(file,'r') as f:
		print(file)
		for link in f:

			print(link.strip())

			page_content = load_page_content(link.strip())

			all_contents.append(page_content)
			label.append(i)
	i += 1

data['datas'] = all_contents
data['labels'] = label
df = pd.DataFrame.from_dict(data)
print(df.head())
df.to_csv('test', sep='\t', encoding='utf-8')