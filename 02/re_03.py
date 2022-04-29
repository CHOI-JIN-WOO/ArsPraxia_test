# 정규표현식 03

import re

text = """
    100 John    PROF
    101 James   STUD
    102 Mac   STUD
"""

text_split = re.split("\s+", text)
text_onlyNum = re.split("\d+", text)

print(text_split)
print(text_onlyNum)

print(re.findall("[A-Z]", text))
print(re.findall('[A-Z]{4}', text))
print(re.findall('[A-Z][a-z]+', text))

