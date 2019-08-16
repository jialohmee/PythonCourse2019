# TODO: write code to answer the following questions: 
# 1) which of these embassies is closest to the White House in meters? 
# how far is it, and what is the address?
# 2) if I wanted to hold a morning meeting there, which cafe would you suggest?
# 3) if I wanted to hold an evening meeting there, which bar would you suggest? 

import imp
import imp
import sys
import geopy.distance

sys.path.insert(0, '/Users/jeremysiow/Documents/Documents_MBP/api_secrets')
imported_items = imp.load_source('google_map', '/Users/jeremysiow/Documents/Documents_MBP/api_secrets/start_google.py')
gmaps = imported_items.client

whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
location = gmaps.geocode(whitehouse)
whitehouse_latlon = location[0]['geometry']['location']
whitehouse_latlon = [float(whitehouse_latlon["lat"]), float(whitehouse_latlon["lng"])]

embassies_latlon = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]

distance_from_whitehouse = []
for embassy_latlon in embassies_latlon:
	distance_from_whitehouse.append(geopy.distance.distance(embassy_latlon, whitehouse_latlon).km)

embassies = []
for embassy in embassies_latlon:
	embassies.append(gmaps.reverse_geocode(embassy))

closest_embassy = embassies[1][0]['formatted_address']
closest_embassy

cafes_nearby = gmaps.places_nearby(embassies_latlon[1], 1000, type = "cafe", keyword = "breakfast")
best_cafe_nearby = None
current_cafe_rating = 0.0
for cafe in range(len(cafes_nearby)):
	if best_cafe_nearby is None:
		best_cafe_nearby = cafes_nearby['results'][cafe]['name']
		current_cafe_rating = cafes_nearby['results'][cafe]['rating']
	else:
		try:
			if current_cafe_rating < cafes_nearby['results'][cafe]['rating']:
				best_cafe_nearby = cafes_nearby['results'][cafe]['name']
				current_cafe_rating = cafes_nearby['results'][cafe]['rating']
		except:
			pass

best_cafe_nearby
current_cafe_rating

bars_nearby = gmaps.places_nearby(embassies_latlon[1], 1000, type = "bar", keyword = "dinner")
best_bar_nearby = None
current_bar_rating = 0.0
for bar in range(len(bars_nearby)):
	if best_bar_nearby is None:
		best_bar_nearby = bars_nearby['results'][bar]['name']
		current_bar_rating = bars_nearby['results'][bar]['rating']
	else:
		try:
			if current_bar_rating < bars_nearby['results'][bar]['rating']:
				best_bar_nearby = bars_nearby['results'][bar]['name']
				current_bar_rating = bars_nearby['results'][bar]['rating']
		except:
			pass

best_bar_nearby
current_bar_rating