import yfinance as yf
import pandas as pd

def fetch_stock_data(tickers, start_date, end_date):
    # Create an empty DataFrame to store the stock data
    data = pd.DataFrame()

    # Fetch the historical data for each ticker
    for ticker in tickers:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        stock_data.insert(0, "Ticker", ticker)  # Insert the "Ticker" column at the beginning
        data = pd.concat([data, stock_data])  # Concatenate the data with the main DataFrame

    # Generate a descriptive file name
    file_name = f"stock_data_{start_date}_{end_date}.xlsx"

    # Save the data as an Excel file
    data.to_excel(file_name, index=False)

    print(f"Stock data for {len(tickers)} stocks saved as {file_name}")

# Example usage:
tickers = ["AAPL", "MSFT", "AMZN", "GOOGL", "FB"]  # User-provided list of ticker symbols
start_date = "2013-05-15"
end_date = "2023-05-15"

fetch_stock_data(tickers, start_date, end_date)
