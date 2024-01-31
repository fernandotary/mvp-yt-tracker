
import streamlit as st


def fetch_documents(documents):
    return ' '.join(document['token'] for document in documents)
