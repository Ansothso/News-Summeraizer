import streamlit as st
from PIL import Image

image = Image.open('images/banner_topnews.png')
st.title("Test-News")
st.image(image)
st.caption("Image by [Cottonbro Studio](https://www.pexels.com/de-de/foto/espresso-fruhstuck-nachrichten-zeitung-3944425/)")

st.write("Read the latest news.")



st.write("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.")

col1, col2 = st.columns(2)

with col1:
   with st.expander("#1 TOP-NEWS"):
       st.write(" The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random.")

   with st.expander("#3 TOP-NEWS"):
       st.write(" The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random.")

with col2:
   with st.expander("#2 TOP-NEWS"):
       st.write(" The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random.")

   with st.expander("#4 TOP-NEWS"):
       st.write(" The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random.")
