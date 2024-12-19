import pymongo
import pytest

from database.models import create_terrier_attack_row
from repository.csv_repository import read_csv


# from database.model import crash_document, injuries_info
# from repository.csv_repository import read_csv


@pytest.fixture
def init_db():
    client = pymongo.MongoClient('localhost', 27017)
    test_db = client['test_db']
    yield test_db
    client.drop_database('test_db')
    client.close()

@pytest.fixture
def test_db_collection(init_db):
    test_collection = init_db['test_collection']
    return test_collection

@pytest.fixture
def populate_crash_db(test_db_collection):
    documents = []
    csv_reader = read_csv()

    for i, row in enumerate(csv_reader):
        if i >= 20:
            break
        documents.append(create_terrier_attack_row(row))
    test_db_collection.insert_many(documents)

