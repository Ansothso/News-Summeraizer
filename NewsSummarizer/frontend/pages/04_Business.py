import streamlit as st
from utilities.rss_theguardian import getArticles as get_guardian_articles
from utilities.rss_bbc import getArticles as get_bbc_articles

GUARDIAN_BUSINESS = "https://www.theguardian.com/uk/business/rss"
articles_guardian = get_guardian_articles(GUARDIAN_BUSINESS)
even_articles = [articles_guardian[i] for i in range(10) if i%2 == 0]
odd_articles = [articles_guardian[i] for i in range(10) if i%2 != 0]

st.title("Business News")
st.write("Latest Business News from The Guardian")

col1, col2 = st.columns(2)

with col1:
    for article in odd_articles:
        with st.expander(article["title"]):
            link = "[Original article]("+article["link"]+")"
            st.write(link)
            #st.write(article["link"])
            st.write(article["text"])
        
with col2:
    for article in even_articles:
        with st.expander(article["title"]):
            st.write(article["link"])
            st.write(article["text"])


st.write("Latest Business News from the BBC")


col1, col2 = st.columns(2)
BBC_BUSINESS = "http://feeds.bbci.co.uk/news/business/rss.xml"
articles_bbc = get_bbc_articles(BBC_BUSINESS)
even_articles = [articles_bbc[i] for i in range(10) if i%2 == 0]
odd_articles = [articles_bbc[i] for i in range(10) if i%2 != 0]


with col1:
    for article in odd_articles:
        with st.expander(article["title"]):
            st.write(article["link"])
            st.write(article["text"])
        
with col2:
    for article in even_articles:
        with st.expander(article["title"]):
            st.write(article["link"])
            st.write(article["text"])
