from pororo import Pororo

tk = Pororo(task="tokenization", lang="ko", model="bpe32k.ko", )
tk("하늘을 나는 새를 보았다")
