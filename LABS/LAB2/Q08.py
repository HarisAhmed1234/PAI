def currency_converter():
    # 1 USD= inside money rates
    money_rates = {
        'USD': 1.0, 
        'EUR': 0.85, 
        'PKR': 278.58, 
        'INR': 82.72,  
        'JPY': 146.17  
    }

    print(
        "Currencies: USD (Dollar), EUR (Euro), PKR (Pakistani Rupee), INR (Indian Rupee), JPY (Japanese Yen)")

    convert_currency = input("Enter the currency you want to convert from (USD, EUR, PKR, INR, JPY): ").upper()
    if convert_currency not in money_rates:
        print("Invalid currency!")
        return

    amount = float(input(f"Enter the amount in {convert_currency}: "))

    to_currency = input("Enter the currency you want to convert to (USD, EUR, PKR, INR, JPY): ").upper()
    if to_currency not in money_rates:
        print("Invalid currency!")
        return
      
    converted_amount = amount * money_rates[to_currency] / money_rates[convert_currency]
    print(f"{amount} {convert_currency} is equal to {converted_amount:.2f} {to_currency}")#.2F for decimal place

currency_converter()
