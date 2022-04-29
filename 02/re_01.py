# 정규표현식 01

import re

# .
print("[. 기호]")
r = re.compile("a.c")
print(r.search("ac"))
print(re.compile("a.c").search("abc"))
print(r.search("abbc"))
print("")

# ?
print("[? 기호]")
r = re.compile("ab?c")
print(r.search("ac"))
print(r.search("abc"))
print(re.compile("ab?c").search("abbc"))
print("")

# *
print("[* 기호]")
r = re.compile("ab*c")
print(r.search("ac"))
print(r.search("abc"))
print(r.search("abbc"))
print("")

# +
print("[+ 기호]")
r = re.compile("ab+c")
print(r.search("ac"))
print(r.search("abc"))
print(r.search("abbc"))
print("")

# ^
print("[^ 기호]")
r = re.compile("^ab")
print(r.search("a"))
print(r.search("ab"))
print(r.search("abc"))
print("")

# {}
print("[{} 기호]")
r = re.compile("ab{2,8}c")
print(r.search("ac"))
print(r.search("abc"))
print(r.search("abbc"))
print(r.search("abbbc"))
print("")

# []
print("[[] 기호]")
r = re.compile("[abc]")
print(r.search("a"))
print(r.search("ab"))
print(r.search("abc"))
print(r.search("abbc"))
print("")

# [^]
print("[[] 기호]")
r = re.compile("[^abc]")
print(r.search("a"))
print(r.search("ab"))
print(r.search("abc"))
print(r.search("d"))
print("")
