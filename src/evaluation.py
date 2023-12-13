import numpy as np
import pandas as pd

import utilfuncs as u
import searchfuncs as s

from collections import Counter
from math import sqrt

validation_labeled_path = fr"validation_labeled.txt"
df_validation_labeled = pd.read_csv(validation_labeled_path, sep='|')

# Get match rankings
df_validation_labeled["CosineRank_0.1"] = df_validation_labeled.apply(lambda row: s.search_result_match_rank(s.make_dict.get(row.EQMAKE,row.EQMAKE) + row.EQMODL, row.CorrectMake+'|'+row.CorrectModel, similarity_func=u.cosine_similarity, cutoff=0.1), axis=1)
df_validation_labeled["CosineRank_0.2"] = df_validation_labeled.apply(lambda row: s.search_result_match_rank(s.make_dict.get(row.EQMAKE,row.EQMAKE) + row.EQMODL, row.CorrectMake+'|'+row.CorrectModel, similarity_func=u.cosine_similarity, cutoff=0.2), axis=1)
df_validation_labeled["CosineRank_0.3"] = df_validation_labeled.apply(lambda row: s.search_result_match_rank(s.make_dict.get(row.EQMAKE,row.EQMAKE) + row.EQMODL, row.CorrectMake+'|'+row.CorrectModel, similarity_func=u.cosine_similarity, cutoff=0.3), axis=1)
print("-----Done with CosineRank-----")
df_validation_labeled["LevenshteinRank_0.1"] = df_validation_labeled.apply(lambda row: s.search_result_match_rank(s.make_dict.get(row.EQMAKE,row.EQMAKE) + row.EQMODL, row.CorrectMake+'|'+row.CorrectModel, similarity_func=u.levenshtein_similarity, cutoff=0.1), axis=1)
df_validation_labeled["LevenshteinRank_0.2"] = df_validation_labeled.apply(lambda row: s.search_result_match_rank(s.make_dict.get(row.EQMAKE,row.EQMAKE) + row.EQMODL, row.CorrectMake+'|'+row.CorrectModel, similarity_func=u.levenshtein_similarity, cutoff=0.2), axis=1)
df_validation_labeled["LevenshteinRank_0.3"] = df_validation_labeled.apply(lambda row: s.search_result_match_rank(s.make_dict.get(row.EQMAKE,row.EQMAKE) + row.EQMODL, row.CorrectMake+'|'+row.CorrectModel, similarity_func=u.levenshtein_similarity, cutoff=0.3), axis=1)
print("-----Done with LevenshteinRank-----")
df_validation_labeled["JaccardRank_0.1"] = df_validation_labeled.apply(lambda row: s.search_result_match_rank(s.make_dict.get(row.EQMAKE,row.EQMAKE) + row.EQMODL, row.CorrectMake+'|'+row.CorrectModel, similarity_func=u.jaccard_similarity, cutoff=0.1), axis=1)
df_validation_labeled["JaccardRank_0.2"] = df_validation_labeled.apply(lambda row: s.search_result_match_rank(s.make_dict.get(row.EQMAKE,row.EQMAKE) + row.EQMODL, row.CorrectMake+'|'+row.CorrectModel, similarity_func=u.jaccard_similarity, cutoff=0.2), axis=1)
df_validation_labeled["JaccardRank_0.3"] = df_validation_labeled.apply(lambda row: s.search_result_match_rank(s.make_dict.get(row.EQMAKE,row.EQMAKE) + row.EQMODL, row.CorrectMake+'|'+row.CorrectModel, similarity_func=u.jaccard_similarity, cutoff=0.3), axis=1)
print("-----Done with JaccardRank-----")
df_validation_labeled["EuclideanRank_0.1"] = df_validation_labeled.apply(lambda row: s.search_result_match_rank(s.make_dict.get(row.EQMAKE,row.EQMAKE) + row.EQMODL, row.CorrectMake+'|'+row.CorrectModel, similarity_func=u.euclidean_similarity, cutoff=0.1), axis=1)
df_validation_labeled["EuclideanRank_0.2"] = df_validation_labeled.apply(lambda row: s.search_result_match_rank(s.make_dict.get(row.EQMAKE,row.EQMAKE) + row.EQMODL, row.CorrectMake+'|'+row.CorrectModel, similarity_func=u.euclidean_similarity, cutoff=0.2), axis=1)
df_validation_labeled["EuclideanRank_0.3"] = df_validation_labeled.apply(lambda row: s.search_result_match_rank(s.make_dict.get(row.EQMAKE,row.EQMAKE) + row.EQMODL, row.CorrectMake+'|'+row.CorrectModel, similarity_func=u.euclidean_similarity, cutoff=0.3), axis=1)
print("-----Done with EuclideanRank-----")
df_validation_labeled["EnsembleRank_0.1"] = df_validation_labeled.apply(lambda row: s.search_result_match_rank(s.make_dict.get(row.EQMAKE,row.EQMAKE) + row.EQMODL, row.CorrectMake+'|'+row.CorrectModel, similarity_func=u.ensemble_similarity, cutoff=0.1), axis=1)
df_validation_labeled["EnsembleRank_0.2"] = df_validation_labeled.apply(lambda row: s.search_result_match_rank(s.make_dict.get(row.EQMAKE,row.EQMAKE) + row.EQMODL, row.CorrectMake+'|'+row.CorrectModel, similarity_func=u.ensemble_similarity, cutoff=0.2), axis=1)
df_validation_labeled["EnsembleRank_0.3"] = df_validation_labeled.apply(lambda row: s.search_result_match_rank(s.make_dict.get(row.EQMAKE,row.EQMAKE) + row.EQMODL, row.CorrectMake+'|'+row.CorrectModel, similarity_func=u.ensemble_similarity, cutoff=0.3), axis=1)
print("-----Done with EnsembleRank-----")

# Actually not matched AND labeled NotFound
for col in ['CosineRank_0.1', 'CosineRank_0.2', 'CosineRank_0.3'
           , 'LevenshteinRank_0.1', 'LevenshteinRank_0.2', 'LevenshteinRank_0.3'
           , 'JaccardRank_0.1', 'JaccardRank_0.2', 'JaccardRank_0.3'
           , 'EuclideanRank_0.1', 'EuclideanRank_0.2', 'EuclideanRank_0.3'
           , 'EnsembleRank_0.1', 'EnsembleRank_0.2', 'EnsembleRank_0.3']:
    df_validation_labeled.loc[
        ((df_validation_labeled['CorrectMake'] == 'NotFound')
        | (df_validation_labeled['CorrectModel'] == 'NotFound'))
        & (df_validation_labeled[col].isna())
        ,col
    ] = 1.0

    # Actually matched AND labeled NotFound
    df_validation_labeled.loc[
        ((df_validation_labeled['CorrectMake'] != 'NotFound')
        & (df_validation_labeled['CorrectModel'] != 'NotFound'))
        & (df_validation_labeled[col].isna())
        ,col
    ] = 10.0

for col in ['CosineRank_0.1', 'CosineRank_0.2', 'CosineRank_0.3'
           , 'LevenshteinRank_0.1', 'LevenshteinRank_0.2', 'LevenshteinRank_0.3'
           , 'JaccardRank_0.1', 'JaccardRank_0.2', 'JaccardRank_0.3'
           , 'EuclideanRank_0.1', 'EuclideanRank_0.2', 'EuclideanRank_0.3'
           , 'EnsembleRank_0.1', 'EnsembleRank_0.2', 'EnsembleRank_0.3']:
    mean_ap = (1/df_validation_labeled[col]).mean()
    print('Mean AP - ' + col +': \t' + str(mean_ap))