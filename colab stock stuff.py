#Installing dependencies (colab needs a pip)
!pip install finvizfinance

# libraries
import pandas as pd
from IPython.display import Image
  # shocker if these still run a year from now tbh
from finvizfinance.screener.custom import Custom
from finvizfinance.quote import finvizfinance

#general settings
pd.set_option('display.max_columns', None)

def high_value_bad(cell_value,bad_threshold,good_threshold):
    bad = 'background-color: red;color:black'
    good = 'background-color: green; color:black'
    default = ''

    if type(cell_value) in [float, int]:
        if cell_value > bad_threshold:
            return bad
        if cell_value < good_threshold:
            return good
    # return default
    
   
def competition (input_ticker):
  #query the input ticker
  stock = finvizfinance(input_ticker)

  #query the input ticker fundamentals
  stock_fundament = stock.TickerFundament(raw=True)

  #initiate the screener function
  foverview = Custom()

  #filters screener against input ticker 'Sector' and 'Industry'
  filters_dict = {'Sector':stock_fundament['Sector'],'Industry':stock_fundament['Industry']}
  foverview.set_filter(filters_dict=filters_dict)

  #create overview screener, sorted by Market Cap, with select columns
  #df = foverview.ScreenerView(order='Market Cap.', ascend=False, columns=[0,1,2,5,6,7,8,9,17,19,27,34,39,42,55,68])
  
  #create overview screener, sorted by Market Cap, with all possible columns
  df = foverview.ScreenerView(order='Market Cap.', ascend=False, columns=[0,1,6,7,8,9,16,17,19,27,38,41,53,65,2])
  
  #set index to 'Ticker'
  df = df.set_index(['Ticker'])

  #insert new column into df, specifically "Price - SMA50"
  df.insert(0,"Price-SMA50", df['Price']-df['SMA50'], True)
  #insert new column into df, specifically "Fwd PE / PE"
  df.insert(1, "(Fwd P/E)/(P/E)", df['Fwd P/E']/df['P/E'], True)

  #output chart
  stock.TickerCharts()
  display(Image(filename=str(input_ticker)+'.jpg'))

  #replace null values and round results
  df.fillna(0, inplace=True)

  #output input_ticker specific data
  print("\n")
  display(df.loc[[input_ticker]])

  #formatting properties
  format_pct = '{:,.2%}'
  format_dol0 = '${:20,.0f}'
  format_dol2 = '${:20,.2f}'
  default = ''
  style_zero = 'background-color: darkorange;'
#  style_good =
#  style_bad = 

  #output top 10 results
  print("\n")
  display(
      df.head(10).style.format(
          formatter = {
              "(Fwd P/E)/(P/E)":format_pct,
              "Market Cap":format_dol0,
              "EPS":format_dol2,
              "EPS this Y":format_pct,
              "EPS past 5Y":format_pct,
              "PEG":format_pct,
              "Insider Trans":format_pct,
              "Debt/Eq":format_pct,
              "Profit M":format_pct,
              "SMA50":format_pct,
              "Price":format_dol2,
            }
      )
      .bar(subset=["Market Cap"], color = 'red')\
      .hide_columns(["Company","Price-SMA50"])\
      #.applymap(bad_value(40,20),subset=["P/E"])   
  )
  
  
  # try any ticker you'd like
  competition("MSFT")
  
  # ticker formatting still super ugly
  # mcap charts definitely not to scale
