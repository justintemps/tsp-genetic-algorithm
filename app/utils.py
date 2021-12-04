from math import sin, cos, radians
from numpy import arccos, random


def get_city_distance(city1, city2):
    """
    Take two pairs of city objects and return the distance
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
