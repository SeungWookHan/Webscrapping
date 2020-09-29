# 구글 무비 동적 페이지 크롤링
# https://play.google.com/store/movies/top 여기서 할인 중인 영화만 가져오김

import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    "Accept-Language": "ko-KR,ko"
}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class": "ImZGtf mpg5gc"})
# print(len(movies))

# with open("movies.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify())  # html 문서를 예쁘게 출력
for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()
    print(title)
