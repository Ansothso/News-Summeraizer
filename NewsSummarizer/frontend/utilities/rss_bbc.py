import feedparser
import requests
from bs4 import BeautifulSoup as bs
import codecs

#define a function that extracts article text from a given url
def getText(url):
    #get the html page from url
    page = requests.get(url)

    #parse html and find all paragraphs in main content
    soup = bs(page.content, "html.parser")
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
#create a function that gets all articles from the rss feed (given the link to the rss feed)
def getArticles(rssLink):
    #fetch all articles from rss
    news = feedparser.parse(rssLink)
    results = []
    #save title, link and text of each article in a dictionary
    for entry in news.entries:
        title = entry.title
        link = entry.link
        text = getText(link)
        #append results to the dictionary
        article = {"title": title, "link": link, "text": text}
        results.append(article)
    return results
#print(getArticles("http://feeds.bbci.co.uk/news/rss.xml"))