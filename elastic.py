import json
import requests
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
r = requests.get('http://localhost:9200')
i = 1
while r.status_code == 200:
    r = requests.get('http://swapi.co/api/people/'+ str(i))
    es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    es.get(index='sw', doc_type='people', id=5)
    # es.get(index='sw', doc_type='people', id=5)
    # es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})
    # es.search(index="sw", body={"query": {"prefix" : { "name" : "lu" }}})
    # es.search(index="sw", body={"query": {"fuzzy_like_this_field" : { "name" : {"like_text": "jaba", "max_query_terms":5}}}})
    i=i+1

print(i)
