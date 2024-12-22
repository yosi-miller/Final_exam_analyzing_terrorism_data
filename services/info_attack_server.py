from repository.info_attack_repository import deadly_attack_data, victims_and_region_data


def calculate_top_attacks(top_n=None):
    dataframe = deadly_attack_data()
    dataframe['impact'] = (dataframe['kill'] * 2) + dataframe['injured']

    result = dataframe.groupby('attack.attack_type')['impact'].sum().reset_index()

    result = result.sort_values(by='impact', ascending=False)

    if top_n:
        result = result.head(top_n)

    return result.to_dict(orient='records')

def calculate_average_casualties_by_area(top_n=None):
    dataframe = victims_and_region_data()
    dataframe['impact'] = (dataframe['kill'] * 2) + dataframe['injured']

    result = dataframe.groupby('location.region')[['impact', 'location.latitude', 'location.longitude']].mean().reset_index()

    result = result.sort_values(by='impact', ascending=False)

    if top_n:
        result = result.head(top_n)

    return result.to_dict(orient='records')
if __name__ == '__main__':
    print(calculate_average_casualties_by_area(5))