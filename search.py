from elasticsearch import Elasticsearch

ES_HOST = "http://localhost:9200"
query = raw_input("Search for people based on their Job Descrition: \n")

if __name__ == '__main__':

    es = Elasticsearch(ES_HOST)
    res = es.search(index="searchindex", doc_type="users", body={"query": {"match": {"job": query}}}, size=20)
    print("%d documents found:" % res['hits']['total'])
    for doc in res['hits']['hits']:
        print("%s) %s <mailto:%s>" % (doc['_id'], doc['_source']['name'], doc['_source']['email']))

