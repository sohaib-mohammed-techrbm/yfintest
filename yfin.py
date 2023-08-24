#Test Api
import yfinance as yf
import matplotlib.pyplot as plt
from textblob import TextBlob
from typing import Union
from fastapi import FastAPI
# import nltk
# nltk.download('punkt')
#ML-----------------------------------------------------------------------------------------------------------------
tickers = ['DKS', 'M','ZM','LOW','SOS','TSLA','MRNA','MDT','NVDA','NVAX','FULC','NKE','BJ','MSFT','AXLA','ATVI','NVOS','S','COTY','PMN','FN','FL','ASO','CSIQ','GMVD','FRGT','APP','ASML','UBI.PA','AMC', 'AMZN',"GOOG",'AAPL'
           'dks','m','zm','low','sos','tsla','mrna','mdt','nvda','nvax','fulc','nke','bj','msft','axla','atvi','nvos','s','coty','pmn','fn','fl','aso','csiq','gmvd','frgt','app','asml','ubi.pa','amc','amzn','goog','aapl']

compare_list = ['compare','Compare','comparison','Comparison','cmp','Cmp','compair','Compair']
#Functions-----------------------------------------------------------------------------------------------------------
def plot_stock_volume(stock_symbols, start_date, end_date):
    plt.figure(figsize=(10, 6))
    
    for symbol in stock_symbols:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        plt.plot(stock_data['High'], label=symbol)

    plt.title("Stock Volume Comparison")
    plt.xlabel("Date")
    plt.ylabel("High")
    plt.legend()
    plt.grid(True)
    plt.show()

def show_details(stock_symbols, start_date, end_date):
    for symbol in stock_symbols:
        print("Details of ",symbol)
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        print(stock_data)
        return stock_data

#userinputs--------------------------------------------------------------------------------------------------------
# stock_symbols_input = input("Enter your question : ")
# start_date = input("Enter start date (YYYY-MM-DD): ")
# end_date = input("Enter end date (YYYY-MM-DD): ")

#@apicall------------------------------------------------------------------------------------------------------------
app = FastAPI()

@app.get("/fin/")
async def final_result(stock_symbols_input: str, start_date: Union[str,int]="2020-02-02", end_date: Union[str,int]="2021-02-02"):
    stock_symbols = []
    found = False

    stock_symbols_input = stock_symbols_input.strip()
    tokens = TextBlob(stock_symbols_input).words

    for token in tokens:
        if token in tickers:
            stock_symbols.append(token)
        else:
            print("Processing........")
    
    for comp in compare_list:
        if comp in stock_symbols_input:
            grap = plot_stock_volume(stock_symbols, start_date, end_date)
            found=True
            return grap
        
    if(found == False):
        detail = show_details(stock_symbols, start_date, end_date)
        return detail
        

#final_result(stock_symbols_input,start_date,end_date)

