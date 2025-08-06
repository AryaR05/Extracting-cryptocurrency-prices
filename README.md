# Crypto Price Scraper

This is a Python script designed to scrape real time cryptocurrency prices from "ArzDigital.com"
(https://arzdigital.com/) and save them into an Excel file.

## Features:
- Fetches current prices of various cryptocurrencies.
- Converts Persian digits to English digits for accurate processing.
- Cleans numerical price strings by removing non-numeric characters (Like a comma, "تومان").
- Robust error handling to prevent script crashes due to missing data or invalid price formats.
- Saves extracted data (Coin Name, Price, Date) into a well-formatted Excel (.xlsx) file.
- Generates unique filenames based on the current timestamp.

## Requirements:
Make sure you have the following Python libraries installed:
"requests"
"BeautifulSoup4" (aliased as "bs")
"pandas" (aliased as "pd")
You can install them using pip:
pip install requests
pip install beautifulsoup4
pip install pandas