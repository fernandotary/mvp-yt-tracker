import streamlit as st
import certifi
from pymongo import MongoClient


def get_documents(channel_name, begin_date, finish_date):
    uri = st.secrets.mongo_connection
    ca = certifi.where()

    try:
        client = MongoClient(uri, tlsCAFile=ca)
        db = client['YNews']
        collection = db['y_channel_backup_2']

        documents = collection.find({"channel_name": channel_name, "publishedAt": {
                                    "$gte": begin_date, "$lte": finish_date}}, {"token": 1})
        return documents

    except Exception as e:
        return f"Error de conexión: {e}"
