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
    st.set_page_config(layout="wide")  # Set page layout to wide
    st.title("Multi-DataFrame Streamlit App")

    # Generate sample DataFrames
    dataframes = generate_dataframes()

    # Display DataFrames in columns
    columns = st.columns(15)  # Change the number of columns to 15
    for i, (name, df) in enumerate(dataframes.items()):
        with columns[i % 15]:
            st.markdown(f'<div style="width: 600px; padding: 10px; border: 1px solid #ccc;">', unsafe_allow_html=True)
            st.header(name)
            st.dataframe(df)
            st.markdown('</div>', unsafe_allow_html=True)

# Run the main function
if __name__ == "__main__":
    main()
