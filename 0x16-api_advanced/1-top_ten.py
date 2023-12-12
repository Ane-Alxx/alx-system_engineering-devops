#!/usr/bin/python3
""" 1-top_ten.py solution """

import requests


def top_ten(subreddit):
	"""
	Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

	Args:
		subreddit: The name of the subreddit.
	"""
	url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
	headers = {"User-Agent": "My cool Reddit bot (by /u/wintermancer)"}
	try:
		response = requests.get(url, headers=headers, allow_redirects=False)
		if response.status_code == 200:
			data = response.json()
			for post in data["data"]["children"]:
				print(post["data"]["title"])
		else:
			print(f"Error: {response.status_code}")
	except Exception as e:
		print(f"Error: {e}")
		print(None)
