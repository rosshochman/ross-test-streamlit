import streamlit as st
import pandas as pd
import random
import string
import time


st.set_page_config(layout="wide")

# Function to generate a random string
def random_string(length=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Define function to generate sample DataFrames with random strings
def generate_dataframes():
    dataframes = {}
    counter = 1
    while counter <= 4:
        df = pd.DataFrame({
            f'Column {i}': [random_string() for _ in range(25)] for i in range(1, 5)
        })
        dataframes[f'DataFrame {counter}'] = df
        counter += 1
    return dataframes

# Main function to display the Streamlit app
def main():


    # Generate sample DataFrames with random strings
    dataframes = generate_dataframes()

    # Calculate the maximum width of any DataFrame
    max_width = max(df.shape[1] * 100 for df in dataframes.values())

    # Display DataFrames in columns
    columns = st.columns(4)  # 15 columns
    for i, (name, df) in enumerate(dataframes.items()):
        with columns[i % 4]:
            st.header(name)
            st.dataframe(df, width=max_width)

# Run the main function continuously

main()
time.sleep(1)  # Add a delay (in seconds) to control the frequency of execution
