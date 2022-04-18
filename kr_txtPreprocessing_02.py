# 한국어 전처리 패키지 02

# 맞춤법 + 띄어쓰기 변환 패키지

from hanspell import spell_checker

sent = "맞춤법 틀리면 외 않되? 쓰고싶은대로쓰면돼지"
spelled_sent = spell_checker.check(sent)
hanspell_sent = spelled_sent.checked

print(hanspell_sent)