"""
A Streamlit UI for removing outliers from a list of words
Nikhil Dave
"""

import streamlit as st
from main import remove_outliers
from wv import Model


@st.cache_resource
def get_model(filename: str):
    return Model(filename)


st.title("Word Outlier Remover")

st.markdown(
    'This app takes a list of words, determines any "outlier" words, and '
    "removes them."
)
words = st.text_input(
    "Please enter a comma-separated list of words").split(",")

# Remove whitespace
words = [w.strip() for w in words]

filtered_words = remove_outliers(get_model("model.txt"), words)

if filtered_words:
    st.subheader("List with outliers removed:")

    sep = ", "
    text = sep.join(filtered_words)

    st.markdown(text)
