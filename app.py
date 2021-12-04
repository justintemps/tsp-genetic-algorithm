from src.city import City
from src.route import Route
from src.utils import random_city_name, random_lat_long

NUMBER_CITIES = 15

# The list of cities we'll be visiting
city_list = []

# Create new cities with random names and locations
# and put them in the list
for city in range(NUMBER_CITIES):
    city_name = random_city_name()
    lat, long = random_lat_long()
    new_city = City(city_name, lat, long)
    city_list.append(new_city)


if __name__ == "__main__":
    # Test City and Route
    geneva = City("Geneva", 46.204391, 6.143158)
    rome = City("Rome", 41.902782, 12.496365)
    vienna = City("Vienna", 48.2082, 16.3738)
    test_cities = [geneva, rome, vienna, geneva]
    test_route = Route(test_cities)
    assert round(test_route.distance) == 2265.0
