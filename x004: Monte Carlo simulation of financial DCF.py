# Install Libraries
!pip install yfinance

# Import Libraries
import pandas as pd
import numpy as np
import yfinance as yf
import seaborn as sns

sns.set_style('whitegrid')


# Check for Normal Distribution of the YoY Revenue Growth Rate
revenue_growth_rate_yoy = 0.2
revenue_growth_rate_yoy_normdist = np.random.normal(loc=revenue_growth_rate_yoy, scale = 0.02, size = 10000)
fig, ax = plt.subplots(figsize=(15,5))
plt.title("Normal Distribution for the YoY Revenue Growth Rate")
axl = sns.histplot(revenue_growth_rate_yoy_normdist, label = 'normdist', ax = ax)
plt.legend()
plt.show()


stock = "MSFT"
ticker = yf.Ticker(stock)

# basic math
M = 1000000 # Designate 1 Million
B = 1000000000 # Designate 1 Billion
simulations = 10000

# data scrape
info = ticker.info
cashflow = ticker.cashflow
balance_sheet = ticker.balance_sheet
earnings = ticker.earnings


# Project revenue for the future periods
revenue = earnings['Revenue']/M
revenue_m = revenue.tolist()

rev_growth_3y_cagr = (revenue_m[3]/revenue_m[0])**(1/3)*100-100
print("The 4-year revenue growth of ",stock," is ",round(rev_growth_4y_cagr,2),"%")

rev_growth_ly_cagr = (revenue_m[3]/revenue_m[2])*100-100
print("The last-year revenue growth of ",stock," is ",round(rev_growth_ly_cagr,2),"%")


# 5 Year revenue growth rate (simmed)
revgrowth_mean = 0.08
revgrowth_std = 0.03

revenue_growth = np.random.normal(loc=revgrowth_mean, scale = revgrowth_std, size = simulations)
fig, ax = plt.subplots(figsize=(15,5))
plt.title("Normal Distribution for the YoY Revenue Growth Rate")
axl = sns.histplot(revenue_growth, label = 'Normal Distribution of YoY Revenue Growth Rate', ax = ax)
plt.legend()
plt.show()

for p in range(simulations): #run the simulation 10000 times
    #creating projections for a 5 year dcf model
    Fiveyrev = []
    startrev = revenue_m[3]
    for i in range(5):
        startrev = startrev*(1+np.random.normal(loc=revgrowth_mean, scale=revgrowth_std))
        Fiveyrev.append(startrev)

print(Fiveyrev)
