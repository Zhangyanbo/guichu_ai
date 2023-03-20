import openai
import pandas as pd
import numpy as np
import time
import tqdm
import backoff


@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def embed(string):
    emb = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=string
        )
    return np.array(emb['data'][0]['embedding'])

def batch_embedding(string_list):
    '''embed the list of strings in batches'''
    embs = []
    for string in tqdm.tqdm(string_list):
        embs.append(embed(string))
    return np.array(embs)

def search_embedding(query_emb, embedding_list, top_k=10):
    '''search for the top_k most similar embeddings using cosine distance'''
    dists = np.array([1.0 - np.dot(query_emb, emb) for emb in embedding_list])
    idx = np.argsort(dists)[:top_k]
    return idx, dists[idx]

def search(query, embedding_list, data, top_k=5):
    '''search for the top_k most similar strings using cosine distance
    return the data frame of the top_k most similar strings, and the distance
    combined in a data frame
    '''
    query_emb = embed(query)
    top_k_idx, distance = search_embedding(query_emb, embedding_list, top_k)
    selected_data = data.iloc[top_k_idx]
    result_data = selected_data.copy()
    result_data['similarity'] = 1 - distance
    return result_data

@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def complete(query, max_tokens=30, temperature=1):
    '''complete the query string'''
    resp = openai.Completion.create(
                model="text-davinci-003",
                prompt=query,
                max_tokens=max_tokens,
                temperature=temperature
            )
    return resp['choices'][0]['text']

def search_next(query, embedding_list, data, top_k=5, max_tokens=30, temperature=1):
    '''search for next string given the query'''
    next_string = complete(query)
    return search(next_string, embedding_list, data, top_k)