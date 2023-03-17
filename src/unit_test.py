from utilities.bbcsports import BBCsports
from utilities.bbc import BBC
from utilities.theguardian import TheGuardian

from difflib import SequenceMatcher

import os, os.path
import codecs
import json

#load expected texts from test articles
with codecs.open("expected_text.txt", 'r', 'utf-8') as file:
    expected_texts = file.readlines()

categories = ["business", "politics", "sports"]
theguardian_business = TheGuardian("https://www.theguardian.com/uk/business/rss",categories[0])
bbc_businesss = BBC("http://feeds.bbci.co.uk/news/business/rss.xml", categories[0])
bbc_sports = BBCsports("https://feeds.bbci.co.uk/sport/rss.xml", categories[2])


# testing getText for the guardian
def testgetTextGuardian():
    fetched_text = theguardian_business.getText("https://www.theguardian.com/business/2023/mar/12/uk-working-on-cash-lifeline-for-tech-firms-hit-by-silicon-valley-bank-collapse")

    seq = SequenceMatcher(None, fetched_text, expected_texts[0])
    if round(seq.ratio(), 1) >= 0.5:
        assert True
    
    else:
        assert False
    print("Similarity ratio: {}".format(round(seq.ratio(), 1)))


# testing getText for BBC
def testgetTextBBC():
    fetched_text = bbc_businesss.getText("https://www.bbc.com/news/world-middle-east-64931074")

    seq = SequenceMatcher(None, fetched_text, expected_texts[1])
    if round(seq.ratio(), 1) >= 0.5:
        assert True
    else:
        assert False
    print("Similarity ratio: {}".format(round(seq.ratio(), 1)))


# testing getText for BBCSports
def testgetTextBBCSports():
    fetched_text = bbc_sports.getText("https://www.bbc.com/sport/horse-racing/64875351")

    seq = SequenceMatcher(None, fetched_text, expected_texts[2])
    if round(seq.ratio(), 1) >= 0.5:
        assert True
    else:
        assert False
    print("Similarity ratio: {}".format(round(seq.ratio(), 1)))


# testing getArticles
# test if cache.json is created if doesn't exist
def testgetArticles():
    theguardian_business.getArticles(summarize=False)
    if os.path.exists("cache.json"):
        assert True
    else:
        assert False

# test if cache.json is updated
def testupdatedCache():
    bbc_businesss.getArticles(summarize=False)
    # load created cache
    cache = json.load(open("cache.json"))
    if len(cache) == 20:
        assert True
    else:
        assert False


# test getArticlesFromSource - see if all attributes are saved
def testgetArticlesfromSource():
    cache = json.load(open("cache.json"))
    attribute_ok = False
    for i in cache:
        if "title" in i.keys() and "link" in i.keys() and "text" in i.keys() and "category" in i.keys() and "source" in i.keys() and "summary" in i.keys():
            attribute_ok = True
        else:
            attribute_ok = False
    assert attribute_ok

# test refresh 
def testRefresh():
    bbc_businesss.refresh(summarize=False)
    cache = json.load(open("cache.json"))
    assert len(cache) == 10
     