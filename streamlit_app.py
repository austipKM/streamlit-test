import streamlit as st
import pandas as pd

"""# Welcome to the demo app"""

df = pd.DataFrame({
    "x": [0, 1, 2],
    "y": [0, 1, 2],
})

"""## Modify plots directly from their respective tables"""
with st.container():
    st.write('Modify the values in the table to change the plot')
    modified_data = st.data_editor(df, use_container_width=True)

    st.line_chart(modified_data, x="x", y="y", use_container_width=True)

"""## Modify plots with sliders"""
with st.container():
    st.write('Use slider to change the number of bars in the plot')
    slider_value = st.slider('Number of bars', 0, 100, 50, 1)
    slider_data = pd.Series([i for i in range(slider_value)])

    st.bar_chart(slider_data, use_container_width=True)

"""## Input chaining """
with st.container():
    st.write("Change the first slider. Notice how the second slider's max value changes to be the first slider's value.")

    limit = st.slider('Set limit of Output', 0, 10, 1, 1)
    st.slider('Output', 0, limit, 0, 1)
