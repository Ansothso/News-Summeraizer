from PIL import Image
import streamlit as st

im = Image.open("icon_1.ico")

st.set_page_config(
    page_title="News-Summarizer",
    page_icon=im
)

st.title("News-Summarizer")
#st.sidebar.success("Select a Page.")

st.write("Welcome to the News-Summarizer")
st.write("This Application will summarize news of the previous day for you to read. You can read a random summary in our Top-News section. If you want to read news of a certain category check ot the category section.")
st.write("You will also be able to create your own summary. In our Own-Summary section you can insert a news-article to have it summarized for you. In addition, you will be able to download your summary as a .txt file to share with others.")
st.write("On our Homepage you can read a more general summary of the previous day.")

ima = Image.open('title_image.jpg')

st.image(ima, caption='This is a stock image Created in create.swf/Walfas')

#colums hinzufügen
#'ausklappen' und 'zuklappen' implementieren
#Funktion für die wahl einer Zufälligen news für Top news entwerfen.

