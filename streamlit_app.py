
To display DataFrames side by side, filling as many columns as will fit on the screen, you can use Streamlit's beta_columns layout feature dynamically. Here's how you can modify the code:

python
Copy code
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

    # Calculate the number of columns that will fit on the screen
    num_columns = st.beta_columns(20)

    # Display DataFrames side by side
    col_index = 0
    for name, df in dataframes.items():
        with num_columns[col_index % len(num_columns)]:
            st.header(name)
            st.dataframe(df)
        col_index += 1

# Run the main function
if __name__ == "__main__":
    main()