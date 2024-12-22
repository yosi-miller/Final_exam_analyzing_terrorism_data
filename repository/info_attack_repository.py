import pandas as pd
from database.connect import get_db



def get_information_attack_data():
    """
    This function retrieves data from the 'terrorism_data' collection,
    normalizes it into a pandas DataFrame, and returns the DataFrame.
    """
    client, db = get_db()
    collection = db['terrorism_data']

    data = list(collection.find({}, {'_id': 0}))
    df = pd.json_normalize(data)
    return df

def information_deadly_attack():
    df = get_information_attack_data()
    columns = ['kill', 'injured', 'attack.attack_code', 'attack.attack_type']
    return df[columns]


if __name__ == '__main__':
    information_deadly_attack()