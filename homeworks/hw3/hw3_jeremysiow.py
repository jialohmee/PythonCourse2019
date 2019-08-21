import tweepy
import sys
sys.path.insert(0, '/Users/jeremysiow/Documents/Documents_MBP/api_secrets') 
# folder containing py file with api keys & tokens
from twitter import api_key, api_secret_key, access_token, access_token_secret
import collections
import csv

def initiate_twitter_connection(): 
	auth = tweepy.OAuthHandler(api_key, api_secret_key)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True) 
	# wait_on_rate_limit allows tweepy to figure the best sleep time when rate limit is reached
	return api

# the terms "user", "follower" and "friend" are defined as such:
# follower --> user --> friend
# a user is our person of interest. alternatively, he/she/it is the central node
# when you check on a user's twitter account, a follower of the user is part of the user's list of followers
# alternatively, a user is following a friend; hence a friend appears in the list of "following" on the user's account

def get_followers_id(api, account_name): # account_name refers to the user's id/screen name
	followers = []
	count = 0 # set follower counter
	for follower in tweepy.Cursor(api.followers_ids, id = account_name).items(): # paginate over user's follower ids
		try:
			count += 1 
			followers.append(follower) # append follower id to list of followers
			print("Added %s followers of %s" % (count, account_name))
		except:
			pass
	return followers

def get_friends_id(api, account_name): # account_name refers to the user's id/screen name
	friends = []
	count = 0 # set friend counter
	for friend in tweepy.Cursor(api.friends_ids, id = account_name).items(): # paginate over user's friend ids
		try:
			count += 1
			friends.append(friend) # append friend id to list of friends
			print("Added %s friends of %s" % (count, account_name))
		except:
			pass
	return friends

def get_users_details(api, users, filename):
	# this function can be used to obtain a user's friends/followers' details
	# users is a list of followers/friends as obtained from the previous two functions
	# filename refers to the name of the csv output, which contains all the followers/friends' details
	count = 0
	with open(filename, 'w') as f:
		w = csv.DictWriter(f, fieldnames = ("name", "tweets", "followers_count"))
		w.writeheader() # write fieldnames to head of csv file
		count = 0
		for user in users: # for each follower/friend in the list
			user_class = api.get_user(user) # returns a user object for each follower/friend
			user_details = {}
			user_details["name"] = user_class.screen_name # store follower/friend's screen name
			user_details["tweets"] = user_class.statuses_count # store follower/friend's tweet counts
			user_details["followers_count"] = user_class.followers_count # store follower/friend's follower counts
			w.writerow(user_details) # write follower/friend's details into csv file
			print("Added user %s's details of %s users into dictionary" % (count+1, len(users))) 
			count += 1

def get_users_users_details(api, users_users, filename):
	# this function is used to find details for two levels of separation
	# for instance, user --> friend --> friend
	# so we can use get_friends_id() to get friend's id, then loop over each friend's id to find the friend's friend's id
	# hence returning a list of lists 
	# users_users then corresponds to this list of lists
	# the idea is the same as the previous function, except that there is an additional for loop
	count = 0
	with open(filename, 'w') as f:
		w = csv.DictWriter(f, fieldnames = ("name", "tweets", "followers_count"))
		w.writeheader()
		user_count = 0
		for user in users_users:
			for user_user in user: # a double for loop is used to loop over the list of lists
				try:
					user_user_class = api.get_user(user_user)
					user_user_details = {}
					user_user_details["name"] = user_user_class.screen_name
					user_user_details["tweets"] = user_user_class.statuses_count
					user_user_details["followers_count"] = user_user_class.followers_count
					w.writerow(user_user_details)
					print("Added user %s's details of %s users into dictionary" % (user_count+1, len(user)))
					user_count += 1
				except:
					pass

def get_most_followed_user(imp_filename, exp_filename):
	# after getting the csv file containing follower/friends' details, input this csv output as imp_filename
	# and enter a new filename to store the output as a csv file -- i.e. exp_filename
	with open(imp_filename, 'r') as f: 
		# this part of the function reads imp_filename and stores it as a python list of lists
		r = csv.DictReader(f) 
		users_details = []
		for row in r:
			users_details.append(row)
	most_followed_user = None
	most_followed_count = None
	for user in range(len(users_details)):
		if most_followed_count is None and most_followed_user is None:
			most_followed_user = users_details[user]["name"]
			most_followed_count = int(users_details[user]["followers_count"])
			# to kickstart the for loop by storing the items from the friend/follower
		else:
			if most_followed_count < int(users_details[user]["followers_count"]):
				most_followed_user = users_details[user]["name"]
				most_followed_count = int(users_details[user]["followers_count"])
				# updates most_followed_user and most_followed_count by checking over each friend/follower in the list
	with open(exp_filename, 'w') as f:
		# this part stores the output as a csv file
		w = csv.DictWriter(f, fieldnames = ("name", "followers_count"))
		w.writeheader()
		output_dict = {}
		output_dict["name"] = most_followed_user
		output_dict["followers_count"] = most_followed_count
		w.writerow(output_dict)

def get_most_tweets_user(imp_filename, exp_filename):
	# arguments are the same as the previous function
	with open(imp_filename, 'r') as f:
		# stores imported csv as a python readable list of lists
		r = csv.DictReader(f)
		users_details = []
		for row in r:
			users_details.append(row)
	output_dict = {}
	output_dict["name"] = None
	output_dict["type"] = None
	with open(exp_filename, 'w') as f:
		w = csv.DictWriter(f, fieldnames = ("name", "type", "tweets"))
		w.writeheader()
		# create a csv file to store the output
		output_dict["tweets"] = 0
		for user in range(len(users_details)):
			if int(users_details[user]["followers_count"]) < 100: # corresponding to laymen whose follower counts < 100
				if output_dict["tweets"] < int(users_details[user]["tweets"]):
					output_dict["type"] = "layman"
					output_dict["name"] = users_details[user]['name']
					output_dict["tweets"] = int(users_details[user]["tweets"])
		w.writerow(output_dict) # stores the unique output among layman users in csv file
		output_dict["tweets"] = 0
		for user in range(len(users_details)): # corresponding to experts whose follower counts are between 100 and 1000
			if int(users_details[user]["followers_count"]) >= 100 and int(users_details[user]["followers_count"]) < 1000:
				if output_dict["tweets"] < int(users_details[user]["tweets"]):
					output_dict["name"] = users_details[user]['name']
					output_dict["type"] = "expert"
					output_dict["tweets"] = int(users_details[user]["tweets"])	
		w.writerow(output_dict)	# stores the unique output among expert users in csv file
		output_dict["tweets"] = 0
		for user in range(len(users_details)): # corresponding to celebrity whose follower counts >= 1000
			if int(users_details[user]["followers_count"]) >= 1000:
				if output_dict["tweets"] < int(users_details[user]["tweets"]):
					output_dict["name"] = users_details[user]['name']
					output_dict["type"] = "celebrity"
					output_dict["tweets"] = int(users_details[user]["tweets"])
		w.writerow(output_dict)	# stores the unique output among celebrity users in csv file
		# hence csv file contains three rows -- each corresponding to one type -- and a header row

def read_csv(imp_filename):
	# a function to import csv file and convert it to a python list
	# needed to filter out particular types of twitter users 
	# e.g. user --> friend --> friend
	# you use get_friends_id() and get_users_detail() to obtain csv output of friend's details
	# but before you can do the filtering in python, you need to read it into python as a list -- hence this function
	with open(imp_filename, 'r') as f:
		r = csv.DictReader(f)
		new_list = []
		for row in r:
			new_list.append(row)
	return new_list

def select_layman_expert(user_details):
	users_select = []
	for user in range(len(user_details)):
		if int(user_details[user]["followers_count"]) < 1000: # to select friend/follower whose follower count < 1000
			users_select.append(user_details[user]["name"])
	return users_select

api = initiate_twitter_connection()

# among WUSTL followers
WUSTL_followers = get_followers_id(api, "WUSTL")
get_users_details(api, WUSTL_followers, "WUSTL_followers.csv")
get_most_followed_user("WUSTL_followers.csv", "WUSTL_followers_most_followed.csv")
get_most_tweets_user("WUSTL_followers.csv", "WUSTL_followers_most_tweets.csv")

# among WUSTL friends
WUSTL_friends = get_friends_id(api, "WUSTL")
get_users_details(api, WUSTL_friends, "WUSTL_friends.csv")
get_most_followed_user("WUSTL_friends.csv", "WUSTL_friends_most_followed.csv")
get_most_tweets_user("WUSTL_friends.csv", "WUSTL_friends_most_tweets.csv")

# among WUSTLPolisci's followers' followers - i.e. follower --> follower --> WUSTLPolisci
WUSTLPoliSci_followers = get_followers_id(api, "WUSTLPoliSci")
get_users_details(api, WUSTLPoliSci_followers, "WUSTLPoliSci_followers.csv")
WUSTLPoliSci_followers_details = read_csv("WUSTLPoliSci_followers.csv")
WUSTLPoliSci_followers_select = select_layman_expert(WUSTLPoliSci_followers_details)
WUSTLPoliSci_followers_followers = []
for follower in WUSTLPoliSci_followers_select:
	try:
		WUSTLPoliSci_followers_followers.append(get_followers_id(api, follower))
	except tweepy.error.TweepError as e:
		print(e.reason) # if error prompts, prints out the reason for the exception
		pass
get_users_users_details(api, WUSTLPoliSci_followers_followers, "WUSTLPoliSci_followers_followers.csv")
get_most_tweets_user("WUSTLPoliSci_followers_followers.csv", "WUSTLPoliSci_followers_followers_most_tweets.csv")

# among WUSTLPolisci's friends' friends - i.e. WUSTLPolisci --> friend --> friend
WUSTLPoliSci_friends = get_friends_id(api, "WUSTLPoliSci")
get_users_details(api, WUSTLPoliSci_friends, "WUSTLPoliSci_friends.csv")
WUSTLPoliSci_friends_details = read_csv("WUSTLPoliSci_friends.csv")
WUSTLPoliSci_friends_select = select_layman_expert(WUSTLPoliSci_friends_details)
WUSTLPoliSci_friends_friends = []
for friend in WUSTLPoliSci_friends_select:
	try:
		WUSTLPoliSci_friends_friends.append(get_friends_id(api, friend))
	except tweepy.error.TweepError as e:
		print(e.reason) # if error prompts, prints out the reason for the exception
		pass
get_users_users_details(api, WUSTLPoliSci_friends_friends, "WUSTLPoliSci_friends_friends.csv")
get_most_tweets_user("WUSTLPoliSci_friends_friends.csv", "WUSTLPoliSci_friends_friends_most_tweets.csv")




