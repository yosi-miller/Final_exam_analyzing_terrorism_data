from datetime import date

def create_terrier_attack_row(row):
    result = {
        'date': date(int(row['iyear']), int(row['imonth']), int(row['iday'])),
        'location': {'country': row['country_txt'],
                     'region': row['region_txt'],
                     'city': row['city'],
                     'latitude': row['latitude'],
                     'longitude': row['longitude']},
        'summary': row['summary'],
        'success': row['success'],
        'attack': {'attack_code': row['attacktype1'],
                    'attack_type': row['attacktype1_txt']},
        'target': {'target_code': row['targtype1'],
                   'target_type': row['targtype1_txt']},
        'group_name': row['gname'],
        'kill': row['nkill'],
        'injured': row['nwound'],

    }