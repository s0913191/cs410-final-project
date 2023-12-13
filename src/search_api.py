from typing import Optional, List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

import numpy as np
import pandas as pd

import searchfuncs as s
import utilfuncs as u

import json

class SearchPair(BaseModel):
    make: str
    model: str
    top: int
    cutoff: Optional[float] = 0.1

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],
)


@app.post('/')
def search_api(data: SearchPair):
    query = s.make_dict.get(data.make,data.make) + data.model
    arr_result = s.search_result(query, n=3, similarity_func=u.cosine_similarity, top=data.top, cutoff=data.cutoff)
    return {'result': json.dumps(arr_result, cls=NumpyEncoder)}
