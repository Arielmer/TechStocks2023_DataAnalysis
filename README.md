# Stock Analysis Using Yahoo Finance API

## 📌 Project Purpose
This project aims to analyze stock price trends for major tech companies (**Amazon, Meta, Alphabet, Microsoft, Apple**) over the period from **January 1, 2023, to December 31, 2023**. Using **Yahoo Finance API**, we extract stock data and compute key metrics such as **average closing prices, maximum closing prices, and daily returns**.

---

## 📊 Dataset Description
The dataset consists of stock price data for the selected companies, including:
- **Date**: The trading date.
- **Open**: Opening price for the stock on that date.
- **High**: The highest price reached on that date.
- **Low**: The lowest price reached on that date.
- **Close**: Closing price of the stock.
- **Adj Close**: Adjusted closing price after accounting for corporate actions.
- **Volume**: Total shares traded on that date.

---

## 🏷 Methodology
### 1️⃣ Data Collection
- Used `yfinance` to fetch historical stock data for **Amazon (AMZN), Meta (META), Alphabet (GOOG), Microsoft (MSFT), and Apple (AAPL)**.
- Set the time period from **January 1, 2023, to December 31, 2023**.
- Converted individual company data into Pandas DataFrames and merged them.

### 2️⃣ Data Analysis
- **Computed the average and maximum closing prices** for each company.
- **Calculated daily returns (%)** to track price fluctuations.
- **Identified the best and worst single-day returns** for each company during the observed period.

### 3️⃣ Data Visualization
- [Optional: Graphs showing stock trends, return distributions, etc.]

---

## 🔍 Key Findings & Insights
- **Average Closing Prices**: Gives an overall view of how the stock performed over the year.
- **Maximum Closing Prices**: Identifies the highest stock value reached during 2023.
- **Best & Worst Single-Day Returns**: Determines the most volatile trading days for each company.

---

## 🚀 Business Implications
- **Investor Decision Making**: Helps investors assess the risk and stability of each stock.
- **Trading Strategy Insights**: Understanding peak and low return days can improve investment strategies.
- **Market Trend Analysis**: Highlights overall stock market movements in the tech sector.

---

## 🛠 Technologies Used
- **Python**
  - `yfinance` for stock data retrieval
  - `pandas` for data manipulation
  - `numpy` for numerical calculations
  - `matplotlib/seaborn` for data visualization

---

## 📂 Repository Files
- **`stock_analysis.py`** – Script for fetching, processing, and analyzing stock data.
- **`README.md`** – Project documentation.

