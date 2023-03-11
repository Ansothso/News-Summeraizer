import streamlit as st
from utilities.summarizer import get_summary
from PIL import Image

im = Image.open("icon_1.ico")

st.set_page_config(
    page_title="Summary",
    page_icon=im
)

st.title("Create your own Summary")
st.write('You can input your own text into the textfield. By clicking the "Generate" button, a summary will be generated. This summary can also be downloaded as a .txt file.')
    
wiedtest = ""
testatiu = st.text_area("Input your article to summarize.", height=300)
submit2 = st.button("Generate")
if submit2:
    tee2 = testatiu.replace('\n', ' ')
    wiedtest = get_summary(tee2)
    #st.session_state["test_in"] = test_in
    st.write(wiedtest)

st.download_button("Click to download", wiedtest)