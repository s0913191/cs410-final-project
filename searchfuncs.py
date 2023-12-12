import numpy as np
import utilfuncs as u
import json

make_dict = {
    'CAT':'Caterpillar'
    ,'CATERPILLAR INC.':'Caterpillar'
    ,'GENIE INDUSTRIES':'Genie'
    ,'CATERPILLAR, INC.':'Caterpillar'
    ,'CATERPILLAR INC':'Caterpillar'
    ,'AA':'Caterpillar'
    ,'GENIE LIFT':'Genie'
    ,'CHALLENGER':'Challenger'
    ,'AGCO CHALLENGER':'Challenger'
    ,'DEERE':'John Deere'
    ,'JD':'John Deere'
    ,'GI':'Genie'
    ,'MIT':'Mitsubishi'
    ,'KUB':'Kubota'
    ,'KOB':'Kobelco'
    ,'G1':'Genie'
    ,'NH':'New Holland'
}

dataset_path = fr"consolidated_docs.json"
data = []
with open(dataset_path, 'r') as f:
    jsonl_data = [json.loads(l) for l in f.readlines()]

for dic in jsonl_data:
    equipment_make = dic["equipment_make"]
    equipment_model = dic["equipment_model"]
    data.append((equipment_make, equipment_model))

def search_result(query: str, n=3, similarity_func=u.cosine_similarity, top=10, cutoff=0.0):
    query = u.clean_str(query)
    query_ngrams = u.ngram(query, n)
    similarities = np.empty([0])

    for make, model in data:
        data_make_model = u.clean_str(make + model)
        data_make_model_ngrams = u.ngram(data_make_model, n)
        similarity = similarity_func(query_ngrams, data_make_model_ngrams)
        similarities = np.append(similarities, similarity)

    similarities_sorted_idx = np.argsort(similarities, axis=-1,kind='quicksort')

    result = np.empty((0,2))
    for i in range(1,len(similarities_sorted_idx)+1):
        if i > top: break
        idx = similarities_sorted_idx[-i]
        if similarities[idx] < cutoff: break
        result = np.append(result, np.array([[data[idx], similarities[idx]]], dtype=object), axis=0)
    return result

def search_result_match_rank(query: str, answer: str, n=3, similarity_func=u.cosine_similarity, top=10, cutoff=0.0):
    search = search_result(query, n, similarity_func, top, cutoff)
    #print(search)
    for idx, pair in enumerate(search):
        if pair[1] < cutoff:
            break
        if pair[0][0]+'|'+pair[0][1] == answer:
            return idx+1
    return None