💰 Tip Calculator + Currency Splitter

This project takes a total bill in USD, adds a tip, splits it among friends, and then converts the final per-person amount into a currency of your choice using a live exchange rate API.

🚀 Features

-Takes user input for bill, tip %, and split count

-Converts the final amount into any target currency (like INR, EUR, JPY...)

-Displays the current exchange rate

-Handles invalid inputs gracefully

-Lets users calculate multiple times in one run

🧠 Concepts Used

-Loops (while) and conditionals (if)

-Type casting and input validation

-Functions for modular structure

-API integration with requests

-JSON parsing

📦 API Used

-ExchangeRate API: 
for fetching real-time currency rates.

🧑‍💻 How to Run

Install dependencies:

pip install requests


Run the script:

python tip_currency_splitter.py

✨ Example Output
💰 Welcome to Currency Converter and Splitter 💰
Enter the amount you want to split in USD: 100
Enter the tip percentage you want to give: 10
Enter the number of people you are splitting the bill amongst: 2
Enter the Target currency code (like INR, JPY, EUR...): INR
💱 Current exchange rate: 1 USD = 83.24 INR
The Bill after splitting and converting into INR is: 4583.2
