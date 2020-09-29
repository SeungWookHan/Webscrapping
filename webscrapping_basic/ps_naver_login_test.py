import time
import pyperclip
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

browser = webdriver.Firefox(
    executable_path="/Users/Han/programming/webscrapping/webscrapping_basic/geckodriver")  # 같은 경로에 있으면 경로 필요 없음
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
# elem = browser.find_element_by_class_name("input_text")
elem.click()

# id, pw 입력
tag_id = browser.find_element_by_id("id")
tag_pw = browser.find_element_by_id("pw")

tag_id.click()
time.sleep(1)
pyperclip.copy("naver_id")
tag_id.send_keys(Keys.COMMAND, 'v')  # 후.... 맥북은 COMMAND 였지...
time.sleep(1)

tag_pw.click()
pyperclip.copy("naver_pw")
tag_pw.send_keys(Keys.COMMAND, 'v')
time.sleep(1)

# 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys("my_id")

# html 정보 출력
print(browser.page_source)

# 브라우저 종료
browser.quit()
