from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st
from collections import Counter


def generate_word_cloud(corpus):
    try:

        wordcloud = WordCloud(width=800, height=400,
                              background_color='white').generate(corpus)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot()
    except:
        st.info("No existe registros para los parámetros especificados", icon="ℹ️")


def generate_bar_chart(corpus):
    try:
        words_list = corpus.split()
        word_counts = Counter(words_list)
        top_words = word_counts.most_common(10)

        labels, counts = zip(*top_words)

        plt.bar(labels, counts)
        plt.xlabel("Words")
        plt.xticks(rotation='vertical')
        plt.ylabel("Frequency")
        plt.title("Word Frequency Bar Chart")
        st.pyplot()
    except:
        st.info("No existe registros para los parámetros especificados", icon="ℹ️")
