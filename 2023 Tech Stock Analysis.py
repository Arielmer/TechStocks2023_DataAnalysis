import yfinance as yf
import pandas as pd
import numpy as np
import datetime

# -----------------------------
# Part 1: Load Stock Data
# -----------------------------
# Define the start and end dates for the analysis
start = datetime.datetime(2023, 1, 1)
end = datetime.datetime(2023, 12, 31)

# List of company tickers
tickers = {
    "Amazon": "AMZN",
    "Meta": "META",
    "Alphabet": "GOOG",
    "Microsoft": "MSFT",
    "Apple": "AAPL"
}

# Download stock data for each company and store in a dictionary
data_frames = {}
for company, ticker in tickers.items():
    df = yf.download(ticker, start, end)
    df.reset_index(inplace=True)
    df["Company"] = company
    data_frames[company] = df

# Combine all individual DataFrames into one
all_data = pd.concat(data_frames.values(), ignore_index=True)

# Display dataset summary
print(all_data.head())

# -----------------------------
# Part 2: Stock Analysis
# -----------------------------
# Compute average closing price for each company
average_closing_prices = all_data.groupby("Company")["Close"].mean()
print("\nAverage Closing Prices:")
print(average_closing_prices)

# Compute maximum closing price for each company
max_closing_prices = all_data.groupby("Company")["Close"].max()
print("\nMaximum Closing Prices:")
print(max_closing_prices)

# -----------------------------
# Part 3: Stock Returns Analysis
# -----------------------------
# Create a new DataFrame containing 'Date', 'Company', and 'Close' columns
returns = all_data[["Date", "Company", "Close"]].copy()

# Calculate daily returns in percentage
def compute_returns(group):
    return (group / group.shift(1) - 1) * 100

returns["Returns"] = returns.groupby("Company")["Close"].apply(compute_returns).reset_index(level=0, drop=True)
returns.dropna(inplace=True)  # Remove NaN values from the first row of each group

# Identify best and worst single-day returns for each company
best_returns = returns.loc[returns.groupby("Company")["Returns"].idxmax()]
worst_returns = returns.loc[returns.groupby("Company")["Returns"].idxmin()]

# Rename columns for clarity
best_returns = best_returns.rename(columns={"Date": "Best_Return_Date", "Returns": "Best_Return_Percentage"})
worst_returns = worst_returns.rename(columns={"Date": "Worst_Return_Date", "Returns": "Worst_Return_Percentage"})

# Merge best and worst returns into a single DataFrame
extreme_returns = pd.merge(
    best_returns[["Company", "Best_Return_Date", "Best_Return_Percentage"]],
    worst_returns[["Company", "Worst_Return_Date", "Worst_Return_Percentage"]],
    on="Company"
)

# Format percentage values for better readability
extreme_returns["Best_Return_Percentage"] = extreme_returns["Best_Return_Percentage"].map("{:.2f}%".format)
extreme_returns["Worst_Return_Percentage"] = extreme_returns["Worst_Return_Percentage"].map("{:.2f}%".format)

# Display best and worst single-day returns
print("\nBest and Worst Single-Day Returns:")
print(extreme_returns)
