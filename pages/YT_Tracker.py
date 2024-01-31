import streamlit as st
import time


from pages.utils.widget import get_channel_input, get_date_input
from pages.utils.db import get_documents
from pages.utils.processing import fetch_documents
from pages.utils.plots import generate_word_cloud, generate_bar_chart


def main():

    st.title("Youtube Channel Tracker")
    st.divider()
    channel_name = get_channel_input()
    begin_date, finish_date = get_date_input()

    documents = get_documents(channel_name, begin_date, finish_date)

    corpus = fetch_documents(documents)
    st.divider()


    tab1, tab2 = st.tabs(["Wordcloud", "Barchart"])
    with tab1:
        st.header("Wordcloud")
        generate_word_cloud(corpus)
    with tab2:
        st.header("Barchart")
        generate_bar_chart(corpus)


if __name__ == "__main__":
    main()
