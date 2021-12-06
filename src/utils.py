"""
A collection of utility functions
"""
import random as rand
from math import sin, cos, radians
from numpy import arccos, random


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


def get_unvisited_cities(current_city, city_list, visited_cities):
    """Returns a list of unvisted cities sorted by distance from the current city"""
    unvisited_cities = [city for city in city_list
                        if city not in visited_cities]
    return sorted(
        unvisited_cities, key=lambda city: city.distance(current_city))


def rank_routes(routes):
    return sorted(routes, key=lambda route: route.fitness, reverse=True)
