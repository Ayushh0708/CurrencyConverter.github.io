def convert_currency(amount, from_currency, to_currency):
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'INR': 75.0,
        'GBP': 0.75
    }
    
    if from_currency == 'USD':
        converted = amount * exchange_rates[to_currency]
    else:
        converted = (amount / exchange_rates[from_currency]) * exchange_rates[to_currency]
    
    return round(converted, 2)

def main():
    print("Currency Converter")
    
    amount = float(input("Enter amount to convert: "))
    from_currency = input("From Currency (USD, EUR, INR, GBP): ").upper()
    to_currency = input("To Currency (USD, EUR, INR, GBP): ").upper()
    
    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")

if __name__ == "__main__":
    main()
