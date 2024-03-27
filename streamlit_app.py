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
    st.title("Multi-DataFrame Streamlit App")

    # Generate sample DataFrames
    dataframes = generate_dataframes()

    # Display DataFrames in columns
    #columns = st.columns(10)  # Change the number of columns as needed
    #for i, (name, df) in enumerate(dataframes.items()):
    #    columns[i % 3].header(name)
    #    columns[i % 3].dataframe(df)

# Run the main function
if __name__ == "__main__":
    main()
