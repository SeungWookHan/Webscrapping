from selenium import webdriver
import time

browser = webdriver.Chrome(
    "/Users/Han/programming/webscrapping/webscrapping_basic/chromedriver")
browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/flights/"

browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 29, 30일 클릭
# browser.find_elements_by_link_text("29")[0].click()  # [0] -> 이번달 달력에서 선택
# browser.find_elements_by_link_text("30")[0].click()

# 다음달 29, 30일 클릭
# browser.find_elements_by_link_text("29")[1].click()  # [1] -> 다음달 달력에서 선택
# browser.find_elements_by_link_text("30")[1].click()

# 이번달 29일부터 다음달 29일까지
browser.find_elements_by_link_text("29")[0].click()  # [0] -> 이번달 달력에서 선택
browser.find_elements_by_link_text(
    "28")[0].click()  # [1]하면 index out of range 뜸

browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()
browser.find_element_by_link_text("항공권 검색").click()

# 첫번째 결과
elem = browser.find_element_by_xpath(
    "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
print(elem)

# time.sleep(10)
# browser.quit()
