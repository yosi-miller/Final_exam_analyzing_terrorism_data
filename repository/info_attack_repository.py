import pandas as pd
from database.connect import get_db

client, db = get_db()
collection = db['terrorism_data']

def get_information_attack_data():
    """
    This function retrieves data from the 'terrorism_data' collection,
    normalizes it into a pandas DataFrame, and returns the DataFrame.
    """

    data = list(collection.find({}, {'_id': 0}))
    df = pd.json_normalize(data)
    return df

def deadly_attack_data():
    df = get_information_attack_data()
    columns = ['kill', 'injured', 'attack.attack_code', 'attack.attack_type']
    return df[columns]

def victims_and_region_data():
    df = get_information_attack_data()
    columns = ['kill', 'injured', 'location.region', 'location.latitude', 'location.longitude']
    return df[columns]

def years_region_and_attack_data():
    df = get_information_attack_data()
    columns = ['date', 'location.region', 'location.latitude', 'location.longitude']
    return df[columns]

def group_and_region_data():
    df = get_information_attack_data()
    columns = ['group_name', 'location.region', 'location.latitude', 'location.longitude']
    return df[columns]

def hitting_and_hits_data():
    df = get_information_attack_data()
    columns = ['amount_terorist', 'kill']
    return df[columns]

def group_and_type_attack_data():
    df = get_information_attack_data()
    columns = ['group_name', 'attack.attack_type']
    return df[columns]

def group_and_type_target_data():
    df = get_information_attack_data()
    columns = ['group_name', 'target.target_type']
    return df[columns]

def group_target_and_region_data():
    df = get_information_attack_data()
    columns = ['group_name', 'target.target_type', 'location.country', 'location.region', 'location.latitude', 'location.longitude']
    return df[columns]

def group_attack_and_region_data():
    df = get_information_attack_data()
    columns = ['group_name', 'attack.attack_type', 'location.country', 'location.region', 'location.latitude', 'location.longitude']
    return df[columns]

def unique_groups_by_area_data():
    df = get_information_attack_data()
    columns = ['group_name', 'location.country', 'location.region', 'location.latitude', 'location.longitude']
    return df[columns]


if __name__ == '__main__':
    print(hitting_and_hits_data().groupby('kill')['amount_terorist'].apply(list).reset_index())