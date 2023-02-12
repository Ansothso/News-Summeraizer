import streamlit as st

from os import remove
from utilities.bbcsports import BBCsports
from utilities.theguardian import TheGuardian


category = "sports"

theguardian_sports = TheGuardian("https://www.theguardian.com/sport/rss",category)
articles_guardian = theguardian_sports.getArticles()
even_articles = [articles_guardian[i] for i in range(10) if i%2 == 0]
odd_articles = [articles_guardian[i] for i in range(10) if i%2 != 0]

st.title("Sports News")
st.write("Latest Sports News from The Guardian")

refresh = st.button("Refresh")
if refresh:
    remove("cache.json")
    st.experimental_rerun()


col1, col2 = st.columns(2)

with col1:
    for article in odd_articles:
        with st.expander(article["title"]):
            link = "[Original article]("+article["link"]+")"
            st.write(link)
            st.write(article["text"])
        
with col2:
    for article in even_articles:
        with st.expander(article["title"]):
            link = "[Original article]("+article["link"]+")"
            st.write(link)
            st.write(article["text"])


st.write("Latest Sports News from the BBC")


bbc_sports = BBCsports("https://feeds.bbci.co.uk/sport/rss.xml", category)

articles_bbc = bbc_sports.getArticles()
even_articles = [articles_bbc[i] for i in range(10) if i%2 == 0]
odd_articles = [articles_bbc[i] for i in range(10) if i%2 != 0]


col1, col2 = st.columns(2)
with col1:
    for article in odd_articles:
        with st.expander(article["title"]):
            link = "[Original article]("+article["link"]+")"
            st.write(link)
            st.write(article["text"])
        
with col2:
    for article in even_articles:
        with st.expander(article["title"]):
            link = "[Original article]("+article["link"]+")"
            st.write(link)
            st.write(article["text"])

