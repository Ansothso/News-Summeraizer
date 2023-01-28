import streamlit as st

st.title("About Us")
st.write("Information about the creators.")

#E-Mail adress needs to be changed and validated once
contact = """
<form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
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
