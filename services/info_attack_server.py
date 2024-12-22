from repository.info_attack_repository import information_deadly_attack


def calculate_top_attacks(top_n=None):
    dataframe = information_deadly_attack()
    dataframe['impact'] = (dataframe['kill'] * 2) + dataframe['injured']

    result = dataframe.groupby('attack.attack_type')['impact'].sum().reset_index()

    result = result.sort_values(by='impact', ascending=False)

    if top_n:
        result = result.head(top_n)

    return result.to_dict(orient='records')


if __name__ == '__main__':
    print(calculate_top_attacks(5))