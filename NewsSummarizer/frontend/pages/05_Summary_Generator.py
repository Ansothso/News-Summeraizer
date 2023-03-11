import streamlit as st
from utilities.summarizer import get_summary
from PIL import Image

im = Image.open("icon_1.ico")

st.set_page_config(
    page_title="Summary",
    page_icon=im
)

st.title("Create your own Summary")
st.write("You are able to input your own text into the textfield. By pressing the button you will generate your own summary.")

if "test_in" not in st.session_state:
   st.session_state["test_in"] = ""

test_in = st.text_input("This test", st.session_state["test_in"])
submit = st.button("Klick")
if submit:
    st.session_state["test_in"] = test_in
    st.write(test_in)

newtest = st.button("Generate Text")
if newtest:
    f = open("Testi.txt", encoding="utf-8")
    st.write(f.read())
    f.close()
    
wiedtest = ""
testatiu = st.text_area("Input your article to summarize.", height=100)
submit2 = st.button("Klick2")
if submit2:
    tee2 = testatiu.replace('\n', ' ')
    wiedtest = get_summary(tee2)
    #st.session_state["test_in"] = test_in
    st.write(wiedtest)


st.download_button("Click to download.", wiedtest)