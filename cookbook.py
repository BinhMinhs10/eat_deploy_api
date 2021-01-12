import streamlit as st
import numpy as np
import time
import pandas as pd

st.title('App cookbook')

# insert elements out of order================
st.text('This will appear first')
my_slot1 = st.empty() # empty slot
my_slot2 = st.empty()
data = np.random.randn(10, 2)
data2 = np.random.randn(10, 2)
st.text('This will appear last')
my_slot1.text(data)
my_slot2.line_chart(data).add_rows(data2)


# Animate elements=============================
progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))
for i in range(100):
    # update progress bar
    progress_bar.progress(i+1)
    new_rows = np.random.randn(10, 2)
    status_text.text(
        'The lastest random number is: %s'% new_rows[-1, 1]
    )

    # append data to the chart
    chart.add_rows(new_rows)
    time.sleep(0.1)
status_text.text('Done!')
st.balloons()