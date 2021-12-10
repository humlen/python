# Import Libraries
import matplotlib.pyplot as plt # Using plt over seaborn due to wide data pref
import numpy as np
import pandas as pd

# Stock Info
current_price = 50.59 # Current price of the security
strike = 55 # Strike price of the option 
premium = 0.47 # Premium issued at the sale of an option at the strike
stock_range_min = 45 # Lowest stock value to model for 
stock_range_max = 60 # Highest stock value to model for 
step = 0.1 # Steps in the calculation

custom_range = np.arange(stock_range_min,stock_range_max,step)


# Return Calculator
buy_hold = []
short_call = []
for i in custom_range:
    buy_and_hold = 100*(i-50.59)
    buy_hold.append(buy_and_hold)
    if i <= strike:
        sc = 100*(premium+i-50.59)
    if i > strike:
        sc = 100*(premium+strike-50.59)
    short_call.append(sc)

# Create Dataframe
tuplelist = list(zip(custom_range,buy_hold,short_call))
df = pd.DataFrame(tuplelist, columns = ['Stock Price', 'Buy & Hold','Short Covered Calls']) # Not sure of a quicker way to turn lists into a df

# Return Chart
plt.plot(df['Stock Price'], df['Buy & Hold'], label = "Buy & Hold")
plt.plot(df['Stock Price'], df['Short Covered Calls'], label = "Short Covered Calls")
plt.axhline(0, color='black', linestyle=':') # Line for the 0-return indicator
plt.axvline(current_price, color = 'black', linestyle = ':') # Line for the current price indicator
plt.title('Option Return Chart')
plt.xlabel('Stock Price')
plt.ylabel('Absolute Return')
plt.legend()
plt.yscale('linear') # Can turn to symlog, but hurts readability for others
plt.show()
