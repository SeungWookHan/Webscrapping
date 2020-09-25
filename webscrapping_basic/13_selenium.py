from selenium import webdriver

browser = webdriver.Chrome(
    "/Users/Han/programming/webscrapping/webscrapping_basic/chromedriver")  # 같은 경로에 있으면 경로 필요 없음
browser.get("http://naver.com")
