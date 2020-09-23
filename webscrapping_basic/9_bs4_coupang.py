import requests
import re
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# print(res.text)

items = soup.find_all("li", attrs={"class": re.compile(
    "^search-product")})  # 공백 열어두면 안됨 search-product
# print(items[1])
# print(items[0].find("div", attrs={"class": "name"}).get_text())


for item in items:

    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
    if ad_badge:
        print("<광고 상품 제외합니다.>")
        continue

    name = item.find("div", attrs={"class": "name"}).get_text()  # 제품명
    # 애플 제품 제외
    if "Apple" in name:
        print("<애플 상품 제외합니다.>")
        continue

    price = item.find(
        "strong", attrs={"class": "price-value"}).get_text()  # 가격

    # 리뷰 100개 이상, 평점 수 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class": "rating"})  # 평점
    if rate:
        rate = rate.get_text()
    else:
        print("<평점 없는 상품 제외합니다.>")
        continue

    rate_count = item.find(
        "span", attrs={"class": "rating-total-count"})  # 평점 수
    if rate_count:
        rate_count = rate_count.get_text()  # 예 (26) 즉 괄호가 덮혀있음
        rate_count = rate_count[1:-1]
        print("리뷰 수: ", rate_count)
    else:
        print("<평점 수 없는 상품 제외합니다.>")
        continue

    if float(rate) >= 4.5 and int(rate_count) >= 100:
        print(name, price, rate, rate_count)
