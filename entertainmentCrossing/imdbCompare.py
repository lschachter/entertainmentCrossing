import re
import requests
from bs4 import BeautifulSoup
from googlesearch import search

def get_title_dict(link):
	response = requests.get(link, timeout=15)
	content = BeautifulSoup(response.content, "html.parser")

	filmography = content.find(id="filmography")
	titles_pattern = "/title/.*"

	titles = filmography.findAll('a', attrs={"href":re.compile(titles_pattern)})
	title_dict = {a.text: a.get('href') for a in titles}

	return title_dict


def compare_filmographies(link_1, link_2):
	title_dict_1 = get_title_dict(link_1)
	title_dict_2 = get_title_dict(link_2)

	both_in = set(title_dict_1) & set(title_dict_2)

	return both_in


def getURL(query):
	# return the first imdb url that google finds 
	for url in search(query, tld="com", num=10, stop=10, pause=2.0):
		if "imdb" in url:
			return url
	return None



def run_queries(query1, query2):
	link1 = getURL(query1)
	link2 = getURL(query2)

	if link1 is None:
		return f'Error: {query1} did not yield an imdb page to search. Please try again.'
	elif link2 is None:
		return f'Error: {query2} did not yield an imdb page to search. Please try again.'

	return compare_filmographies(link1, link2)



if __name__ == "__main__":
	print(run_queries("george clooney", "brad pitt"))

