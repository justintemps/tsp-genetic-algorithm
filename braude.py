from src.city import City
from src.route import Route


if __name__ == "__main__":
    geneva = City("Geneva", 46.204391, 6.143158)
    rome = City("Rome", 41.902782, 12.496365)
    vienna = City("Vienna", 48.2082, 16.3738)
    boston = City("Boston", 42.3601, -71.0589)
    shanghai = City("Shanghai", 31.2304, 121.4737)
    sydney = City("Sydney", -33.865143, 151.209900)

    city_list = [geneva, rome, vienna, boston, shanghai, sydney]

    route_1 = Route(city_list, [0, 1, 1, 1])
    route_2 = Route(city_list, [1, 2, 0, 0])
    print(route_1)
    print(route_2)

    route_3 = Route.breed(route_1, route_2, city_list, crossover_point=2)
    print(route_3)
