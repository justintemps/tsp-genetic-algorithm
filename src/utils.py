"""
A collection of utility functions
"""
import random as rand
from math import sin, cos, radians
from numpy import arccos, random
import src.route
import src.city


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
    departure_city = city_list[0]
    # Separate the itinerary from the departure city
    itinerary = city_list[1:]
    # Randomize the itinerary stops
    itinerary = rand.sample(itinerary, len(itinerary))
    # Insert the departure city back at the beginning
    itinerary.insert(0, departure_city)
    # Create a new route
    route = src.route.Route(itinerary)
    return route


def create_population(pop_size, city_list):
    """Create a population of routes"""
    population = []
    for i in range(0, pop_size):
        population.append(create_route(city_list))
    return population


def cross_over(route_1, route_2, cross_over_point=2):
    assert route_1.cities[0].name == route_2.cities[0].name, "In cross_over, both routes must have the same first city"
    # Get everything from the first route up until the cross_over_point
    part_1 = route_1.cities[0:cross_over_point]
    # Fill in all the missing legs with the other route
    part_2 = [city for city in route_2.cities if city not in part_1]
    # PUt the two parts of the route together and instantiate a new Route object
    new_itinerary = part_1 + part_2
    return src.route.Route(new_itinerary)
