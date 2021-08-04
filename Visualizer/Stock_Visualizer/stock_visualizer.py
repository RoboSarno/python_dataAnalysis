import pandas as pd
import streamlit as st
import yfinance as yf

st.write(""" # Simple Stock Price App 
         
         Shown are the stock **closing price** and **volume** of Google! 
         It uses streamlit, yfinance, and pandas.
         
         """)

#define the ticker symbol
tickerSymb = 'GOOGL'

tickerData = yf.Ticker(tickerSymb)

tickerDf = tickerData.history(period='1m', start='2010-5-31', end='2021-6-01')

st.write("""
         ## Closing Price
         """)
st.line_chart(tickerDf.Close)

st.write("""
         ## Volume Price
         """)
st.line_chart(tickerDf.Volume) 


