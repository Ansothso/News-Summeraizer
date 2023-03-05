from utilities.newssite import NewsSite
import requests

from bs4 import BeautifulSoup as bs

class BBCsports(NewsSite):

    def __init__(self, rss, category):
        super().__init__(rss, category, "bbc")

    #define a function that extracts article text from a given url
    def getText(self, url):
        #get the html page from url
        print(url)
        page = requests.get(url)

        #parse html and find all paragraphs in main content
        soup = bs(page.content, "html.parser")
        if "live" in url:
            results = soup.find(id="lx-commentary-top").find_all("p")
        else:
            results = soup.find("article").find_all("p")
        #extract and format text from paragraphs
        articleText = ""
        for paragraph in results:
            for content in paragraph.contents:
                #print(content.name)
                if content.name == None:
                    articleText += str(content) + " "
                else:
                    if content.name == "a" or content.name == "strong" or content.name == "b":
                        if len(content.contents) > 0:
                            articleText += str(content.get_text())

        return articleText


