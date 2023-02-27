import streamlit as st
from PIL import Image

st.title("Help")


st.header("First Steps")


st.subheader("Navigation")

st.write("For navigation and exploring our website, you can use the sidebar on the left. There are eight pages you can visit:")
st.write("1. Home")
st.write("This our homepage, where you can get a brief overlook of our website.")
st.write("2. Top-News")
st.write("In this page you can read the most important news-articles briefly.")
st.write("3. Sports")
st.write("This page provides all important summarized sportsnews of the day.")
st.write("4. Politics")
st.write("This page provides all important summarized news about (inter-)national politics of the day.")
st.write("5. Business")
st.write("This page provides all important summarized news about business and economics of the day.")
st.write("6. Own Summary")
st.write("Here you can you our intelligent summarizer-machine for summarizing news-texts you want.")
st.write("7. Help")
st.write("The pages, where you are currently, provides instructions for using our website comfortably.")
st.write("8. Contact")
st.write("This page contains all of our contact information and a contact form.")


st.subheader("News-Articles")

st.write("The categories Top-News, Sports, Politics and Business contain the most important and viral news-articles of the day. The news-articles are selected from reliable sources such as BBC and The Guardian and are already summarized by our transformer.")
st.write("If you open one of this pages or categories, you are going to see boxes with headline of each article. To read them, you have to go to the box/headline and click on it. The box opens up and then you are able to read the article.")

col1, col2 = st.columns(2)
image1 = Image.open('newsarticle-box0.png')
image2 = Image.open('newsarticle-box1.png')

with col1:
    st.image(image1, 'Before')
with col2:
    st.image(image2, 'After')

st.subheader("Own Summary")
st.write("Using the Summarizer for your interesting news-articles, go to the sidebar and open 'Own Summary'. Copy the text of the article, paste in into the text-box below the text-line 'Input your article to summarize' and press 'Klick2'-button. It might take a little time to summarize your text depending on the size of it. However, the summary pops up below the buttons.")
st.write("Nevertheless, if you don't want to copy the whole summary, you can export it into a .txt-file by pressing the 'Click to download'-button.")


st.header("FAQ")
st.write("FAQs and their answers are going to be published as soon as possibe.")


st.header("Further Questions and Help")
st.write("For further questions about the website, our intelligent machine or us, you can reach us via the Contact page. Fill the form and submit it to us.")