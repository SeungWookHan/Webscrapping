# 서울/경기권 대학교 목록을 쉽게 발췌하기 위한 크롤링
# 목적: 서울/경기권 대학교(전문대 포함)의 비대면 수업 여부, 기한을 정리하고자 함
# 해당 데이터를 csv 파일로 출력 하고자함
from bs4 import BeautifulSoup
from pprint import pprint
import requests
import re
import csv

# https://ko.wikipedia.org/wiki/%EA%B2%BD%EA%B8%B0%EB%8F%84%EC%9D%98_%EB%8C%80%ED%95%99_%EB%AA%A9%EB%A1%9D - 경기권
# https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%EC%9D%98_%EB%8C%80%ED%95%99_%EB%AA%A9%EB%A1%9D - 서울 특별시
# https://ko.wikipedia.org/wiki/%EC%9D%B8%EC%B2%9C%EA%B4%91%EC%97%AD%EC%8B%9C%EC%9D%98_%EB%8C%80%ED%95%99_%EB%AA%A9%EB%A1%9D - 인천
kyongki = "https://ko.wikipedia.org/wiki/%EA%B2%BD%EA%B8%B0%EB%8F%84%EC%9D%98_%EB%8C%80%ED%95%99_%EB%AA%A9%EB%A1%9D"
seoul = "https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%EC%9D%98_%EB%8C%80%ED%95%99_%EB%AA%A9%EB%A1%9D"
incheon = "https://ko.wikipedia.org/wiki/%EC%9D%B8%EC%B2%9C%EA%B4%91%EC%97%AD%EC%8B%9C%EC%9D%98_%EB%8C%80%ED%95%99_%EB%AA%A9%EB%A1%9D"

urls = [kyongki, seoul, incheon]
list = []
total_list = []
for url in urls:
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    colleges = soup.find_all("td")

    # print(colleges)
    for college in colleges:
        name = college.find("a") or college.find("span")
        if name is not None and "대학교" in name.get_text() and "대학원" not in name.get_text() and "사이버" not in name.get_text():
            name = name.get_text()
            list.append(name)

    list.sort()
    for i in range(0, len(list)-1):
        for j in range(i+1, len(list)):
            if list[i] in list[j]:
                list[i] = "del"
            else:
                break
    total_list += [[x] for x in list if x is not "del"]
    list = []


total_list.sort()
# print(total_list)
# for li in total_list:
#     print(li)


filename = "서울경기인천대학.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

writer.writerow(["대학교명"])

for row in total_list:
    writer.writerow(row)


# for li in list:
#     print(li)

# soup = BeautifulSoup(html.text, 'html.parser')

# # for data1 in soup.find_all('table', {'class':'wikitable sortable'}):
# #   print(data1)

# data2 = []
# for data1 in soup.find_all('a'):
#     if 'title' in data1.attrs:
#         data2.append(data1.attrs['title'])

# matching = [s for s in data2 if "대학교" in s]

# # result = []
# # for i, name in enumerate(matching):
# #   result.append((i, name))

# pprint(matching)
