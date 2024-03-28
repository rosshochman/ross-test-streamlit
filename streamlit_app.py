import streamlit as st
import pandas as pd

# Define function to generate sample DataFrames
def generate_dataframes():
    dataframes = {}
    for i in range(1, 6):  # 15 columns
        df = pd.DataFrame({
            'Column 1': [f'Data {i}-1', f'Data {i}-2', f'Data {i}-3'],
            'Column 2': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C'],
            'Column 3': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C'],
            'Column 3': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C'],
            'Column 3': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C'],
            'Column 3': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C'],
            'Column 3': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C'],
            'Column 3': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C'],
            'Column 3': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C'],
            'Column 3': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C'],
            'Column 3': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C'],
            'Column 3': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C'],
            'Column 3': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C'],
            'Column 3': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C'],
            'Column 3': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C'],
            'Column 3': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C'],
            'Column 3': [f'Data {i}-A', f'Data {i}-B', f'Data {i}-C']
        })
        dataframes[f'DataFrame {i}'] = df
    return dataframes

# Main function to display the Streamlit app
def main():
    st.set_page_config(layout="wide")  # Set page layout to wide
    #st.title("Multi-DataFrame Streamlit App")

    # Generate sample DataFrames
    dataframes = generate_dataframes()

    # Calculate the maximum width of any DataFrame
    max_width = max(df.shape[1] * 100 for df in dataframes.values())

    # Display DataFrames in columns
    columns = st.columns(5)  # 15 columns
    for i, (name, df) in enumerate(dataframes.items()):
        with columns[i % 5]:
            st.header(name)
            st.dataframe(df, width=max_width)

# Run the main function
if __name__ == "__main__":
    main()
