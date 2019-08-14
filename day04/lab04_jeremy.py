## Go to https://polisci.wustl.edu/people/88/
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
## 	-Specialization
## 	-Name
## 	-Title
## 	-E-mail
## 	-Web page
	
from bs4 import BeautifulSoup
import urllib.request
import csv 

web_address = 'https://polisci.wustl.edu/people/88/'
web_page = urllib.request.urlopen(web_address)

soup = BeautifulSoup(web_page.read())	
soup.prettify()

soup.find_all("h3")
name = soup.find_all("h3")
name_list = [i.text for i in name]
name_list = name_list[1: len(name_list) - 3]

titles = soup.find_all('div', {'class' : "dept"})
print(type(titles[0]))
title_list = [i.text for i in titles]

all_card_tags = soup.find_all("a", {"class" : "card"})
faculty_web_address = []
for i in range(len(all_card_tags)):
	faculty_web_address.append("https://polisci.wustl.edu" + all_card_tags[i]["href"])
#faculty_web_address[6] = "http://epstein.wustl.edu/"

faculty_web_page = []
for i in range(len(faculty_web_address)):
	try:
		faculty_web_page.append(urllib.request.urlopen(faculty_web_address[i]))
		print("Connection successful for" + faculty_web_address[i])
	except urllib.error.URLError:
		print("Connection unsuccessful for" + faculty_web_address[i])
		pass

soup_faculty_web_page = []
for i in range(len(faculty_web_page)):
	soup_faculty_web_page.append(BeautifulSoup(faculty_web_page[i].read()))
email = []
for i in range(len(soup_faculty_web_page)):
	email.append(soup_faculty_web_page[i].find_all("a")[20].text)
print(email)



all_a_deniz = soup_faculty_web_page[0].find_all("a")
for i in all_a_deniz:
	print(i)

#all_a_deniz.startswith("mailto")
#for i in all_a_deniz:
#	if not all_a_deniz[i].startswith("mailto")

for num, i in enumerate(all_a_deniz):
	print(num, i)
all_a_deniz[20].text


research_interests = []
for i in range(len(soup_faculty_web_page)):
	research_interests.append(soup_faculty_web_page[i].find_all("meta", {"name" : "description"}))
research_interests_list = []

research_interests[0].get_text()

soup_faculty_web_page[0].find_all("meta", {"name" : "description"})

with open("washu_faculty.csv", "w") as f:
	my_writer = csv.DictWriter(f, fieldnames = ("Name", "Title"))
	my_writer.writeheader()
	for i in range(len(titles)):
		my_writer.writerow({"Name": name_list[i], "Title": title_list[i]})
	#for name in name_list:
	#	my_writer.writerow({"Name": name})
	#for name in name_list:
	#	my_writer.reader(name)
	#for name in name_list:
	#	my_writer.writerow(name)
	
				
