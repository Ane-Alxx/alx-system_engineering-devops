#!/usr/bin/python3
""" 100-count.py solution """

import requests
from collections import Counter

def count_words(subreddit, word_list):
	"""
	Recursively queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of the given keywords.

	Args:
		subreddit: The name of the subreddit to query.
		word_list: A list of keywords to count.
	"""
	url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
	headers = {
		"User-Agent": "My cool Reddit bot (by /u/wintermancer)"
	}
	try:
		response = requests.get(url, headers=headers, allow_redirects=False)
		if response.status_code == 200:
			data = response.json()
			words = Counter()
			for post in data["data"]["children"]:
				title = post["data"]["title"].lower()
				for word in word_list:
					word_normalized = word.lower()
					if word_normalized.strip() and not (word_normalized.endswith(".") or word_normalized.endswith("!") or word_normalized.endswith("_")):
						words[word_normalized] += title.count(word_normalized)
			words = sorted([(count, word) for word, count in words.items() if count > 0], key=lambda x: (-x[0], x[1]))
			for count, word in words:
				print(f"{word}: {count}")
			after = data["data"]["after"]
			if after:
				return count_words(subreddit, word_list, words)
		else:
			print(f"Error: {response.status_code}")
	except Exception as e:
		print(f"Error: {e}")

def main():
	if len(sys.argv) < 3:
		print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
		print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
	else:
		count_words(sys.argv[1], sys.argv[2].split())

if __name__ == "__main__":
	main()
