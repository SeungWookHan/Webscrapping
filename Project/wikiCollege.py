# 서울/경기권 대학교 목록을 쉽게 발췌하기 위한 크롤링
# 목적: 서울/경기권 대학교(전문대 포함)의 비대면 수업 여부, 기한을 정리하고자 함
from bs4 import BeautifulSoup
from pprint import pprint
import requests
import re

# https://ko.wikipedia.org/wiki/%EA%B2%BD%EA%B8%B0%EB%8F%84%EC%9D%98_%EB%8C%80%ED%95%99_%EB%AA%A9%EB%A1%9D - 경기권
# https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%EC%9D%98_%EB%8C%80%ED%95%99_%EB%AA%A9%EB%A1%9D - 서울 특별시

url = "https://ko.wikipedia.org/wiki/%EA%B2%BD%EA%B8%B0%EB%8F%84%EC%9D%98_%EB%8C%80%ED%95%99_%EB%AA%A9%EB%A1%9D"
html = requests.get(url)

# pprint(html.text)
soup = BeautifulSoup(html.text, 'html.parser')

# for data1 in soup.find_all('table', {'class':'wikitable sortable'}):
#   print(data1)

data2 = []
for data1 in soup.find_all('a'):
    if 'title' in data1.attrs:
        data2.append(data1.attrs['title'])


matching = [s for s in data2 if "대학교" in s]


# result = []
# for i, name in enumerate(matching):
#   result.append((i, name))

pprint(matching)
