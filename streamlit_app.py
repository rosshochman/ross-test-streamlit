import streamlit as st
import pandas as pd

# Define function to generate sample DataFrames
def generate_dataframes():
    dataframes = {}
    for i in range(1, 21):
        df = pd.DataFrame({
            'Column 1': [f'Data {i}-1', f'Data {i}-2', f'Data {i}-3'],
            'Column 2': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C']
        })
        dataframes[f'DataFrame {i}'] = df
    return dataframes

# Main function to display the Streamlit app
def main():
    st.set_page_config(layout="wide")
    st.title("Multi-DataFrame Streamlit App")

    # Generate sample DataFrames
    dataframes = generate_dataframes()

    # CSS to override Streamlit's default layout
    st.markdown("""
    <style>
    .stApp {
        max-width: 100%;
    }
    .stApp > div:first-child {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

    # Display DataFrames in columns
    columns = st.columns(15)  # Change the number of columns to 15
    for i, (name, df) in enumerate(dataframes.items()):
        with columns[i % 15]:
            st.markdown(f'<div style="padding: 10px; border: 1px solid #ccc;">', unsafe_allow_html=True)
            st.header(name)
            st.dataframe(df)
            st.markdown('</div>', unsafe_allow_html=True)

# Run the main function
if __name__ == "__main__":
    main()
