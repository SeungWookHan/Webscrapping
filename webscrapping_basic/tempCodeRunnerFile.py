import requests

res = requests.get("http://naver.com")
print("응답코드: ", res.status_code)

if res.status_code == requests.codes.ok:
    print("정상입니다.")
else:
    print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")
