# # 구글 무비 동적 페이지 크롤링
# # https://play.google.com/store/movies/top 여기서 할인 중인 영화만 가져오김
# 구글 창이 안뜨게 실행 가능하게 headless로 구현


# url = "https://play.google.com/store/movies/top"

from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2560x1600")

browser = webdriver.Chrome(
    "/Users/Han/programming/webscrapping/webscrapping_basic/chromedriver", options=options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

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

# 백에서 잘 돌아가나 확인을 위한 스크린샷
browser.get_screenshot_as_file("google_movie.png")


soup = BeautifulSoup(browser.page_source, "lxml")

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
