import streamlit as st
from PIL import Image

im = Image.open("icon_1.ico")

st.set_page_config(
    page_title="Help",
    page_icon=im
)

st.title("Help")
st.write("This page consists of a [user manual](#user-manual) and [FAQ](#faq).")

st.header("User Manual")
st.write("The user manual gives an overview of the pages, as well as explains the functionalities of the website.")

st.subheader("Pages Overview")

st.write("For navigating and exploring the website, you can use the sidebar on the left. There are seven pages you can visit:")
st.write("1. Home")
st.write("This the homepage, where you can get a brief overview of the whole website. Moreover, you can read different summaries listed as top news.")
st.write("2. Sports")
st.write("This page provides the summaries of the latest sport news.")
st.write("3. Politics")
st.write("This page provides the summaries of the latest political news.")
st.write("4. Business")
st.write("This page provides the summaries of the latest business news.")
st.write("5. Summary Generator")
st.write("This page generates a summary of an input text.")
st.write("6. Help")
st.write("This page provides an overview of all the functions of the website.")
st.write("7. Contact")
st.write("This page contains contact information and a contact form.")


st.subheader("News Articles")

st.write('''The categories "Sports", "Politics" and "Business" contain the most important news articles of the day. The news articles are selected from reliable sources, such as BBC and The Guardian, and are already summarized. \n 
On these pages, you can see different boxes with article headlines in them, as displayed in Figure 1. To read them, click on the box or headline. The box expands to show the summarized article and also provides a link, which takes you to the original article, as displayed in Figure 2.''')

col1, col2 = st.columns(2)
image1 = Image.open('images/newsarticle-box1.jpg')
image2 = Image.open('images/newsarticle-box0.jpg')

with col1:
    st.image(image1, 'Figure 1: Collapsed boxes')
with col2:
    st.image(image2, 'Figure 2: Expanded boxes')

st.subheader("Summary Generator")
st.write('''To generate a summary for an article of choice, you can go the summary generator page. There you can paste the text of the article in the input field and click the "Generate" button. The summary will appear below the "Generate" button. The generated text can be downloaded as a .txt file by clicking the "Download" button.''')


st.header("FAQ")
st.write("FAQs and their answers will be published soon.")


st.write("For comments, complaints, suggestions, or further questions, you can reach us via the [Contact](/Contact) page. Fill in the form and send it to us.")