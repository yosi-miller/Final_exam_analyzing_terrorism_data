import csv
from pymongo import errors
from database.connect import get_db
# from database.model import crash_document, injuries_info
from services.logger_server import log_error, log_info


def read_csv(path='../data/terroris_db_1000_rows.csv'):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row


def init_crash_information_from_csv():
    """
    Initializes terrorism data from CSV file to MongoDB collection.
    """

    client, db = get_db()

    crash_collection = db['terrorism data']

    if crash_collection.count_documents({}) == 0:
        try:
            log_info(f'action: started insert crashs information to db')

            for row in read_csv('data/Traffic_Crashes_-_Crashes - 20k rows.csv'):
                injuries = injuries_info(row)

                document = crash_document(row, injuries)

                crash_collection.insert_one(document)

            log_info('action: completed insert crashs information to db')

            create_index(crash_collection)
            return True, 'action: completed insert crashs information to db'
        except errors.PyMongoError as e:
            log_error(f'action: try insert crashs information, error: {e}')
            print(f'Error: {e}')
            return False, e
        finally:
            client.close()
    return True, 'the db is already exsit'

# TODO: Implement this function
def create_index(crash_collection):
    # create a new index for the imported columns
    pass


if __name__ == '__main__':
    csv_path = '../data/terroris_db_1000_rows.csv'
    csv_reader = read_csv(csv_path)
    first_row = next(csv_reader)
    print(first_row)