import streamlit as st
import pandas as pd

st.write('Welcome to Streamlit')

def generate_dataframes():
    dataframes = {}
    for i in range(1, 21):
        df = pd.DataFrame({
            'Column 1': [f'Data {i}-1', f'Data {i}-2', f'Data {i}-3'],
            'Column 2': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C']
        })
        dataframes[f'DataFrame {i}'] = df
    return dataframes

# Function to display DataFrame section
def display_dataframe_section(dataframes):
    for name, df in dataframes.items():
        st.header(name)
        st.write(df)
# Generate sample DataFrames
dataframes = generate_dataframes()

# Display DataFrame sections
display_dataframe_section(dataframes)