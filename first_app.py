import streamlit as st
import numpy as np
import pandas as pd

st.title('My first app')

# layout organize widgets
add_selectbox = st.sidebar.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home page', 'Mobile phone')
)

add_slider = st.sidebar.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0)
        )


left_column, right_column = st.beta_columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


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

# use a selecbox for options
option =  st.selectbox(
        'which number do you like best?',
        df['first column'])
'You selected: ', option


# Layout app
left_column, right_column = st.beta_columns(2)
pressed = left_column.button('press me?')
if pressed:
    right_column.write('Hi i`m Minh')
expander = st.beta_expander('FAQ')
expander.write('Here you could put in some really')


# Display status in real time
import time
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


