import re

# ca?e
# care, cafe, case, cave ...
p = re.compile("ca.e")
# . (.ca.e) :하나의 문자를 의미: care, cafe, case | caffee는 안됨 5글자.
# ^ ^(de) : 문자열의 시작: desk, destination | fade (x)
# $ (se$): 문자열의 끝: case, base | face (x)
# 다양한 것이 많지만 웹스크래핑 수업에서는 위 정도면 충분

# 정규식과 case가 매칭이 안되면 에러 발생


def print_match(m):
    if(m):
        print("m.group():", m.group())  # 일치하는 문자열 반환
        print("m.string:", m.string)  # 일치하는 문자열
        print("m.start():", m.start())  # 일치하는 문자열 시작 index
        print("m.end():", m.end())  # 일치하는 문자열 끝 index
        print("m.span():", m.span())  # 일치하는 문자열 끝 index
    else:
        print("매칭되지 않았습니다.")


# m = p.match("careless")  # 주어진 문자열의 '처음부터' 매칭하는지 확인. 예를들어 careless 같은 경우
# print_match(m)          # ca.e 와 매칭된다고 나오며 print_match시 care만 노출됨

# m = p.search("good care")  # 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("good care cafe")  # 일치하는 모든 것을 리스트 형태로 반환, care, cafe 면 2개 리스트로 해서 리턴
# print(lst)

# 정규식을 쓸 때 순서
# 1. p = re.compile("원하는 형태"):
# 2. m = p.match("비교할 문자열"): 주어진 문자열과 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열"): 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열"): 주어진 문자열 중에 일치하는 모든 것을 '리스트' 형태로 반환

# 원하는 형태 : 정규식
# . (.ca.e) :하나의 문자를 의미: care, cafe, case | caffee는 안됨 5글자.
# ^ ^(de) : 문자열의 시작: desk, destination | fade (x)
# $ (se$): 문자열의 끝: case, base | face (x)
