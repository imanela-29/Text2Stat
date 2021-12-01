"""Home page shown when the user enters the application"""
import streamlit as st

import awesome_streamlit as ast


# pylint: disable=line-too-long
def write():
    st.write("")
    st.write("")

    st.success("""Welcome to our web application allowing text Processing and Analysis of the University Mohamed First Website [ump.ma](https://ump.ma)  
    It's built in with multiple features which can be accessed from the left side bar.""")
    
    st.info("Visual tool, provides more informations about the text content of the website [ump.ma](https://ump.ma), descriptives stats, word frequency distribution, what appears more. In order to improve the content, textual communication targets the public, also to promote the missions of the university and enhance social communicationin general. ")

    st.write("Using natural language processing techniques, NLP is actually an interdisciplinary field between text analysis, computational linguistics, AI and machine learning.")