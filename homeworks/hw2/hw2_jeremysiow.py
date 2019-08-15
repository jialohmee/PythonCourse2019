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
import re
import datetime

with open("petitions.csv", "w") as f:
	w = csv.DictWriter(f, fieldnames = ("No", "Title", "Date", "Signatures", "Issue1", "Issue2", "Issue3")) # set headers for dataframe
	w.writeheader() # write fieldnames as headers to csv file
	base_url = "https://petitions.whitehouse.gov" # set base url which will be concatenated with respective href in the loop
	extension = "" # set extension to null
	number = 0 # set counter to 0
	text = "Load More" # create "load more" text for while loop to execute
	while text == "Load More": # when "load more" is present in current page, performing following methods. if not, stop operation
		url = base_url + extension # concatenate base_url with extension
		print("\nScraping current url: %s\n" % url) # tells user which page is currently being scraped
		page = urllib.request.urlopen(url) # open url
		html = BeautifulSoup(page.read(), "html.parser") # save html
		petitions = {} # empty dictionary to store keys and values from current url
		for petition in range(len(html.find_all("h3"))): # for all h3 tags in current url	
			try: # perform methods for those h3 tags that have <a href> values
				petition_url = base_url + html.find_all("h3")[petition].a["href"] # store url for each petition
				petition_page = urllib.request.urlopen(petition_url) # open petition url
				petition_html = BeautifulSoup(petition_page.read(), "html.parser") # store petition html
				number += 1 # add 1 to counter variable
				petitions["No"] = number # store counter variable as "No" key in dict
				petitions["Title"] = petition_html.find("h1").get_text() # store petition title as "Title" key in dict
				date = petition_html.find("h4").get_text() # get date created from petition html
				petitions["Date"] = date.split(" on ")[1] # keep only date and exclude text "created by... on"
				signatures = petition_html.find("div", {"class" : "signatures-text-container"}).text # store number of signatures as "Signatures" key in dict
				signatures_pattern = re.compile(r"(?<=)\n") # keep everything up until new line
				petitions["Signatures"] = int(signatures_pattern.split(signatures)[0].replace(',', '')) # store signature number to "Signatures" key and convert it to integer
				tags = petition_html.find("div", {"class" : "field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags"}).get_text() # get issue tags from html
				tags_pattern = re.compile(r"(?<=[a-z])(?=[A-Z])") # multiple tags were stored as e.g. "Defence and PolicySocial and Economic Reform" --> convert "Defence and Policy Social and Economic Reform"
				for i in range(len(tags_pattern.split(tags))):
					petitions["Issue" + str(i+1)] = tags_pattern.split(tags)[i] # store each issue to different key in the dictionary, from issue1 to issue3
				print(petitions) # check if keys and values are correctly stored in dict
				w.writerow(petitions) # write dict to csv file
			except: 
				continue # skips those h3 tags that have no <a href> values
		text = html.find("div", {"class": "page-load-next"}).get_text() # updates looping variable "text". 
		try: 
			extension = html.find("div", {"class": "page-load-next"}).a["href"] # if "load more" is present, find and update extension, then return to beginning of while loop
		except TypeError: # if "load more" is not present in current url, stop operation
			now = datetime.datetime.now() # store current date and time
			date_time = now.strftime("%Y-%m-%d %H:%M") # return current date and time as YYYY-MM-DD HH:MM
			print("\nYou have reached the end of the page. Petition data scraped from %s and finished at %s." % (base_url, date_time)) # message to indicate that scraping is done