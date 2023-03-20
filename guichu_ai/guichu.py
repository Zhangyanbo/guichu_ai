import openai
from .utils import batch_embedding, search, search_next


class GuichuMaster:
    def __init__(self, dataset, key, embedding=None):
        openai.api_key = key
        if embedding is None:
            self.embedding = batch_embedding(dataset['content'])
        else:
            self.embedding = embedding
        self.data = dataset
    
    def search(self, query, top_k=5):
        return search(query, self.embedding, self.data, top_k)
    
    def search_next(self, query, top_k=5, max_tokens=30, temperature=1):
        return search_next(query, self.embedding, self.data, top_k, max_tokens, temperature)