from src.city import City
from src.route import Route
from src.utils import random_city_name, random_lat_long, create_population, cross_over

# The number of cities to visit
NUMBER_CITIES = 6

# The number of different routes we'll generate
# in our initial population
POPULATION_SIZE = 2

# The list of cities we'll be visiting
city_list = []

# Create new cities with random names and locations
for city in range(NUMBER_CITIES):
    city_name = random_city_name()
    lat, long = random_lat_long()
    new_city = City(city_name, lat, long)
    city_list.append(new_city)

# A list of routes that will make up our initial population
initial_population = create_population(POPULATION_SIZE, city_list)


if __name__ == "__main__":
    # Test City and Route
    geneva = City("Geneva", 46.204391, 6.143158)
    rome = City("Rome", 41.902782, 12.496365)
    vienna = City("Vienna", 48.2082, 16.3738)

    test_cities = [geneva, rome, vienna]
    test_route = Route(test_cities)
    assert round(test_route.distance) == 2265.0

    for route in initial_population:
        print(route)

    route_1, route_2 = initial_population

    new_route = cross_over(route_1, route_2)
    print(new_route)
