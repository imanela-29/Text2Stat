"""Main module for the streamlit app"""
import streamlit as st

import awesome_streamlit as ast
import src.pages.actu_page
import src.pages.notes_page
import src.pages.home
import src.pages.event_page

st.set_page_config(page_title='Text2Stat - UMP', page_icon='src/img/textpng.png')

ast.core.services.other.set_logging_format()

PAGES = {
    "Home": src.pages.home,
    "News": src.pages.actu_page,
    "Events": src.pages.event_page,
    "Notes": src.pages.notes_page,
}


def main():

    col1, col2, col3 = st.beta_columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.image('src/img/Text.png')

    with col3:
        st.write("")

    st.sidebar.header("Hello World")
    selection = st.sidebar.radio("Select Page", list(PAGES.keys()))
    page = PAGES[selection]
    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)
    
    st.sidebar.info("The pages we are going to analyze from ump.ma are the news page [ump.ma/actualite](http://www.ump.ma/fr/actualite) , the events page [ump.ma/events](http://www.ump.ma/fr/events), the notes page [ump.ma/notes](http://www.ump.ma/fr/notes)")
    st.sidebar.title("About")
    st.sidebar.success("""
        This is an application that automates the process of text analysis of the University Mohamed First Website [ump.ma](https://ump.ma) with a user-friendly GUI. It has been implemented using Python and deployed with the Streamlit package.""")


if __name__ == "__main__":
    main()
