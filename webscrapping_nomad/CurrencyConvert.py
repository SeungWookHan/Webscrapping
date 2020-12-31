import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")
url = "https://www.iban.com/currency-codes"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
countries = {}
max_key = 0
print("Welcome to CurrencyConvert Pro 2000")
table = soup.find("tbody")

trs = table.find_all("tr")

for num, tr in enumerate(trs):
  indiviual_tr = tr.find_all("td")
  country = indiviual_tr[0].get_text()
  code = indiviual_tr[2].get_text()
  countries[num] = (country, code)

print()
for key, value in countries.items():
  print("#{0} {1}".format(key, value[0]))
  max_key = key

while(True):
  try:
    print("\nWhere are you from? Choose a country by number.\n")
    input_value = int(input("#: "))
    if input_value < 0 or input_value > max_key:
      print("Choose a number from the list.")
    else:
      print(countries[input_value][0].title(), "\n")
      from_currency = countries[input_value][1]
      break
  except:
    print("That wasn't a number.")

first_select = input_value
while(True):
  try:
    print("\nNow choose another country.\n")
    input_value = int(input("#: "))
    if input_value < 0 or input_value > max_key:
      print("Choose a number from the list.")
    elif input_value == first_select:
      print("Same Country. Choose anothe country.")
    else:
      print(countries[input_value][0].title(), "\n")
      to_currency = countries[input_value][1]
      break
  except:
    print("That wasn't a number.")

print("\nHow many {} do you want to convert to {}?".format(from_currency, to_currency))
while(True):
  try:
    from_currency_result = float(input())
    break
  except:
    print("That wasn't a number.")

url = "https://transferwise.com/gb/currency-converter/{0}-to-{1}-rate?amount={2}".format(from_currency, to_currency, from_currency_result)


res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
currency_rate = float(soup.find("span", attrs={"class":"text-success"}).get_text())

to_currency_result = from_currency_result * currency_rate

from_currency_result = format(from_currency_result, ",.2f")
to_currency_result = format_currency(to_currency_result, "KRW", locale="ko_KR")

print("{0}{1} is {2}".format(from_currency, from_currency_result, to_currency_result))
