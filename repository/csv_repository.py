import csv
from pymongo import errors
from database.connect import get_db
from database.models import terrier_attack_model
from services.logger_server import log_error, log_info


def read_csv(path='C:\\Users\y0504\Desktop\Final exam - analyzing terrorism data\data\\terroris_db_1000_rows.csv'):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row


def init_crash_information_from_csv():
    """
    Initializes terrorism data from CSV file to MongoDB collection.
    """

    client, db = get_db()

    collection = db['terrorism_data']

    if collection.count_documents({}) == 0:
        try:
            log_info(f'action: started insert crashs information to db')

            chunk = []
            for row in read_csv():
                terrier_attack_document = terrier_attack_model(row)
                chunk.append(terrier_attack_document)

                if len(chunk) == 100:
                    collection.insert_many(chunk)
                    log_info('insert 100 documents with chunk')
                    print('insert 100 documents with chunk')
                    chunk = []

            if chunk:
                collection.insert_many(chunk)

            log_info('action: completed insert crashs information to db')

            create_index(collection)
            return True, 'action: completed insert crashs information to db'
        except errors.PyMongoError as e:
            log_error(f'action: try insert crashs information, error: {e}')
            print(f'Error: {e}')
            return False, e
        finally:
            client.close()
    return True, 'the db is already exsit'

def create_index(collection):
    """
    Create indexes for the imported columns to improve query performance.
    """
    collection.create_index([('date', 1)])
    collection.create_index([('location.country', 1)])
    collection.create_index([('location.region', 1)])
    collection.create_index([('location.city', 1)])
    collection.create_index([('attack.attack_code', 1)])
    collection.create_index([('target.target_code', 1)])
    collection.create_index([('group_name', 1)])
    collection.create_index([('kill', 1)])
    collection.create_index([('injured', 1)])


if __name__ == '__main__':
    csv_path = 'C:\\Users\y0504\Desktop\Final exam - analyzing terrorism data\data\RAND_Database_of_Worldwide_Terrorism_Incidents - 5000 rows (1).csv'
    csv_reader = read_csv(csv_path)
    first_row = next(csv_reader)
    print(first_row)