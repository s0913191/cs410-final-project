import searchfuncs as s
import utilfuncs as u

#print(s.search_result_match_rank('GENIE INDUSTRIES Z34E', 'Genie|Z-34/22N', cutoff=0.3))

#query = "Gehl 2480SX"
#query = "Caterpillar D7LR"
#query = "Caterpillar 32007"
query = "CAT320-07"
#query = "JCB 310"
#query = "CS 410"
#query = "Caterpillar D3C XL"
#query = "Genie Z-30/20N"
#query = "Caterpillar D10N"

#query = "CASE 1150G DOZER"
#similarity_func_pool = [cosine_similarity, jaccard_similarity, levenshtein_similarity, euclidean_similarity, ensemble_similarity]
similarity_func_pool = [u.cosine_similarity]
for similarity_func in similarity_func_pool:
    print(s.search_result(query, 3, similarity_func, 10, cutoff=0.5))