import json
import feedparser
import pandas as pd
from os.path import exists
from utilities.summarizer import get_summary

'''
abstract class for news fetching
'''
class NewsSite:
    
    # initialize news site instance with rss link and news category
    def __init__(self, rss, category, source):
        self.rss = rss
        self.category = category
        self.source = source
    
    
    # abstract function for getting article text - to be overloaded by subclass
    def getText(self, url):
        pass

    # gets all articles from the rss feed (given the link to the rss feed)
    def getArticlesFromSource(self):
        #fetch all articles from rss
        news = feedparser.parse(self.rss)
        results = []

        #save title, link, source, category and text of each article in a dictionary
        for i in range (0,10):
            entry = news.entries[i]
            title = entry.title
            link = entry.link
            text = self.getText(link)

            ##do summary
            summary = get_summary(text)

            #append results to the dictionary
            article = {"title": title, "link": link, "text": text, "category": self.category, "source": self.source, "summary": summary}
            results.append(article)
        return results

    # still under construction...
    def refresh(self):
        articles = self.getArticlesFromSource()
        with open("cache.json", "w") as file:
            json.dump(articles, file)

    # get article from cache if available, else get from source.
    def getArticles(self):
        if exists("cache.json"):
            saved_articles = json.load(open("cache.json"))
            
            df = pd.DataFrame(saved_articles)
            res = df[df['source'] == self.source]
            res = res[res['category'] == self.category].to_dict(orient='records')

            if len(res) != 0:
                return res
            else: 
                articles = self.getArticlesFromSource()
                
                saved_articles = saved_articles + articles
                with open("cache.json", "w") as file:
                    json.dump(saved_articles, file)
                return articles
        
        else:
            articles =  self.getArticlesFromSource()
            with open("cache.json", "w") as file:
                json.dump(articles, file)
            return articles


'''
testing existing technologies
update on the 9th
'''
        