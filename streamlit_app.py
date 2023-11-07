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
