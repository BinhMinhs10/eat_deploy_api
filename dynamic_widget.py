import streamlit as st
import pandas as pd

@st.cache
def load_data():
    return pd.read_csv("streamlit_football_visualize/football_data.csv")


@st.cache
def describe_sample(dataset, nrows):
    sample = dataset.head(nrows)
    return sample.describe()


data = load_data()  # data import: ✅
described_sample = describe_sample(data, 100)  # input into streamlit object: ✅
st.write(described_sample)
