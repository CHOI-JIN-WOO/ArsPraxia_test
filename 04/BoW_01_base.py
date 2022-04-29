"""
BoW 01 base
"""

from konlpy.tag import Okt

okt = Okt()


def build_bag_of_words(document):
    document = document.replace(".", "")                # 구두점 제거
    tokenized_document = okt.morphs(document)           # 형태소 분석

    word_to_index = {}                                  # Dict 생성
    bow = []                                            # List 생성

    for word in tokenized_document:
        if word not in word_to_index.keys():
            word_to_index[word] = len(word_to_index)    # Dict 내 인덱싱
            bow.insert(len(word_to_index) - 1, 1)       # List 내 Default 1
        else:
            index = word_to_index.get(word)             # Dict 내 인덱스 검색
            bow[index] = bow[index] + 1                 # List 내 인덱스 + 1

    print(tokenized_document)                           # 확인용

    return word_to_index, bow
