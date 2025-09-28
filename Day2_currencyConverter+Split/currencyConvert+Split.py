import requests

def currencyConvert(split_bill):
    initial_code = "USD"
    target_code = input("Enter the Target currency code (like INR, JPY, EUR...): ").strip().upper()
    url = f"https://api.exchangerate-api.com/v4/latest/{initial_code}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Something went wrong while fetching exchange rates.")
        return

    data = response.json()
    
    # Check if currency code is valid
    if target_code not in data["rates"]:
        print("Invalid currency code. Try again!")
        return
    rate = data["rates"][target_code]
    print(f"💱 Current exchange rate: 1 USD = {rate} {target_code}")
    rate = data["rates"][target_code]
    converted_amount = split_bill * rate
    print(f"\nThe Bill after splitting and converting into {target_code} is: {round(converted_amount, 2)}\n")
          
def before_change():
    while True:
        try:
            bill = float(input("Enter the amount you want to split in USD: "))
        except:
            print("Enter the bill as a numeric value please.")
            continue
        if bill <= 0:
            print("Enter an amount greater than 0 to convert.")
            continue
        else:
            break
    tip = int(input("Enter the tip percentage you want to give: "))
    split = int(input("Enter the number of people you are splitting the bill amongst: "))
    tipped_bill = bill + (bill * tip / 100)
    split_bill = tipped_bill / split
    currencyConvert(split_bill)

def main():
    print("💰 Welcome to Currency Converter and Splitter 💰")
    while True:
        before_change()
        again = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for using the Currency Converter and Splitter😁👌")
            break

if __name__ == "__main__":
    main()