from faker import Factory
from elasticsearch import Elasticsearch
import json
import time

ES_HOST = "http://localhost:9200"
es = Elasticsearch(ES_HOST)

number = 0

def create_names(fake):
    for x in range(1000):
        genName = fake.name()
        genJob = fake.job()
        genEmail = fake.email()
        global number
        number += 1

        go = es.index(
            index="searchindex",
            doc_type="users",
            id=str(number),
            body={
                "name": genName,
                "job": genJob,
                "email": genEmail
            }
        )

        print json.dumps(go)
        time.sleep(0.01)

if __name__ == '__main__':
    fake = Factory.create()
    create_names(fake)

