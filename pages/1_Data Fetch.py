import streamlit as st
import pandas as pd
from binance.client import Client
from binance.exceptions import BinanceAPIException
import datetime


st.set_page_config(
    page_title="Data Fetch",
    page_icon="💹",
    layout='wide'
)

client_binance = Client('', '')



binanceDataHeader = ['Kline open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Kline close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Unused field, ignore.']
binanceDataframeDict = {"1min":client_binance.KLINE_INTERVAL_1MINUTE,
                        "3min":client_binance.KLINE_INTERVAL_3MINUTE,
                        "5min":client_binance.KLINE_INTERVAL_5MINUTE,
                        "15min":client_binance.KLINE_INTERVAL_15MINUTE,
                        "30min":client_binance.KLINE_INTERVAL_30MINUTE,
                        "1Hour":client_binance.KLINE_INTERVAL_1HOUR,
                        "2Hour":client_binance.KLINE_INTERVAL_2HOUR,
                        "4Hour":client_binance.KLINE_INTERVAL_4HOUR,
                        "6Hour":client_binance.KLINE_INTERVAL_6HOUR,
                        "8Hour":client_binance.KLINE_INTERVAL_8HOUR,
                        "12Hour":client_binance.KLINE_INTERVAL_12HOUR,
                        "1Day":client_binance.KLINE_INTERVAL_1DAY,
                        "3Day":client_binance.KLINE_INTERVAL_3DAY,
                        "1Week":client_binance.KLINE_INTERVAL_1WEEK,
                        "1Month":client_binance.KLINE_INTERVAL_1MONTH
                        }


st.header("Data Fetcher")
st.subheader("Fetch historical data from **Binance**(Other Exchanges will be added soon!)")
exchangeCol, CurrencyCol, timeframeCol = st.columns(3)
with exchangeCol:
    exchangeName = st.selectbox('Select the Exchange:',['Binance'])

if exchangeName == 'Binance':
    with CurrencyCol:
        if exchangeName == 'Binance':
            tempPairs = []
            for item in client_binance.get_all_tickers():
                tempPairs.append(item['symbol'])
            currencyName = st.selectbox("Currency Name:",tempPairs)

    with timeframeCol:
        if exchangeName == 'Binance':
            timeframe = st.selectbox("Select the timeframe:",binanceDataframeDict.keys())
    dateCol1, dateCol2 = st.columns(2)
    with dateCol1:
        dateFrom = st.date_input("From:")

    with dateCol2:
        dateTo = st.date_input("To:")

    infoCol, downloadCol = st.columns(2)
    with infoCol:
        st.info(exchangeName + "      " + currencyName + "      " + timeframe, icon="ℹ️")


    with downloadCol:
        downloadButton = st.button("Download Data")




    if downloadButton:
        tempCurrencyName = currencyName
        klines = client_binance.get_historical_klines(tempCurrencyName,binanceDataframeDict[timeframe],start_str=str(dateFrom),end_str=str(dateTo))
        df = pd.DataFrame(klines,columns=binanceDataHeader).drop(columns=['Unused field, ignore.'])
        # df.drop(columns=['Unused field, ignore.'],inplace=True)
        st.write(df)
        saveAsCol, SaveButCol = st.columns(2)
        with saveAsCol:
            selectAs = st.selectbox("Download As:",['csv'])
        with SaveButCol:
            if selectAs == 'csv':
                st.download_button(
                    label="Download as CSV",
                    data=df.to_csv(index=False),
                    file_name='teststreamlitaaa.csv',
                    mime='text/csv'
                )

else:
    st.warning("In this version you can only use **Binance**. Other Exchanges will be added soon!", icon="⚠️")

