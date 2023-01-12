import streamlit as st
st.set_page_config(
    page_title="New Test"
)

st.title("Main Paige")
st.sidebar.success("Select a Page.")

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
    