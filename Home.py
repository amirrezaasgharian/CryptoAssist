import streamlit as st
import pandas as pd
from binance.client import Client
from binance.exceptions import BinanceAPIException

st.set_page_config(
    page_title="CryptoAssist - Home",
    page_icon="💹",
    layout='wide'
)

st.title("Welcome to CryptoAssist V 0.1")
# st.subheader("This system would help you to Fetch historical data from Binance and Kucoin (Other Exchanges will be added soon!)")
st.write("""
This system would help you get much deeper insights about cryptocurreny and you can use it as an algo-trading assistant.
""")

st.subheader("Data Fetch")
st.write("""
You can Fetch historical data from different exchanges in all available **timeframes** and currencies between your selected dates. \n
Available Exchanges : **Binance** - **KuCoin** \n
**Note:** Other Exchanges will be added to the list soon!
""")

st.warning('If you are using this app from **Iran**, turn on your VPN first!', icon="⚠️")

c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Data Scientist: [Amirreza Asgharian](https://instagram.com/amirrezaasgharian)**', icon="💡")
with c2:
    st.info('**GitHub: [@amirrezaasgharian](https://github.com/amirrezaasgharian)**', icon="💻")
with c3:
    st.info('**LinkedIn: [amirrezaasgharian](https://www.linkedin.com/in/amirreza-asgharian/)**', icon="🚩")