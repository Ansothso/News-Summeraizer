import streamlit as st
from PIL import Image

im = Image.open("icon_1.ico")

st.set_page_config(
    page_title="Contact",
    page_icon=im
)

st.title("Contact")
st.write("Information about the creators.")

st.header("Contact Form")

#E-Mail adress needs to be changed and validated once
contact = """
<form action="https://formsubmit.co/news-summarizer@proton.me" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your E-Mail" required>
     <textarea name="message" placeholder="Your Message"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("pages\style.css")

st.header("Address")


image1 = Image.open('images/map.png')

st.write("""News Summarizer Team \n
Robert-Mayer-Str. 11-15,
60325 Frankfurt am Main
""")
    
st.image(image1, 'Location')
