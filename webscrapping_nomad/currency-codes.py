import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
countries = {}
max_key = 0

table = soup.find("tbody")

trs = table.find_all("tr")

for num, tr in enumerate(trs):
  indiviual_tr = tr.find_all("td")
  country = indiviual_tr[0].get_text()
  code = indiviual_tr[2].get_text()
  countries[num] = (country, code)

print("Hello! Please choose select a country by number:")
for key, value in countries.items():
  print("#", key, value[0])
  max_key = key

while(True):
  try:
    input_value = int(input("#: "))
    if type(input_value) == int:
      if input_value < 0 or input_value > max_key:
        print("Choose a number from the list.")
      else:
        print("You chose", countries[input_value][0].title())
        print("The currency code is", countries[input_value][1])
        break
  except:
    print("That wasn't a number.")