import requests,json
from bs4 import BeautifulSoup

class wikipedia():
	"""docstring for wikipedia"""
	def __init__(self):
		self._endpoint = "https://id.wikipedia.org/w/api.php"


	def _search_from_wiki(self, query):
		s = requests.session()
		url = "https://id.wikipedia.org/w/api.php"
		PARAMS = {
		"action": "query",
		"format": "json",
		"list": "search",
		"srsearch": query
		}
		js = s.get(url=url, params=PARAMS).json()
		text = ""
		for x in js['query']['search']:
			text += x['snippet']
			cleantext = BeautifulSoup(text, "lxml").text
			return cleantext

		
