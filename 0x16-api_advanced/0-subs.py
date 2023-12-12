#!/usr/bin/python3
""" 0-subs.py solution """
import requests


def number_of_subscribers(subreddit):
	"""
	Queries the Reddit API for the number of subscribers of a given subreddit.

	Args:
		subreddit: The name of the subreddit.

	Returns:
		The number of subscribers, or 0 if the subreddit is invalid.
	"""
	url = f"https://www.reddit.com/r/{subreddit}/about.json"
	headers = { "User-Agent": "My cool Reddit bot (by /u/wintermancer)"}
	try:
		response = requests.get(url, headers=headers, allow_redirects=False)
		if response.status_code == 200:
			data = response.json()
			return data["data"]["subscribers"]
		else:
			return 0
	except Exception as e:
		print(f"Error: {e}")
		return 0
