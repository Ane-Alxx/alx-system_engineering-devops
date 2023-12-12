#!/usr/bin/python3
""" 2-recurse.py solution """

import requests


def recurse(subreddit, hot_list=[]):
	"""
	Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

	Args:
		subreddit: The name of the subreddit.
		hot_list: The list of hot article titles collected so far (default: []).

	Returns:
		A list of all hot article titles, or None if the subreddit is invalid.
	"""
	url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
	headers = {"User-Agent": "My cool Reddit bot (by /u/wintermancer)"}
	try:
		response = requests.get(url, headers=headers, allow_redirects=False)
		if response.status_code == 200:
			data = response.json()
			hot_list.extend([post["data"]["title"] for post in data["data"]["children"]])
			after = data["data"]["after"]
			if after:
				return recurse(subreddit, hot_list)
			else:
				return hot_list
		else:
			return None
	except Exception as e:
		print(f"Error: {e}")
		return None
