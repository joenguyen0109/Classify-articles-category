import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


# url = 'https://vnexpress.net/phap-luat'
# uClient = uReq(url)

# page_html = uClient.read()

# uClient.close()

# page_soup = soup(page_html,"html.parser")

# container = page_soup.findAll("h4",{"class":"title-news"})

# print(container[0].get_text())

# import bs4
# from urllib.request import urlopen as uReq
# from bs4 import BeautifulSoup as soup


urls = ['https://vnexpress.net/suc-khoe','https://vnexpress.net/giai-tri']
topic = {}
for url in urls:
	title_holder  = []
	uClient = uReq(url)

	page_html = uClient.read()

	uClient.close()

	page_soup = soup(page_html,"html.parser")

	titles = page_soup.findAll("h3",{"class":"title-news"})

	for title in titles:
		title_holder.append(title.get_text().strip())

	print(len(title_holder))
	topic[url] = title_holder



urls = ['https://vnexpress.net/phap-luat']
for url in urls:
	title_holder  = []
	uClient = uReq(url)

	page_html = uClient.read()

	uClient.close()

	page_soup = soup(page_html,"html.parser")

	titles = page_soup.findAll("h4",{"class":"title-news"})

	for title in titles:
		title_holder.append(title.get_text().strip())
	topic[url] = title_holder
	print(len(title_holder))
print(topic)