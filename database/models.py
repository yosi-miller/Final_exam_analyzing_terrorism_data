from datetime import datetime

def create_terrier_attack_row(row):
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