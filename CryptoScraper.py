import requests
# 1.The library 're' is used to remove extra letters and characters from within the price.
import re
import pandas as pd
from bs4 import BeautifulSoup as bs
# 2.The 'datetime' library is used to record the date and time along with the prices and in the file name.
from datetime import datetime as dt


def clean_and_convert_price(price_str_with_persian_digits):
    # 3.Check if the input format is a string, and if not, convert it to a string.
    if not isinstance(price_str_with_persian_digits, str):
        price_str_with_english_digits = str(price_str_with_english_digits)
    # 4.Convert Persian numbers to English.
    price_str_with_english_digits = price_str_with_persian_digits.translate(
        str.maketrans('۰۱۲۳۴۵۶۷۸۹', '0123456789'))

    # 5.Remove extra characters
    cleaned_str = re.sub(r'[^\d.]', '', price_str_with_english_digits)
    # 6.Handle cases where the cleaned string cannot be converted to a float.
    try:
        final_price = float(cleaned_str)
        return final_price
    except ValueError:
        print(
            f"Warning: Could not convert {price_str_with_english_digits} to float Cleaned: {cleaned_str}")
        return None


# 7.Using a header to avoid being identified as a bot.
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
# 8.Retrieve the content of the HTML page.
response = requests.get('https://arzdigital.com/coins/', headers=header
                        )
# 9.Reviewing the request and parsing the HTML page.
if response.status_code == 200:
    soup = bs(response.text, 'html.parser')
    # 10.Selecting tags containing the names and prices of currencies.
    tags = soup.select(
        '#list-price > div.arz-scroll-box > div > table > tbody > tr')
    # 11.Review the discovery of tags.
    if tags:
        coins_info = []
        # 12.Using a loop to extract the price and name of all currencies.
        for tag in tags:
            coin_name, coin_price = None, None
            # 13.Management of potential errors during data extraction.
            try:
                coin_name = tag['data-name']
                coin_price = clean_and_convert_price(
                    tag.find_all('span')[3].text)
            except Exception as e:
                print(e)
            # 14.Record the date along with the price and the names of the currencies.
            date_now = str(dt.now())
            finalـdata = {
                "name": coin_name,
                "price": coin_price,
                # 15.Create an empty column between price and date.
                "empty column": "    ",
                "date": date_now
            }
            coins_info.append(finalـdata)
        # 16.Using the date in the file name.
        now = dt.now()
        time_str = now.strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'crypto_prices_{time_str}.xlsx'
        # 17.Saving data in an Excel file.
        df = pd.DataFrame(coins_info)
        df.to_excel(file_name, index=False)
        print(df)
        print(f'{file_name}\nThe data has been saved successfully')
    else:
        print('Tags not found!')
else:
    print('Error in receiving HTML content!')
