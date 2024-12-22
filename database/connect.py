import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

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