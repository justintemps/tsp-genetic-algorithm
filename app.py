from src.city import City
from src.utils import random_city_name, random_lat_long

NUMBER_CITIES = 15

city_list = []
for city in range(NUMBER_CITIES):
    city_name = random_city_name()
    lat, long = random_lat_long()
    new_city = City(city_name, lat, long)
    city_list.append(new_city)

if __name__ == "__main__":
    for city in city_list:
        print(repr(city))
