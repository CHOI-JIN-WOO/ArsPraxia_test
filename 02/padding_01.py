"""
패딩 01 : Numpy
"""

from padding_Base import encoded
import numpy as np

# 최대 길이 찾기
max_len = max(len(item) for item in encoded)

# 최대 길이에 맞게 0으로 채우기
for sentence in encoded:
    while len(sentence) < max_len:
        sentence.append(0)

padded = np.array(encoded)
