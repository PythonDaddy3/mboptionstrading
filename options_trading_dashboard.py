import pandas as pd
import streamlit as st

# Load the Excel file
df = pd.read_excel('/Users/pythondaddy/Desktop/trading_app/options_data.xlsx')  # Ensure this path is correct

# Streamlit app
st.title("Market Breakout Options Trading Dashboard")
st.title("Option Order Flow ")
# Filters
dates = st.multiselect(
    "Select Date:",
    options=sorted(df['Date'].unique()),
    default=None
)

symbols = st.multiselect(
    "Select Symbol:",
    options=sorted(df['Symbol'].unique()),
    default=None
)

sectors = st.multiselect(
    "Select Sector:",
    options=sorted(df['Sector'].unique()),
    default=None
)

option_expirations = st.multiselect(
    "Select Option Expiration:",
    options=sorted(df['Option Expiration'].unique()),
    default=None
)

types = st.multiselect(
    "Select Type:",
    options=sorted(df['Type'].unique()),
    default=None
)

strikes = st.multiselect(
    "Select Strike:",
    options=sorted(df['Strike'].unique()),
    default=None
)

spot_prices = st.multiselect(
    "Select Spot Price:",
    options=sorted(df['Spot Price'].unique()),
    default=None
)

open_interests = st.multiselect(
    "Select Open Interest:",
    options=sorted(df['Open Interest'].unique()),
    default=None
)

trade_qtys = st.multiselect(
    "Select Trade Qty:",
    options=sorted(df['Trade Qty'].unique()),
    default=None
)

trade_prices = st.multiselect(
    "Select Trade Price:",
    options=sorted(df['Trade Price'].unique()),
    default=None
)

bid_sizes = st.multiselect(
    "Select Bid Size:",
    options=sorted(df['Bid Size'].unique()),
    default=None
)

bids = st.multiselect(
    "Select Bid:",
    options=sorted(df['Bid'].unique()),
    default=None
)

asks = st.multiselect(
    "Select Ask:",
    options=sorted(df['Ask'].unique()),
    default=None
)

ask_sizes = st.multiselect(
    "Select Ask Size:",
    options=sorted(df['Ask Size'].unique()),
    default=None
)

trade_amount = st.multiselect(
    "Select Trade Amount:",
    options=sorted(df['Trade Amount'].unique()),
    default=None
)

sides = st.multiselect(
    "Select Side:",
    options=sorted(df['Side'].unique()),
    default=None
)

deltas = st.multiselect(
    "Select Delta:",
    options=sorted(df['Delta'].unique()),
    default=None
)

expiration_cycles = st.multiselect(
    "Select Expiration Cycle:",
    options=sorted(df['Expiration Cycle'].unique()),
    default=None
)

days_to_exp = st.multiselect(
    "Select Days To Exp:",
    options=sorted(df['Days To Exp'].unique()),
    default=None
)

events = st.multiselect(
    "Select Events:",
    options=sorted(df['Events'].unique()),
    default=None
)

# Filter the dataframe based on selections
filtered_df = df
if dates:
    filtered_df = filtered_df[filtered_df['Date'].isin(dates)]
if symbols:
    filtered_df = filtered_df[filtered_df['Symbol'].isin(symbols)]
if sectors:
    filtered_df = filtered_df[filtered_df['Sector'].isin(sectors)]
if option_expirations:
    filtered_df = filtered_df[filtered_df['Option Expiration'].isin(option_expirations)]
if types:
    filtered_df = filtered_df[filtered_df['Type'].isin(types)]
if strikes:
    filtered_df = filtered_df[filtered_df['Strike'].isin(strikes)]
if spot_prices:
    filtered_df = filtered_df[filtered_df['Spot Price'].isin(spot_prices)]
if open_interests:
    filtered_df = filtered_df[filtered_df['Open Interest'].isin(open_interests)]
if trade_qtys:
    filtered_df = filtered_df[filtered_df['Trade Qty'].isin(trade_qtys)]
if trade_prices:
    filtered_df = filtered_df[filtered_df['Trade Price'].isin(trade_prices)]
if bid_sizes:
    filtered_df = filtered_df[filtered_df['Bid Size'].isin(bid_sizes)]
if bids:
    filtered_df = filtered_df[filtered_df['Bid'].isin(bids)]
if asks:
    filtered_df = filtered_df[filtered_df['Ask'].isin(asks)]
if ask_sizes:
    filtered_df = filtered_df[filtered_df['Ask Size'].isin(ask_sizes)]
if trade_amount:
    filtered_df = filtered_df[filtered_df['Trade Amount'].isin(trade_amount)]
if sides:
    filtered_df = filtered_df[filtered_df['Side'].isin(sides)]
if deltas:
    filtered_df = filtered_df[filtered_df['Delta'].isin(deltas)]
if expiration_cycles:
    filtered_df = filtered_df[filtered_df['Expiration Cycle'].isin(expiration_cycles)]
if days_to_exp:
    filtered_df = filtered_df[filtered_df['Days To Exp'].isin(days_to_exp)]
if events:
    filtered_df = filtered_df[filtered_df['Events'].isin(events)]

# Display the filtered dataframe
st.dataframe(filtered_df)

# Additional visualizations
if 'Open Interest' in filtered_df.columns:
    st.line_chart(filtered_df['Open Interest'])
else:
    st.write("Column 'Open Interest' not found in the DataFrame.")

# Save this script as options_trading_dashboard.py and run `streamlit run options_trading_dashboard.py` in the terminal