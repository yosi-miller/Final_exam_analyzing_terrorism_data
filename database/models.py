from datetime import datetime
from database.connect import get_db

client, db = get_db()
collection = db['terrorism_data']

def terrier_attack_model(row):
    result = {
        'date': datetime(int(row['iyear']),
                     int(row['imonth']) if int(row['imonth']) >= 1 else 1,
                     int(row['iday']) if int(row['iday']) >= 1 else 1),
        'location': {'country': row['country_txt'],
                     'region': row['region_txt'],
                     'city': row['city'],
                     'latitude': float(row['latitude']) if row['longitude'] != '' else None,
                     'longitude': float(row['longitude']) if row['longitude'] != '' else None},
        'summary': row['summary'],
        'success': int(row['success']),
        'attack': {'attack_code': int(row['attacktype1']),
                    'attack_type': row['attacktype1_txt']},
        'target': {'target_code': int(row['targtype1']),
                   'target_type': row['targtype1_txt']},
        'group_name': row['gname'],
        'amount_terorist': int(row['nperps']) if row['nperps'] >= '1' else 1,
        'kill': int(row['nkill']) if row['nkill'] >= '1' else 0,
        'injured': int(row['nwound']) if row['nwound'] >= '1' else 0
    }

    return result


def calculate_terrorism_amount(injuries, kills):
    victim_amount = injuries + kills
    match victim_amount:
        case _ if victim_amount < 5:
            return 1
        case _ if victim_amount < 10:
            return 2
        case _:
            return 3

def calculate_location():
    existing_data = list(collection.find({}, {"_id": 0, "location": 1}))
    data_map = {entry["location"]["country"]: entry["location"] for entry in existing_data}
    print(data_map)

def second_terrier_attack_model(row):
    result = {
        'date': datetime.strptime(row['date'], '%d-%b-%y'),
        'location': {'country': row['Country'],
                     # 'region': row['region_txt'],
                     'city': row['City'],
                     # 'latitude': float(row['latitude']) if row['longitude'] != '' else None,
                     # 'longitude': float(row['longitude']) if row['longitude'] != '' else None
                     },
        'summary': row['Description'],
        'attack': {'attack_code': None,
                    'attack_type': row['Weapon']},
        'target': {'target_code': None,
                   'target_type': 'Unknown'},
        'group_name': row['Perpetrator'],
        'amount_terorist': calculate_terrorism_amount(int(row['Injuries']), int(row['Fatalities'])),
        'kill': int(row['Fatalities']),
        'injured': int(row['Injuries'])
    }

    return result


if __name__ == '__main__':
    calculate_location()