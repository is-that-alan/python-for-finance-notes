#Extracting data from web tables
import bs4 as bs
imprt datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
#serialised any python objects, save any object, in this case the wikipedia list of S&P500 list
import pickle
import requests

def save_sp500_tickers():
  resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
  soup = bs.BeautifulSoup(resp.text, "lxml")
  table = soup.find('table', {'class':'wikitable sortable;})
  tickers = []
  for row in table.findAll('tr') [1:]:
     ticker = row.findAll('td') [0].text
     tickers.append(ticker)
                             
  with open("sp500tickers.pickle", "wb") as f:
  
 print(tickers)
                             
 return tickers
 
#save_sp500_tickers()

#Build on the previous function
def get_data_from_yahoo(reload_sp500=False)
  if reload_sp500:
    tickers = save_sp500_tickers()
  else:
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)
        
  if not os.path.exists('stock_dfs'):
      os.akedirs('stock_dfs')
      
  start = dt.datetime(2000,1,1)
  end = dt.datetime(2016,12,31)
  
  for ticker in tickers:
      print(ticker)
      if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
          df = web.Datareader(ticker, 'yahoo', start, end)
          df.to_csv('stock_dfs/{}.csv'.format(ticker))
      else:
          print('Already have ()'. format(ticker))
       
