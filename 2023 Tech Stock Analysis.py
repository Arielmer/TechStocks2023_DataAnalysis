
    #Part 1:
    #!pip install yfinance in terminal
import yfinance as yf
#import needed packages
import pandas as pd
import numpy as np
pd.core.common.is_list_like = pd.api.types.is_list_like
import datetime
#import matplotlib.pyplot as plt

    #Part 2: Data prep
    # Figure out how to get the stock data from Jan. 1st 2023 to Dec. 31st 2023 for each of these companies. 
    # Set each company to be a separate dataframe, with the variable name for that company being its ticker symbol. 
    # This will involve a few steps:
    # 1. Use datetime to set start and end datetime objects.
    # 2. Figure out the ticker symbol for each company.
    # 3. Figure out how to use datareader to grab info on the stock.
start = datetime.datetime(2023, 1, 1)
end = datetime.datetime(2023, 12, 31)
# Amazon
Amazon = yf.download("AMZN", start, end)
# Meta
Meta = yf.download("META", start, end)
# Alphabet
Alphabet = yf.download("GOOG", start, end)
# Microsoft
Microsoft = yf.download("MSFT", start, end)
# Apple
Apple = yf.download("AAPL", start, end)
# Resetting Indexes
Amazon.reset_index(inplace=True)
Meta.reset_index(inplace=True)
Alphabet.reset_index(inplace=True)
Microsoft.reset_index(inplace=True)
Apple.reset_index(inplace=True)
# Show data head
Amazon.head()
# Add a Column_Company Name
Amazon["Company"]='Amazon'
Meta["Company"]='Meta'
Microsoft["Company"]='Microsoft'
Apple["Company"]='Apple'
Alphabet["Company"]='Alphabet'
# Create a list containing all the individual DataFrames for each company
data_frames = [Amazon, Meta, Alphabet, Microsoft, Apple]
# Combines the DataFrames into one
all_data = pd.concat(data_frames, ignore_index=True)
#Display the first 500 rows of the all_data DataFrame
all_data.head(500)

    # Part 3: Analysis
# [Derive the average closing price for each company]
average_closing_prices = all_data.groupby('Company')['Close'].mean()
print(average_closing_prices)
# [Find out the max close price for each company's stock throughout the time period]
max_closing_prices = all_data.groupby('Company')['Close'].max()
print(max_closing_prices)
# [Create a new dataframe called returns.
#  This dataframe will contain the returns for each company's stock.]
# Create a new DataFrame that only includes 'Date', 'Company', and 'Close' columns
returns = all_data[['Date', 'Company', 'Close']].copy()
# 计算收益率并转换为百分数
returns['Returns'] = returns.groupby('Company')['Close'].apply(lambda x: (x / x.shift(1) - 1) * 100).reset_index(level=0, drop=True)
# 将 'Returns' 列转换为百分数格式
returns['Returns'] = returns['Returns'].map("{:.2f}%".format)
# 显示结果
returns.head(500)
# [Using this returns dataframe, figure out on 
#  what dates each company stock had the best and worst single day returns]
# 确保 'Returns' 列为数值格式，先去掉 NaN 值
returns['Returns'] = pd.to_numeric(returns['Returns'].astype(str).str.replace('%', ''), errors='coerce')


# 找到每个公司单日收益率最高的日期和最低的日期
best_returns = returns.loc[returns.groupby('Company')['Returns'].idxmax()]
worst_returns = returns.loc[returns.groupby('Company')['Returns'].idxmin()]

# 为清晰起见，重命名列
best_returns = best_returns.rename(columns={"Date": "Best_Return_Date", "Returns": "Best_Return_Percentage"})
worst_returns = worst_returns.rename(columns={"Date": "Worst_Return_Date", "Returns": "Worst_Return_Percentage"})

# 合并最佳和最差收益率
extreme_returns = pd.merge(
    best_returns[['Company', 'Best_Return_Date', 'Best_Return_Percentage']],
    worst_returns[['Company', 'Worst_Return_Date', 'Worst_Return_Percentage']],
    on='Company'
)

# 将百分比格式化为显示
extreme_returns['Best_Return_Percentage'] = extreme_returns['Best_Return_Percentage'].map("{:.2f}%".format)
extreme_returns['Worst_Return_Percentage'] = extreme_returns['Worst_Return_Percentage'].map("{:.2f}%".format)

# 显示结果
print(extreme_returns)
