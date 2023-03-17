import streamlit as st
from PIL import Image

from os import remove
from utilities.bbc import BBC
from utilities.theguardian import TheGuardian

im = Image.open("icon_1.ico")

st.set_page_config(
    page_title="Politics",
    page_icon=im
)


category = "politics"

theguardian_sports = TheGuardian("https://www.theguardian.com/politics/rss",category)
articles_guardian = theguardian_sports.getArticles()
even_articles = [articles_guardian[i] for i in range(10) if i%2 == 0]
odd_articles = [articles_guardian[i] for i in range(10) if i%2 != 0]

image = Image.open('images/banner_politics.png')
st.title("Politics News")
st.image(image)
st.caption("Image by [Mathias Reding](https://www.pexels.com/de-de/foto/stadt-wahrzeichen-gebaude-bau-4468974/)")

st.write("Latest Politics News from The Guardian")

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
            st.write(article["summary"])
        
with col2:
    for article in even_articles:
        with st.expander(article["title"]):
            link = "[Original article]("+article["link"]+")"
            st.write(link)
            st.write(article["summary"])


st.write("Latest Politics News from the BBC")


bbc_sports = BBC("http://feeds.bbci.co.uk/news/politics/rss.xml", category)

articles_bbc = bbc_sports.getArticles()
even_articles = [articles_bbc[i] for i in range(10) if i%2 == 0]
odd_articles = [articles_bbc[i] for i in range(10) if i%2 != 0]


col1, col2 = st.columns(2)
with col1:
    for article in odd_articles:
        with st.expander(article["title"]):
            link = "[Original article]("+article["link"]+")"
            st.write(link)
            st.write(article["summary"])
        
with col2:
    for article in even_articles:
        with st.expander(article["title"]):
            link = "[Original article]("+article["link"]+")"
            st.write(link)
            st.write(article["summary"])

