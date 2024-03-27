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

    # Calculate the number of columns based on the screen width
    max_columns = st.beta_columns(20)
    num_columns = len(max_columns)

    # Display DataFrames side by side
    for i, (name, df) in enumerate(dataframes.items()):
        if i % num_columns == 0:
            columns = st.beta_columns(num_columns)
        with columns[i % num_columns]:
            st.header(name)
            st.dataframe(df)

# Run the main function
if __name__ == "__main__":
    main()
