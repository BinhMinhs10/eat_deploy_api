import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'scores': [0.6863609552383423, 0.5861597061157227],
})

st.bar_chart(df, use_container_width=False)
