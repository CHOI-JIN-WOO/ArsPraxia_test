"""
패딩 02 : Keras
"""

from tensorflow.keras.preprocessing.sequence import pad_sequences
from padding_Base import encoded

# 패딩 진행
padded = pad_sequences(encoded)
