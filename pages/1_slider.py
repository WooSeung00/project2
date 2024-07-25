import streamlit as st

text = st.text_input("입력")
if st.button("Save"):
    st.session_state.text = text

    #session_state는 키와 값으로 나뉜다
    #session_state.key or
    #session_state["key"]