CITIES_FILE = './worldcitiespop.txt'


def all_ru_cities():
    cities_file = open(CITIES_FILE, 'rt', encoding='windows-1251')
    all_ru_cities = []

    for string in cities_file:
        data_city = string.split(',')
        if data_city[0] == 'ru':
            if data_city[4] != '':
                all_ru_cities.append({'name': data_city[2], 'population': int(data_city[4])})

    cities_file.close()
    return all_ru_cities


def find_ten_big_cities():
    ru_cities = all_ru_cities()

    def sort_key(elem):
        return -elem['population']
    ru_cities.sort(key=sort_key)
    return ru_cities[:10]


ten_cities = find_ten_big_cities()
for n, c in enumerate(ten_cities, start=1):
    print('{:>2}. {:20}{:>15,}'.format(n, c['name'], c['population']))






