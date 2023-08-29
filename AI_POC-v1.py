import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
from AI_POC_DATA import tickers, compare_list, high_revenue, low_revenue

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
    for symbol1 in stock_symbols:
        print("Details of ",symbol1)
        stock_data = yf.download(symbol1, start=start_date, end=end_date)
        sd = pd.DataFrame(stock_data)
        print(sd)
        

def show_high_revenue(stock_symbols, start_date, end_date):
    for symbol2 in stock_symbols:
        stock_data = yf.download(symbol2, start=start_date, end=end_date)
        high_list = stock_data['High']
        print(f'Highest Revenue of {symbol2} is {max(high_list)}')

def show_low_revenue(stock_symbols, start_date, end_date):
    for symbol3 in stock_symbols:
        stock_data = yf.download(symbol3, start=start_date, end=end_date)
        low_list = stock_data['Low']
        print(f'Lowest Revenue of {symbol3} is {min(low_list)}')
        

#userinputs
stock_symbols_input = input("Enter your question : ")
start_date = '2022-01-01'  #input("Enter start date (YYYY-MM-DD): ")
end_date = '2023-01-01'    #input("Enter end date (YYYY-MM-DD): ")

def final_result(stock_symbols_input_data,start_date_data,end_date_data):
    stock_symbols = []
    found = False
    

    stock_symbols_input_data = stock_symbols_input_data.strip()
    tokens = TextBlob(stock_symbols_input_data).words

    for token in tokens:
        if token in tickers:
            stock_symbols.append(token)
        else:
            print("Processing........")
    
    for comp in compare_list:
        if comp in stock_symbols_input_data:
            grap = plot_stock_volume(stock_symbols, start_date_data, end_date_data)
            found=True
            return grap
    
    for high in high_revenue:
        if high in stock_symbols_input_data:
            hi_re = show_high_revenue(stock_symbols, start_date_data, end_date_data)
            found=True
            return hi_re
        
    for low in low_revenue:
        if low in stock_symbols_input_data:
            lo_re = show_low_revenue(stock_symbols, start_date_data, end_date_data)
            found=True
            return lo_re

        
    if(found == False):
        detail = show_details(stock_symbols, start_date_data, end_date_data)
        return detail
        

final_result(stock_symbols_input,start_date,end_date)

