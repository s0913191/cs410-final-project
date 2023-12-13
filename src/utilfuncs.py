import numpy as np
from collections import Counter
from math import sqrt

def ngram(string, n=3):
    return [string[i:i+n] for i in range(len(string)-n+1)]

def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2)) / len(s1.union(s2))

def dice_coefficient(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    if not s1 and not s2:
        return 1.0
    return 2 * len(s1.intersection(s2)) / (len(s1) + len(s2))

def euclidean_distance(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    all_ngrams = set(counter1.keys()) | set(counter2.keys())
    distance = sum((counter1[ngram] - counter2[ngram]) ** 2 for ngram in all_ngrams)
    return distance ** 0.5

def levenshtein_distance(list1, list2):
    if len(list1) > len(list2):
        list1, list2 = list2, list1
    distances = range(len(list1) + 1)
    for i2, ngram2 in enumerate(list2):
        distances_ = [i2+1]
        for i1, ngram1 in enumerate(list1):
            if ngram1 == ngram2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

def distance_to_similarity_exp(d, beta=-0.1):
    return np.exp(beta * d)

def euclidean_similarity(list1, list2):
    return distance_to_similarity_exp(euclidean_distance(list1, list2))

def levenshtein_similarity(list1, list2):
    return distance_to_similarity_exp(levenshtein_distance(list1, list2))

def cosine_similarity(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    
    common_terms = set(counter1.keys()) & set(counter2.keys())
    dot_product = sum(counter1[term] * counter2[term] for term in common_terms)
    magnitude1 = sqrt(sum(val**2 for val in counter1.values()))
    magnitude2 = sqrt(sum(val**2 for val in counter2.values()))

    if not magnitude1 or not magnitude2:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)

def ensemble_similarity(list1, list2):
    similarity_func_pool = [cosine_similarity, jaccard_similarity, levenshtein_similarity, euclidean_similarity]
    avg_similarity = sum(similarity_func(list1,list2) for similarity_func in similarity_func_pool)/len(similarity_func_pool)
    return avg_similarity

def clean_str(string):
    s = ''.join(c for c in string if c.isalnum())
    s = s.lower()
    return s


