# 정규표현식 02

import re

# search / match
r = re.compile("ab.")
print(r.search("kkkabc"))
print(r.match("kkkabc"))
print("")

# split
text = "사과 바나나 딸기 오렌지"
text_list = re.split(" ", text) # text.split(" ")
print(text_list)
print("")

# findall
text = """
    이름 : 김철수
    전화번호 : 010 - 1234 - 1234
    나이 : 30
    성별 : 남
"""
text_list = re.findall("\d+", text) # 최소 1개 이상의 모든 숫자 패턴
print(text_list)
print("")

# sub
text = "Regular expression : A regular expression, regex or regexp[1] (sometimes called a rational expression)[2][3] is, in theoretical computer science and formal language theory, a sequence of characters that define a search pattern."
text_list = re.sub("[^a-zA-Z]", " ", text)
print(text_list)
print("")
