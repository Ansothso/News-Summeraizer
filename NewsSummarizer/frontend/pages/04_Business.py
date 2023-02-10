import streamlit as st

from os import remove
from utilities.bbc import BBC
from utilities.theguardian import TheGuardian


category = "business"

theguardian_sports = TheGuardian("https://www.theguardian.com/uk/business/rss",category)
articles_guardian = theguardian_sports.getArticles()
even_articles = [articles_guardian[i] for i in range(10) if i%2 == 0]
odd_articles = [articles_guardian[i] for i in range(10) if i%2 != 0]

st.title("Business News")
st.write("Latest Business News from The Guardian")

refresh = st.button("Refresh")
if refresh:
    remove("cache.json")
    st.experimental_rerun()


col1, col2 = st.columns(2)

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


st.write("Latest Business News from the BBC")



bbc_sports = BBC("http://feeds.bbci.co.uk/news/business/rss.xml", category)

articles_bbc = bbc_sports.getArticles()
even_articles = [articles_bbc[i] for i in range(10) if i%2 == 0]
odd_articles = [articles_bbc[i] for i in range(10) if i%2 != 0]


col1, col2 = st.columns(2)
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

