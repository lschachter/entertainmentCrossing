import re
import requests
from bs4 import BeautifulSoup
from googlesearch import search


class ComparePages:
	def __init__(self, queries):
		self.queries = queries

	def run_queries(self):
		self.links = []

		for query in self.queries:
			link = self.get_url(query)
			if not link:
				return {"error_msg": f'{query} did not yield an individual\'s imdb page to search. Please try again.'}
			self.links.append(link)

		intersections = self.compare_filmographies()


	def get_url(self, query):
		# return the first imdb url that google finds 
		for url in search(query, tld="com", num=10, stop=10, pause=1.0):
			if "imdb" in url and "name" in url:
				return url
		return None


	def compare_filmographies(self):
		self.title_dicts = []

		for link in self.links:
			title_dict = self.get_title_dict(link)
			if title_dict.get('error_msg'):
				return title_dict

		return set.intersection(*self.title_dicts)


	def get_title_dict(self, link):
		response = requests.get(link, timeout=15)
		content = BeautifulSoup(response.content, "html.parser")

		filmography = content.find(id="filmography")
		if not filmography:
			return {"error_msg": f'the page <a href="{link}" target="_blank">{link}</a> did not yield a filmography to search. Please try again.'}

		titles_pattern = "/title/.*"

		titles = filmography.find_all('a', attrs={"href":re.compile(titles_pattern)})
		title_dict = {a.get('href'): a.text for a in titles}

		return title_dict


def get_title_dict(link):
	response = requests.get(link, timeout=15)
	content = BeautifulSoup(response.content, "html.parser")

	filmography = content.find(id="filmography")
	if not filmography:
		return {"error_msg": f'the page <a href="{link}" target="_blank">{link}</a> did not yield a filmography to search. Please try again.'}

	titles_pattern = "/title/.*"

	titles = filmography.find_all('a', attrs={"href":re.compile(titles_pattern)})
	title_dict = {a.get('href'): a.text for a in titles}

	return title_dict


def compare_filmographies(link_1, link_2):
	title_dict_1 = get_title_dict(link_1)
	title_dict_2 = get_title_dict(link_2)

	if title_dict_1.get('error_msg'):
		return title_dict_1
	if title_dict_2.get('error_msg'):
		return title_dict_2

	both_in_titles = set(title_dict_1) & set(title_dict_2)
	both_in_dict = { title: title_dict_1[title] for title in both_in_titles}

	return both_in_dict


def getURL(query):
	# return the first imdb url that google finds 
	for url in search(query, tld="com", num=10, stop=10, pause=1.0):
		if "imdb" in url:
			return url
	return None



def run_queries(query1, query2):
	link1 = getURL(query1 + " imdb")
	link2 = getURL(query2 + " imdb")

	if not link1:
		return {"error_msg": f'{query1} did not yield an imdb page to search. Please try again.'}
	if not link2:
		return {"error_msg": f'{query2} did not yield an imdb page to search. Please try again.'}

	both_in = compare_filmographies(link1, link2)
	if both_in.get('error_msg'):
		return both_in

	return {
		"crossing": both_in,
		"e1": {
			"name": query1,
			"url": link1
		},
		"e2": {
			"name": query2,
			"url": link2
		}
	}


if __name__ == "__main__":
	print(run_queries("cate blanchett", "elijah wood"))
