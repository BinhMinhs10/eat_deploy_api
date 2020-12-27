import streamlit as st
import numpy as np
import pandas as pd

st.title('My first app')
st.write('Here first attempt at using data')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df

# Draw charts and maps: Matplotlib, Altair, deck.gl
# using checkboxes to show/hide data
if st.checkbox('show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

# display data point on a map (sample in San Francisco)
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)



