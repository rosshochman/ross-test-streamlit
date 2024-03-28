import streamlit as st
import pandas as pd
import requests
import time
st.set_page_config(layout="wide")
st.title("Penny Stock Data Science")


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
        formatted_percentage_str = '{:.2f}%'.format(percentage_float)
        if percentage_float > 0:
            formatted_percentage_str = "+"+formatted_percentage_str
        change_str = i["todaysChange"]
        change_float = float(change_str)
        if change_float > 0:
            change_str = "+"+change_str
        dayDic = i["day"]
        dayV = dayDic["v"]
        dayVint = int(dayV)
        dayVW = dayDic["vw"]
        dayVWfloat = float(dayVW)
        daylastTrade = i["lastTrade"]
        dayPrice = daylastTrade["p"]
        dayPriceFloat = float(dayPrice)
        dollarValue = dayPriceFloat*dayVWfloat
        new_list = [ticker,dayPriceFloat,dayVWfloat,percentage_float,change_float,dollarValue]
        master_list.append(new_list)
    columns = ["Ticker","Price","VWAP","% Change","$ Change","$ Volume"]
    df = pd.DataFrame(master_list, columns=columns)
    df_sorted = df.sort_values(by="% Change", ascending=False).head(100)
    return df_sorted

def main():


    # Infinite loop to continuously update data
    while True:
        try:
            # Fetch data from Polygon.io API
            df1 = fetch_data()

            # Display data frames
            st.header('Stocks')
            st.dataframe(df1)


            # Sleep for 1 second before making the next API call
            time.sleep(1)

        except Exception as e:
            continue

# Run the Streamlit app
if __name__ == '__main__':
    main()