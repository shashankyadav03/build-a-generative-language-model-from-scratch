import os
import numpy
import pickle
from numpy import dot
from numpy.linalg import norm


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(CURRENT_DIR + "/word_to_vector_trsf.pkl", "rb") as pk:
    word_to_vector = pickle.load(pk)

def cos_sim(a, b):
    return dot(a, b)/(norm(a)*norm(b))

def similar_words(word, top_k=10):
    return sorted(
        word_to_vector.keys(), 
        key=lambda x: cos_sim(word_to_vector[word], word_to_vector[x]),
        reverse=True
    )[:top_k]

print(similar_words("stop"))