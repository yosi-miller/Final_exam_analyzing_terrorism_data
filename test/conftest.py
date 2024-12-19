import pymongo
import pytest

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
    csv_reader = read_csv('../data/terroris_db_1000_rows.csv')

    for i, row in enumerate(csv_reader):
        if i >= 20:
            break
        documents.append({'iyear': row['iyear']})
    # for row in read_csv('C:\\Users\y0504\Desktop\Week 5(10-10)\data\‏test_data.csv'):
    #     injuries = injuries_info(row)
    #     document = crash_document(row, injuries)
    test_db_collection.insert_many(documents)

