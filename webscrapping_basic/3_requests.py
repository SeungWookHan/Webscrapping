import requests

res = requests.get("http://google.com")
# res = requests.get("wooogy.com")
print("응답코드: ", res.status_code)
res.raise_for_status()
# if 문 대신 raise_for_status() 사용.
print("웹 스크랩핑을 진행합니다")

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
