from PIL import Image
import streamlit as st

im = Image.open("icon_1.ico")

st.set_page_config(
    page_title="News-Summarizer",
    page_icon=im
)

st.title("News-Summarizer")
#st.sidebar.success("Select a Page.")

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
    
testatiu = st.text_area("Input your article to summarize.", height=100)
submit2 = st.button("Klick2")
if submit2:
    #st.session_state["test_in"] = test_in
    st.write(testatiu)


st.download_button("Click to download.", testatiu)

#colums hinzufügen
#'ausklappen' und 'zuklappen' implementieren
#Funktion für die wahl einer Zufälligen news für Top news entwerfen.