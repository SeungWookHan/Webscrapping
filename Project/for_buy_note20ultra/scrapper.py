import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

BASE_URL_G = "https://browse.gmarket.co.kr/search?keyword=노트20울트라+자급제"
# BASE_URL_11 = "http://search.11st.co.kr/Search.tmall?kwd=노트20울트라 자급제"
BASE_URL_A = "http://browse.auction.co.kr/search?keyword=노트20울트라+자급제"
# BASE_URL_C = "https://www.coupang.com/np/search?component=&q=노트20울트라+자급제&channel=user"
# BASE_URL_T = "https://search.tmon.co.kr/search/?keyword=%EB%85%B8%ED%8A%B820%EC%9A%B8%ED%8A%B8%EB%9D%BC%20%EC%9E%90%EA%B8%89%EC%A0%9C"
# BASE_URL_W = "https://search.wemakeprice.com/search?search_cate=top&keyword=%EB%85%B8%ED%8A%B820%EC%9A%B8%ED%8A%B8%EB%9D%BC%20%EC%9E%90%EA%B8%89%EC%A0%9C&isRec=1&_service=5&_type=3"
BASE_URL_I = "http://shopping.interpark.com/shopSearch.do?q=%EB%85%B8%ED%8A%B820%EC%9A%B8%ED%8A%B8%EB%9D%BC%20%EC%9E%90%EA%B8%89%EC%A0%9C"

def get_G():
  contents_g = []
  url = BASE_URL_G
  res = requests.get(url, headers=headers)
  soup = BeautifulSoup(res.text, "html.parser")
  ea = int(soup.find("span", {"class":"text__item-count"}).get_text().replace(",", ""))
  if ea % 100 == 0:
    pages = ea//100
  else:
    pages = ea//100+1

  for page in range(1, pages+1):
    url = BASE_URL_G + "&p={}".format(page)
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    contents = soup.find_all("div", {"class":"box__component box__component-itemcard box__component-itemcard--general"})
    for content in contents:
      price = content.find("strong", {"class":"text text__value"}).get_text()
      link = content.find("a", {"class":"link__item"})["href"]
      contents_g.append({"price":price, "link":link})
  return contents_g

def get_A():
  contents_A = []
  url = BASE_URL_A
  res = requests.get(url, headers=headers)
  soup = BeautifulSoup(res.text, "html.parser")
  ea = int(soup.find("span", {"class":"text--item_count"}).get_text().replace(",", ""))
  if ea % 100 == 0:
    pages = ea//100
  else:
    pages = ea//100+1

  for page in range(1, pages+1):
    url = BASE_URL_A + "&p={}".format(page)
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    contents = soup.find_all("div", {"class":"component component--item_card type--general"})
    for content in contents:
      price = content.find("strong", {"class":"text--price_seller"}).get_text()
      link = content.find("span", {"class":"text--itemcard_title ellipsis"}).a["href"]
      contents_A.append({"price":price, "link":link})
  return contents_A

def get_I():
  contents_I = []
  url = BASE_URL_I
  res = requests.get(url, headers=headers)
  soup = BeautifulSoup(res.text, "html.parser")
  contents = soup.find_all("li", {"class":"goods"})
  for content in contents:
    price = content.find("strong", {"class":"number"}).get_text()
    print(price)
    link = content.find("a", {"class":"name"})["href"]
    print(link)
    contents_I.append({"price":price, "link":link})
  return contents_I

def get_All():
  contents_All = get_G()
  contents_All += get_A()
  # contents_All += get_C()
  return contents_All