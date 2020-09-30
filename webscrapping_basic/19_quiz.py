# quiz. 부동상 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오

# 조회 조건
# 1. http://daum.net 접속
# 2. '송파 헬리오시티' 검색
# 3. 다음 부동산 부분에 나오는 결좌 정보

# [출력 결과]
# ========== 매물1 ==========
# 거래: 매매
# 면적: 84/59 (공급/전용)
# 가격: 165,000 (만원)
# 동: 214동
# 층: 고/23
# ========== 매물2 ==========
# ...

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome(
    "/Users/Han/programming/webscrapping/webscrapping_basic/chromedriver")

url = "http://daum.net"
browser.get(url)

elem = browser.find_element_by_id("q")
elem.send_keys("송파 헬리오시티")
elem.submit()

soup = BeautifulSoup(browser.page_source, "lxml")

# with open("quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

data_rows = soup.find("table", attrs={"class": "tbl"}).find(
    "tbody").find_all("tr")

for idx, row in enumerate(data_rows):
    columns = row.find_all("td")

    print("========== 매물 {} ==========".format(idx+1))
    print("거래: ", columns[0].get_text().strip())
    print("면적: ", columns[1].get_text().strip(), "(공급/전용)")
    print("가격: ", columns[2].get_text().strip(), "(만원)")
    print("동: ", columns[3].get_text().strip())
    print("층: ", columns[4].get_text().strip())
# 거래: 매매
# 면적: 84/59 (공급/전용)
# 가격: 165,000 (만원)
# 동: 214동
# 층: 고/23
