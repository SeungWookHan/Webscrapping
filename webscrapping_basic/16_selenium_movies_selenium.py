# # 구글 무비 동적 페이지 크롤링
# # https://play.google.com/store/movies/top 여기서 할인 중인 영화만 가져오김


# url = "https://play.google.com/store/movies/top"

from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver

browser = webdriver.Chrome(
    "/Users/Han/programming/webscrapping/webscrapping_basic/chromedriver")
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 스크롤 내리기(자바스크립트를 통해 최하단 1600 으로 스크롤 내리기?)
# # browser.execute_script("window.scrollTo(0, 1600)")  # 2560 X 1600
# browser.execute_script("window.scrollTo(0, 2080)")

interval = 2  # 2초에 한번씩 스크롤을 내리기 위함

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    browser.execute_script(
        "window.scrollTo(0, document.body.scrollHeight)")  # 끝까지!
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    current_height = browser.execute_script(
        "return document.body.scrollHeight")
    if current_height == prev_height:
        break

    prev_height = current_height

print("스크롤 완료")


# url = "https://play.google.com/store/movies/top"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
#     "Accept-Language": "ko-KR,ko"
# }

soup = BeautifulSoup(browser.page_source, "lxml")

# 클래스가 리스트 안에 있던 것과 일치하게
# movies = soup.find_all("div", attrs={"class": ["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
print(len(movies))

# with open("movies.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify())  # html 문서를 예쁘게 출력
for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격 정보
    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print("<할인되지 않은 영화 제외>")
        continue

    # 할인된 가격
    price = movie.find(
        "span", attrs={"class": "VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class": "JC71ub"})["href"]
    # https://play.google.com + link

    print(f"제목: {title}")
    print(f"할인 전 금액: {original_price}")
    print(f"할인 후 금액: {price}")
    print("링크: ", 'https://play.google.com' + link)
    print("-" * 120)

browser.quit()
