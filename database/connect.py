import os
from pymongo import MongoClient

def get_db():
    """
    connect to local MongoDb
    :return:
    """
    url = os.getenv('MONGO_URL')
    port = os.getenv('MONGO_PORT')
    print(url, port)

    client = MongoClient(url, int(port))
    db = client['Final_exam-analyzing_terrorism_data']
    return client, db