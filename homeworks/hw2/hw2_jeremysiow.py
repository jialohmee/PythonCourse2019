#• Go to https://petitions.whitehouse.gov/petitions
#• Go to the petition page for each of the petitions.
#• Create a .csv file with the following information for each petition:
#– Title
#– Published date
#– Issues
#– Number of signatures

from bs4 import BeautifulSoup
import urllib.request
import requests
import csv 

url = "https://petitions.whitehouse.gov"
page = urllib.request.urlopen(url)
html = BeautifulSoup(page.read(), "html.parser")

for petition in range(len(html.find_all("h3"))):
	try:
		petition = {}
		petition_url = url + html.find_all("h3")[petition].a["href"]
		petition_page = urllib.request.urlopen(petition_url)
		petition_html = BeautifulSoup(petition_page.read(), "html.parser")		
	except:
		pass

petition["Title"] = petition_html.find("h1").text
petition["Date"] = petition_html.find("h4").text
petition["Signatures"] = petition_html.find("div", {"class" : "signatures-text-container"}).text

for i in petition_html.find_all("div", {"class" : "field-item odd"}):
	print(i)



for i in petitions:
	print(i)
	
html.find_all("h3")[0].a["href"]




extension = html.find("div", {"class": "page-load-next"}) # find "load more"
text = extension.text

urls = [url]

while text is not None:
	urls.append(url + extension.a["href"])
	new_url = url + extension.a["href"]
	new_page = urllib.request.urlopen(base_url)
	html = BeautifulSoup(page.read(), "html.parser")
	extension = html.find("div", {"class": "page-load-next"})
	text = extension.text



text = extension.text
href = extension.a["href"]
urls = [url]
urls.append(url + href)
urllib.request.urlopen(urls[1])

urls = [url]
base_url = "https://petitions.whitehouse.gov/petitions"
for i in range()


while extension.text == "Load More":
	urls.append(url + extension.a["href"])
	base_url = url + extension.a["href"]
	page = urllib.request.urlopen(base_url)
	html = BeautifulSoup(page.read(), "html.parser")
	extension = html.find("div", {"class": "page-load-next"})

urls

urls.append(url)
urls.append(url + extension.a["href"])



urls = []
while extension.text == "Load More":
	urls.append(base_url + extension.a["href"])
	url = url + extension.a["href"]
	page = urllib.request.urlopen(url)
	html = BeautifulSoup(page.read(), "html.parser")
	extension = html.find("div", {"class" : "page-load-next"})

extension.text

urls = [base_url]
urls.append(base_url + base_extension.a["href"])
urls

base_extension.a["href"]

with open('hw2_solution_jeremy.csv', 'w') as f:
  w = csv.DictWriter(f, fieldnames = ("Title", "Published Date", "Issues", "Number of Signatures"))
  w.writeheader()
  base_url = "https://petitions.whitehouse.gov/petitions"
  base_page = urllib.request.urlopen(base_url)
  base_html = BeautifulSoup(base_page.read(), "html.parser")
  base_extension = base_html.find("div", {"class" : "page-load-next"})
  base_extension.a["href"]


extensions = []


url = "https://petitions.whitehouse.gov/petitions?page=4"
page = urllib.request.urlopen(url)
html = BeautifulSoup(page.read(), "html.parser")
html.find("div", {"class" : "page-load-next"})

url = "https://petitions.whitehouse.gov/petitions?page=3"
page = urllib.request.urlopen(url)
html = BeautifulSoup(page.read(), "html.parser")
extension = html.find("div", {"class" : "page-load-next"})
extension.a["href"]
extension.text == "Load More"