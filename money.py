import requests

API_KEY = "4e269a7c81006027cdbf1ac8"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}"

def get_supported_currencies():
    url = f"{BASE_URL}/codes"
    try:
        print("(Fetching supported currency codes...)\n")
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("result") == "success":
            currency_dict = dict(data["supported_codes"])
            print("🌐 Popular Currency Codes:")
            for code in ["USD", "INR", "EUR", "GBP", "JPY", "AUD", "CAD"]:
                print(f"{code} - {currency_dict.get(code, 'Not found')}")

            show_all = input("\nShow full currency list? (y/n): ").strip().lower()
            if show_all == 'y':
                for code, name in data["supported_codes"]:
                    print(f"{code} - {name}")
        else:
            print("❌ API Error while fetching currency codes.")
    except Exception as e:
        print(f"\n❌ Failed to fetch currencies: {str(e)}")

def convert_currency(amount, from_currency, to_currency):
    url = f"{BASE_URL}/pair/{from_currency.upper()}/{to_currency.upper()}/{amount}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if data.get("result") == "success":
            converted = data["conversion_result"]
            print(f"\n✅ {amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
        else:
            print(f"\n❌ API Error: {data.get('error-type', 'Unknown error')}")
    except Exception as e:
        print("\n❌ Network error:", str(e))

def main():
    print("🌍 Currency Converter for All Nations")
    print("------------------------------------")
    get_supported_currencies()

    try:
        amount = float(input("\nEnter amount to convert: "))
        from_currency = input("Convert from (Currency Code): ").strip()
        to_currency = input("Convert to (Currency Code): ").strip()
        convert_currency(amount, from_currency, to_currency)
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()



