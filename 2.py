CITIES_FILE = './worldcitiespop.txt'


def count_population_in_country():
    cities_file = open(CITIES_FILE, 'rt', encoding='windows-1251')

    countries = {}
    population = 0
    current_country = ''

    for string in cities_file:
        data_city = string.split(',')

        if current_country == '':
            current_country = data_city[0]

        if current_country == data_city[0] and data_city[4] != '':
            population += int(data_city[4])
            countries[data_city[0]] = population

        if current_country != data_city[0] and data_city[4] != '':
            current_country = data_city[0]
            population = 0
            population += int(data_city[4])
            countries[data_city[0]] = population

    cities_file.close()

    return countries


def sort_countries():
    dict_with_countries = count_population_in_country()

    list_from_dict = list(dict_with_countries.items())
    list_from_dict.sort(key=lambda x: x[1])

    return list(list_from_dict)



def find_big_population_countries():
    sorted_countries = sort_countries()
    list_of_ten_count = sorted_countries[-10:][::-1]

    return dict(list_of_ten_count)

dict_of_ten_count = find_big_population_countries()
for country, population in dict_of_ten_count.items():
    print('Country: {}, Population: {:,}'.format(country, population))



