from forex_python.converter import CurrencyRates
C = CurrencyRates()
Amount = int(input("Enter Your amount :"))
from_currency = input("From Currency:".upper())
to_currency = input("To Currency:".upper())
print(from_currency,"TO",to_currency,Amount)
result = C.convert(from_currency,to_currency,Amount)
print(result)