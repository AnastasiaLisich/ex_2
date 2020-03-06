# a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
# c = 2 ⋅ atan2( √a, √(1−a) )
# d = R ⋅ c
# φ is latitude, λ is longitude, R is Earth’s radius (mean radius = 6,371km);
# note that angles need to be in radians to pass to trig functions!
# y = x * math.pi / 180
import math

CITIES_FILE = './worldcitiespop.txt'


def deg_to_rad(angle):
    return angle * math.pi / 180
    # degree to radian

def calc_distance(point_1, point_2):
    phi1 = deg_to_rad(point_1[0])
    phi2 = deg_to_rad(point_2[0])
    lambda_1 = deg_to_rad(point_1[1])
    lambda_2 = deg_to_rad(point_2[1])

    R =  6357  # km

    a = math.sin((phi2 - phi1) / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin((lambda_2 - lambda_1) / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

def calc_distance_between_cities(city_1, city_2, cities):
    city_1_point = cities[city_1.lower()]
    city_2_point = cities[city_2.lower()]
    return calc_distance(city_1_point, city_2_point)


def read_cities_file():
    cities_file = open(CITIES_FILE, 'rt', encoding='windows-1251')

    city_coordinates = {}

    for string in cities_file:
        lst = string.split(',')
        if lst[4] != '' and int(lst[4]) > 2000000:
            city_coordinates[lst[1]] = (float(lst[5]), float(lst[6]))

    cities_file.close()

    return city_coordinates


def main():
    # cities = {'Moscow': (55, 37), 'Oslo': (60, 11)}
    cities = read_cities_file()

    while True:
        first_city = input('Enter the first city: ')
        second_city = input('Enter the second city: ')
        distance = round(calc_distance_between_cities(first_city, second_city, cities))

        print('The distance between {} and {} is {} km'.format(
            first_city, second_city, distance
        ))


main()

# Ctrl + C



