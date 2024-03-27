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

# Calculate the number of columns based on the screen width
def calculate_num_columns(column_width=300):
    max_width = st._get_report_ctx().width - 30  # Subtracting padding
    return max(1, int(max_width / column_width))

# Main function to display the Streamlit app
def main():
    st.title("Multi-DataFrame Streamlit App")

    # Generate sample DataFrames
    dataframes = generate_dataframes()

    # Calculate the number of columns
    num_columns = calculate_num_columns()

    # Display DataFrames side by side
    col_index = 0
    for name, df in dataframes.items():
        if col_index % num_columns == 0:
            st.write('')
        st.header(name)
        st.dataframe(df)
        col_index += 1

# Run the main function
if __name__ == "__main__":
    main()
