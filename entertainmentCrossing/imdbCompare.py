class ComparePages:
	'''
	ComparePages will take multiple queries and search for the IMDb pages most related to them.
	If it successfully finds overlap in the filmographies found on those IMDb pages,
	it will return that overlap. Otherwise it will return the relevant error.
	'''
	def __init__(self, search_api, requests_api, scraper_lib, regex_lib):
		self.search_api = search_api
		self.requests_api = requests_api
		self.scraper_lib = scraper_lib
		self.regex_lib = regex_lib
		self.links = []
		self.entertainers = []
		self.output = {}


	def run_queries(self, names):
		self.names = names
		for name in self.names:
			self.links.append(self.get_url(name))

		self.output['crossing'] = self.compare_filmographies()
		self.output['entertainers'] = self.entertainers
		return self.output


	def get_url(self, name):
		'''
		Use Google's search API to return the first imdb url found
		'''
		query = name + " imdb"
		for url in self.search_api(query, tld="com", num=10, stop=10, pause=1.0):
			if "imdb" in url and "name" in url:
				return url
		self.output["error_msg"] = f'"{name}" did not yield an individual\'s imdb page to search. Please try again.'
		return ""


	def compare_filmographies(self):
		'''
		Get and compare the filmographies of each entertainer entered
		'''
		if self.output.get("error_msg"):
			return {}

		title_dicts = []
		num_entertainers = len(self.names)
		for i in range(num_entertainers):
			title_dict = self.get_title_dict(self.names[i], self.links[i])
			title_dicts.append(title_dict)

		intersect_set = set.intersection(*map(set, title_dicts))
		intersect_dict = { link: title_dicts[0][link] for link in intersect_set }
		return intersect_dict


	def get_title_dict(self, name, link):
		'''
		Use the `requests` and `BeautifulSoup` libraries to scrape the given IMDb page for a filmography section.
		Use the `re` library to search the scraped content for the regular expression that points to the title section. 
		'''
		response = self.requests_api.get(link, timeout=15)
		content = self.scraper_lib(response.content, "html.parser")

		filmography = content.find(id="filmography")
		if not filmography:
			self.output["error_msg"] = f'the IMDb page "<a href="{link}" target="_blank">{name}</a>" did not yield a filmography to search. Please try again.'
			return None

		self.add_entertainer(content, link)
		titles_pattern = "/title/.*"
		titles = filmography.find_all('a', attrs={ "href": self.regex_lib.compile(titles_pattern) })
		title_dict = { a.get('href'): a.text for a in titles }
		return title_dict


	def add_entertainer(self, page_content, link):
		# y'all, imdb source code is a mess
		name_section = page_content.find(id="name-overview-widget")
		official_name = name_section.find(class_="itemprop").get_text()
		self.entertainers.append({ "name": official_name, "url": link })
