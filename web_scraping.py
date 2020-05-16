import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# chcp 65001
# set PYTHONIOENCODING=utf-8
with open('giao-duc.txt','w') as f:
	i = 0
	
	urls = ['https://vnexpress.net/giao-duc','https://vnexpress.net/giao-duc-p2','https://vnexpress.net/giao-duc-p3']
	links = []
	for url in urls:
		if i > 50:
				break
		uClient = uReq(url)

		page_html = uClient.read()

		uClient.close()

		page_soup = soup(page_html,"html.parser")
		if url == 'https://vnexpress.net/giao-duc':
			containers = page_soup.findAll("h4",{"class":"title-news"})
		else:
			containers = page_soup.findAll("h3",{"class":"title-news"})
		for container in containers:
			f.write(container.a['href'] + '\n')
			links.append(container.a['href'])
			i += 1
			if i > 50:
				break
			
	

	








