# headless 주의할 점
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2560x1600")

# 이 라인을 통해 user_Agent 를 바꿔줌
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36")
# user-agent 사이 = 붙여야지 잘 들어감

browser = webdriver.Chrome(
    "/Users/Han/programming/webscrapping/webscrapping_basic/chromedriver", options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6)
# AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/85.0.4183.102 Safari/537.36
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)

# 하지만 여기서는 eadlessChrome/85.0.4183.121 Safari/537.36 이렇게 나옴
# 즉 서버 입장에서 위 user_Agent를 막을 수 있음
