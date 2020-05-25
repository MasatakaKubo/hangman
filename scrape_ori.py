import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        # url を受け取る
        self.site = site

    def scrape(self):
        html = requests.get(self.site)
        soup = BeautifulSoup(html.content, "html.parser")
        # <a></a>タグをすべて集める
        for tag in soup.find_all("a"):
            url = tag.get("jslog")
            if url is None:
                continue
            if ".html" in url :
                print("\n" + url)

Scraper("https://news.google.com/").scrape()
