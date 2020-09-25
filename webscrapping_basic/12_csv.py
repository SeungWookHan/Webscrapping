# 코스피 시가총액 순위 csv로 저장
import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
# newline을 통해 줄바꿈 없애줌, 엑셀에서 한글 깨지면 utf-8-sig 로
f = open(filename, "w", encoding="utf8", newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")  # 탭으로 구분되어 있는 문자열을 탭 기준으로 리스트화
# [n, 종목명, 현재가 ...]
print(type(title))
writer.writerow(title)

for page in range(1, 1+1):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class": "type_2"}).find(
        "tbody").find_all("tr")

    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:  # 의미없는 데이터 삭제
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)
