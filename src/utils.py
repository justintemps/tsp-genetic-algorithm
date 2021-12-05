"""
A collection of utility functions
"""
import random as rand
from math import sin, cos, radians
from numpy import arccos, random
import src.route
import src.city
import Route


def get_city_distance(city1, city2):
    """
    Uses Haversine Formula to take two pairs of city objects and return the distance
    between them in kilometers<Float>. First, convert degrees to radians so they
    work with python trig functions.
    """
    EARTH_RADIUS = 6371.0  # in kilometers
    city1_in_radians = (radians(city1.location[0]), radians(city1.location[1]))
    city2_in_radians = (radians(city2.location[0]), radians(city2.location[1]))
    return EARTH_RADIUS * arccos(sin(city1_in_radians[0]) *
                                 sin(city2_in_radians[0]) +
                                 cos(city1_in_radians[0]) *
                                 cos(city2_in_radians[0]) *
                                 cos(city1_in_radians[1] -
                                     city2_in_radians[1]))


def random_lat_long():
    """
    returns a tuple with random lat long pairs
    """
    lat_min = -90.
    lat_max = 90.
    long_min = -180.
    long_max = 180.
    lat = random.uniform(lat_min, lat_max, 1)
    long = random.uniform(long_min, long_max, 1)
    return lat[0], long[0]


def random_city_name(length=5):
    """returns a random city name"""
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    return "".join(
        rand.choice((consonants, vowels)[i % 2]) for i in range(length))


def create_route(city_list):
    """Shuffle the cities list and use it to create a new route"""
    cities = rand.sample(city_list, len(city_list))
    # Make sure the first city is also the last city
    first_city = cities[0]
    cities.append(first_city)
    route = src.route.Route(cities)
    return route

# TODO: We have to make sure that the first and last cities are always
# the same for each route in the population


def create_population(pop_size, city_list):
    """Create a population of routes"""
    population = []
    for i in range(0, pop_size):
        population.append(create_route(city_list))
    return population


# You are here!
# def rank_routes(population):
#     fitnessResults = {}
#     for i in range(0, len(population)):
#         fitnessResults[i] = Fitness(population[i]).routeFitness()
#     return sorted(
#         fitnessResults.items(),
#         key=operator.itemgetter(1),
#         reverse=True)


def cross_over(route_1, route_2, cross_over_point=1):
    route_1_cities = route_1.cities
    route_2_cities = route_2.cities
    assert route_1_cities[0] == route_2_cities[0] == route_1_cities[-1] == route_2_cities[-1], "First and last cities must be the same of both parents"
    parent_1 = route_1.cities[1:-1]
    parent_2 = route_2.cities[1:-1]
    child = parent_1[0:cross_over_point]
    child.append(parent_2[cross_over_point:])
    return Route(child)
