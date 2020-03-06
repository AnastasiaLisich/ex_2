CITIES_FILE = './worldcitiespop.txt'


def count_population():
    cities_file = open(CITIES_FILE, 'rt', encoding='windows-1251')

    population = 0

    for string in cities_file:
        data_city = string.split(',')
        if data_city[4] != '':
            population += int(data_city[4])

    cities_file.close()

    return population


population = count_population()
print('{:,}'.format(population))





