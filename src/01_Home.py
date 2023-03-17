import streamlit as st
from PIL import Image
import json
from os.path import exists
import random

image = Image.open('images/banner_topnews.png')
st.title("Home")
st.image(image)
st.caption("Image by [Cottonbro Studio](https://www.pexels.com/de-de/foto/espresso-fruhstuck-nachrichten-zeitung-3944425/)")


st.write('''Welcome to the News Summarizer!

This application summarizes news from the previous day. You can read a random summary below. If you want to read news of a certain category, you can go to respective page.

You can create your own summary. In the summary generation page, you can insert a news article and have it summarized. In addition, you can download your summary as a .txt file to share with others.''')

if exists("cache.json"):
    saved_articles = json.load(open("cache.json"))
    samples = random.sample(range(0, len(saved_articles)), 4)
   

even_articles = [samples[1], samples[3]]
odd_articles = [samples[0],samples[2]]
col1, col2 = st.columns(2)

with col1:
    for index in odd_articles:
        article=saved_articles[index]
        with st.expander(article["title"]):
            link = "[Original article]("+article["link"]+")"
            st.write(link)
            st.write(article["summary"])
        
with col2:
    for index in even_articles:
        article=saved_articles[index]
        with st.expander(article["title"]):
            link = "[Original article]("+article["link"]+")"
            st.write(link)
            st.write(article["summary"])
