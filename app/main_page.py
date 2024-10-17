import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="OpenQuant", layout="wide")

# Title
st.title("OpenQuant")

# Sidebar for asset selection
asset_types = ["Stocks", "ETFs", "Indices", "Forex", "Futures", "Crypto"]
selected_asset_type = st.sidebar.selectbox("Select Asset Type", asset_types)

# Asset selector (placeholder - you'd need to implement a proper asset lookup)
asset = st.sidebar.text_input("Enter Asset Symbol (e.g., AAPL for Apple Inc.)")

# Time window selector
time_windows = ["Intraday", "Daily", "Weekly", "Monthly", "Yearly"]
selected_time_window = st.sidebar.selectbox("Select Time Window", time_windows)

# Fetch data (placeholder - you'd need to implement proper data fetching)
if asset:
    data = yf.download(asset, period="1y")
else:
    data = pd.DataFrame()

# Main chart
if not data.empty:
    fig = go.Figure()
    
    # Candlestick chart
    fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'],
                                 name='Price'))
    
    # Volume chart
    fig.add_trace(go.Bar(x=data.index, y=data['Volume'], name='Volume', yaxis='y2'))
    
    # Update layout
    fig.update_layout(
        title=f'{asset} Stock Price and Volume',
        yaxis_title='Price',
        yaxis2=dict(title='Volume', overlaying='y', side='right'),
        xaxis_rangeslider_visible=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Returns and Volatility chart
    returns = data['Close'].pct_change()
    volatility = returns.rolling(window=20).std()
    
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=data.index, y=returns, name='Returns'))
    fig2.add_trace(go.Scatter(x=data.index, y=volatility, name='Volatility', yaxis='y2'))
    
    fig2.update_layout(
        title='Returns and Volatility',
        yaxis_title='Returns',
        yaxis2=dict(title='Volatility', overlaying='y', side='right')
    )
    
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.write("Please enter a valid asset symbol to display charts.")
