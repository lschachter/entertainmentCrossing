import re
import requests
from bs4 import BeautifulSoup
from googlesearch import search


class ComparePages:
	'''
	ComparePages will take multiple queries and search for the IMDb pages most related to them. If it successfully finds overlap in the filmographies found on those IMDb pages, it will return that overlap. Otherwise it will return the relevant error.
	'''
	def __init__(self, names={}):
		self.entertainers = { name: "" for name in names }
		self.error_dict = {}
		self.title_dicts = []


	def run_queries(self, names):
		self.entertainers = { name: "" for name in names }
		for name in self.entertainers:
			self.entertainers[name] = self.get_url(name)

		if self.error_dict: return self.error_dict
		self.intersect = self.compare_filmographies()
		if self.error_dict: return self.error_dict

		output = self.build_output_dict()
		return output


	def get_url(self, query):
		'''
		Use Google's search API to return the first imdb url found
		'''
		for url in search(query, tld="com", num=10, stop=10, pause=1.0):
			if "imdb" in url and "name" in url:
				return url
		self.error_dict = {"error_msg": f'{query} did not yield an individual\'s imdb page to search. Please try again.'}
		return ""


	def compare_filmographies(self):
		'''
		Get and compare the filmographies of each entertainer entered
		'''
		for name in self.entertainers:
			self.title_dicts.append(self.get_title_dict(name, self.entertainers[name]))

		intersect_set = set.intersection(*map(set, self.title_dicts))
		intersect_dict = { title: self.title_dicts[0][title] for title in intersect_set }
		return intersect_dict


	def get_title_dict(self, name, link):
		'''
		Use the `requests` and `BeautifulSoup` libraries to scrape the given IMDb page for a filmography section.
		Use the `re` library to search the scraped content for the regular expression that points to the title section. 
		'''
		response = requests.get(link, timeout=15)
		content = BeautifulSoup(response.content, "html.parser")

		filmography = content.find(id="filmography")
		if not filmography:
			self.error_dict = {"error_msg": f'the IMDb page <a href="{link}" target="_blank">{name}</a> did not yield a filmography to search. Please try again.'}
			return None

		titles_pattern = "/title/.*"
		titles = filmography.find_all('a', attrs={"href":re.compile(titles_pattern)})
		title_dict = {a.get('href'): a.text for a in titles}
		return title_dict


	def build_output_dict(self):
		output = {"crossing": self.intersect}

		for i, name in enumerate(self.entertainers):
			key = "e" + str(i + 1)
			output[key] = { "name": name, "url": self.entertainers[name] }

		return output


if __name__ == "__main__":
	cp = ComparePages()
	output = cp.run_queries(["cate blanchett", "elijah wood", "sean bean"])
	print('crossing: ')
	for item in output['crossing']:
		print(item, output['crossing'][item])
	print(output['e1'])
	print(output['e2'])
	print(output['e3'])
