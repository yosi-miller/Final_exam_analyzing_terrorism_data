import pandas as pd
from repository.info_attack_repository import deadly_attack_data, victims_and_region_data, get_information_attack_data, \
    group_and_region_data, hitting_and_hits, group_and_type_attack


# Q-1
def calculate_top_attacks(top_n=None):
    dataframe = deadly_attack_data()
    dataframe['impact'] = (dataframe['kill'] * 2) + dataframe['injured']

    result = dataframe.groupby('attack.attack_type')['impact'].sum().reset_index()

    result = result.sort_values(by='impact', ascending=False)

    if top_n:
        result = result.head(top_n)

    return result.to_dict(orient='records')

# Q-2
def calculate_average_casualties_by_area(top_n=None):
    dataframe = victims_and_region_data()
    dataframe['impact'] = (dataframe['kill'] * 2) + dataframe['injured']

    result = dataframe.groupby('location.region')[['impact', 'location.latitude', 'location.longitude']].mean().reset_index()

    result = result.sort_values(by='impact', ascending=False)

    if top_n:
        result = result.head(top_n)

    return result.to_dict(orient='records')

# Q-6
def calculate_percentage_change_attacks_by_region(top_n=None):
    dataframe = get_information_attack_data()
    dataframe['year'] = pd.to_datetime(dataframe['date']).dt.year

    # ספירת פיגועים לכל שנה לפי אזור
    yearly_counts = dataframe.groupby(['location.region', 'year']).size().reset_index(name='attack_count')
    # חישוב שינוי האחוזים בין כל השנים
    yearly_counts['percent_change'] = yearly_counts.groupby('location.region')['attack_count'].pct_change() * 100

    # חישוב סך שינוי האחוזים עבור כל אזור (התעלמות מ-NaN)
    total_changes = yearly_counts.groupby('location.region')['percent_change'].sum().reset_index()

    # חישוב מיקום ממוצע לכל אזור
    avg_location = dataframe.groupby('location.region').agg({
        'location.latitude': 'mean',
        'location.longitude': 'mean'
    }).reset_index()

    result = total_changes.merge(avg_location, on='location.region', how='left')
    result = result.sort_values(by='percent_change', ascending=False)

    if top_n:
        result = result.head(top_n)

    # החזרת התוצאה בפורמט JSON
    return result.to_dict(orient='records')

# Q-8
def calculate_most_active_groups_by_region(region=None):
    dataframe = group_and_region_data()

    result = dataframe.groupby(['location.region', 'group_name']).size().reset_index(name='attack_count')
    result = result.sort_values(by='attack_count', ascending=False)

    avg_location = dataframe.groupby('location.region').agg({
        'location.latitude': 'mean',
        'location.longitude': 'mean'
    }).reset_index()

    result = result.merge(avg_location, on='location.region', how='left')

    if region:
        result = result[result['location.region'] == region]

    return result[['location.region', 'location.latitude', 'location.longitude', 'group_name', 'attack_count']].to_dict(orient='records')

# Q-9 . קורלציה בין מספר הפוגעים למספר הנפגעים.
def calculate_correlation_between_hitting_and_hits():
    dataframe = hitting_and_hits()
    return dataframe['kill'].corr(dataframe['amount_terorist'])

# Q-13 איתור קבוצות שהשתתפו באותן תקיפות.
def calculate_groups_involved_in_same_attacks():
    dataframe = group_and_type_attack()

    result = dataframe.groupby('attack.attack_type')['group_name'].unique().reset_index()

    result['group_name'] = result['group_name'].apply(lambda x: list(x))

    return result.to_dict(orient='records')


if __name__ == '__main__':
    print(calculate_groups_involved_in_same_attacks())