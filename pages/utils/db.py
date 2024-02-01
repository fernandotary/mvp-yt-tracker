import streamlit as st
import certifi
from pymongo import MongoClient


def get_documents(channel_id, begin_date, finish_date):
    uri = st.secrets.mongo_connection
    ca = certifi.where()

    try:
        client = MongoClient(uri, tlsCAFile=ca)
        db = client['YNews']
        collection = db['y_channel_transcripts']

        count_with_token = collection.count_documents(
            {'token': {'$exists': True}})

        documents = collection.find({"channel_id": channel_id, "publishedAt": {
                                    "$gte": begin_date, "$lte": finish_date}})
        return documents

    except Exception as e:
        return f"Error de conexión: {e}"
