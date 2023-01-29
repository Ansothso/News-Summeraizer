import streamlit as st

st.title("Sports News")
st.write("Read the latest sports news.")

f = open("Testi.txt", encoding="utf-8")
#st.write(f.read())
#f.close()

col1, col2 = st.columns(2)

with col1:
   with st.expander("#1 TOP-NEWS"):
       st.write(f.read())

   with st.expander("#3 TOP-NEWS"):
       st.write(" The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random.")

with col2:
   with st.expander("#2 TOP-NEWS"):
       st.write(" The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random.")

   with st.expander("#4 TOP-NEWS"):
       st.write(" The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random.")
