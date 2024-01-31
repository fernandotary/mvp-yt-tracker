import time
import streamlit as st
import numpy as np
import pandas as pd

st.header("Trying out streamlit pages")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

x = st.slider('x')  # this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    chart_data


df1 = pd.DataFrame({
    'first column': [5, 6, 7, 8],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
    ['a', 'b', 'c'])

'You selected: ', option


add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)


col1, col2 = st.columns(2)

with col1:
    st.write("Contenido de la columna 1")
    st.write("Contenido de la columna 1")
    st.write("Contenido de la columna 1")
    st.write("Contenido de la columna 1")

with col2:
    st.write("Contenido de la columna 2")
    st.write("Contenido de la columna 2")
    st.write("Contenido de la columna 2")
    st.write("Contenido de la columna 2")


with st.sidebar.expander("Haz clic para expandir"):
    st.write(
        "Contenido oculto que se mostrará al hacer clic en la flecha de expansión.")


'holi'



# session
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")


if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(
        np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)
