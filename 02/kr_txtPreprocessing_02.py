"""
한국어 전처리 패키지 02 : Py-Hanspell
"""

from hanspell import spell_checker

sent = "맞춤법 틀리면 외 않되? 쓰고싶은대로쓰면돼지"
spelled_sent = spell_checker.check(sent)
hanspell_sent = spelled_sent.checked

print(hanspell_sent)
