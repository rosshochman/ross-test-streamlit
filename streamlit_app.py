import streamlit as st
import pandas as pd
import requests
import time
st.set_page_config(layout="wide")
st.title("Penny Stock Data Science")

def format_percentage(value):
    if value >= 0:
        return '+{:.2%}'.format(value)
    else:
        return '{:.2%}'.format(value)

def fetch_data():
    master_list = []
    url = "https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers?include_otc=true&apiKey=DT909L2IQJNAOmTWBgpPsNHo6m8AWuD4"
    #add something to get lists of otc vs listed
    response = requests.get(url)
    data = response.json()
    tickers_list = data["tickers"]
    for i in tickers_list:
        ticker = i["ticker"]
        percentage_str = i["todaysChangePerc"]
        percentage_float = float(percentage_str)
        change_str = i["todaysChange"]
        change_float = float(change_str)
        dayDic = i["day"]
        dayV = dayDic["v"]
        dayVint = int(dayV)
        dayVW = dayDic["vw"]
        dayVWfloat = float(dayVW)
        daylastTrade = i["lastTrade"]
        dayPrice = daylastTrade["p"]
        dayPriceFloat = float(dayPrice)
        dollarValue = int(dayVint*dayVWfloat)
        epoch_time = int(time.time())
        new_list = [ticker,dayPriceFloat,dayVWfloat,percentage_float,dayVint,dollarValue,epoch_time]
        master_list.append(new_list)
    columns = ["Ticker","Price","VWAP","% Change","Volume","$ Volume","Time"]
    df = pd.DataFrame(master_list, columns=columns, index=False)
    df_sorted = df[df['Price'] > 1].sort_values(by="% Change", ascending=False).head(100)
    df_sorted['Price'] = df_sorted['Price'].round(2)
    df_sorted['VWAP'] = df_sorted['VWAP'].round(2)
    df_sorted["% Change"] = df_sorted["% Change"].apply(format_percentage)

    return df_sorted

def main():
    st.header('Stocks')
    df1 = st.empty()
    
    

    # Infinite loop to continuously update data
    while True:
        try:
            # Fetch data from Polygon.io API
            new_df1 = fetch_data()

            # Display data frames
            
            df1.dataframe(new_df1)

            # Sleep for 1 second before making the next API call
            time.sleep(.1)

        except Exception as e:
            continue

# Run the Streamlit app
if __name__ == '__main__':
    main()