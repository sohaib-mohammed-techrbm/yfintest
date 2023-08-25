import yfinance as yf
import pandas as pd

# List of company tickers
company_tickers = ["AAPL","AMZN","GOOG","MSFT","TSLA","JPM","UNH","V","MA","PG","WMT","DIS",
                   "INTC","VZ","BAC","KO","JNJ","XOM","UNP","COST","HD","CSCO","ORCL","SBUX","TGT",
                   "PYPL","CMCSA","IBM","ADP","GS","MMM","LMT","ABBV","NFLX","NVDA","WFC","VZ",
                   "T","GE","TMO","LOW","PEP","CRM","TXN","CVX","MRK","WDAY","FIS","QCOM","DHR","ADP",
                   "RTN","UNH","UNP","VZ","AMTD","SLB","MO","CHTR","MDLZ","LLY"]

"""ticker_to_company = { "AAPL": "Apple Inc.",
  "AMZN": "Amazon.com, Inc.",
  "GOOG": "Alphabet Inc.",
  "MSFT": "Microsoft Corporation",
  "TSLA": "Tesla, Inc.",
  "JPM": "JPMorgan Chase & Co.",
  "UNH": "UnitedHealth Group Inc.",
  "V": "Visa Inc.",
  "MA": "Mastercard Incorporated",
  "PG": "Procter & Gamble Company",
  "WMT": "Walmart Inc.",
  "DIS": "The Walt Disney Company",
  "INTC": "Intel Corporation",
  "VZ": "Verizon Communications Inc.",
  "BAC": "Bank of America Corporation",
  "KO": "The Coca-Cola Company",
  "JNJ": "Johnson & Johnson",
  "XOM": "ExxonMobil Corporation",
  "UNP": "Union Pacific Corporation",
  "COST": "Costco Wholesale Corporation",
  "HD": "The Home Depot, Inc.",
  "CSCO": "Cisco Systems, Inc.",
  "ORCL": "Oracle Corporation",
  "SBUX": "Starbucks Corporation",
  "TGT": "Target Corporation",
  "PYPL": "PayPal Holdings, Inc.",
  "CMCSA": "Comcast Corporation",
  "IBM": "International Business Machines Corporation",
  "ADP": "Automatic Data Processing, Inc.",
  "GS": "The Goldman Sachs Group, Inc.",
  "MMM": "3M Company",
  "LMT": "Lockheed Martin Corporation",
  "ABBV": "AbbVie Inc.",
  "NFLX": "Netflix, Inc.",
  "NVDA": "NVIDIA Corporation",
  "WFC": "Wells Fargo & Company",
  "VZ": "Verizon Communications Inc.",
  "T": "AT&T Inc.",
  "GE": "General Electric Company",
  "TMO": "Thermo Fisher Scientific Inc.",
  "LOW": "Lowe's Companies, Inc.",
  "PEP": "PepsiCo, Inc.",
  "CRM": "Salesforce, Inc.",
  "TXN": "Texas Instruments Incorporated",
  "CVX": "Chevron Corporation",
  "MRK": "Merck & Co., Inc.",
  "WDAY": "Workday, Inc.",
  "FIS": "Fiserv, Inc.",
  "QCOM": "QUALCOMM Incorporated",
  "DHR": "Danaher Corporation",
  "ADP": "Automatic Data Processing, Inc.",
  "RTN": "Raytheon Technologies Corporation",
  "UNH": "UnitedHealth Group Inc.",
  "UNP": "Union Pacific Corporation",
  "VZ": "Verizon Communications Inc.",
  "AMTD": "American Express Company",
  "SLB": "Schlumberger Limited",
  "MO": "Altria Group, Inc.",
  "CHTR": "Charter Communications, Inc.",
  "MDLZ": "Mondelez International, Inc.",
  "LLY": "Eli Lilly and Company"
}"""
# Create an empty DataFrame to store the data
all_data = pd.DataFrame()

# Loop through the tickers and fetch data
for ticker in company_tickers:
    company = yf.Ticker(ticker)
    data = company.history(period="5y")  # Fetch 1 year of historical data
    data['Ticker'] = ticker  # Add a column for the ticker symbol
    all_data = pd.concat([all_data, data])

# Save the data to a CSV file
csv_filename = "finance_data.csv"
all_data.to_csv(csv_filename, index=True)

print("Data exported to", csv_filename)
