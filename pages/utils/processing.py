
import streamlit as st


def fetch_documents(documents):
    return ' '.join(document['token_y'] for document in documents)
