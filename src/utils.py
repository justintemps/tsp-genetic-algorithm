"""
A collection of utility functions
"""
import random as rand
from math import sin, cos, radians
from numpy import arccos, random, array
import pandas as pd
import src.route


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


def random_gene_pool(size, num_genes, max_base=1):
    """Returns a list of route dna lists
    e.g. [[0,1,0,1][0,0,1,1]...]
    """
    gene_pool = []
    for i in range(size):
        dna = []
        for j in range(num_genes):
            gene = rand.randrange(0, max_base + 1)
            dna.append(gene)
        gene_pool.append(dna)
    return gene_pool


def get_unvisited_cities(current_city, city_list, visited_cities):
    """Returns a list of unvisted cities sorted by distance from the current city"""
    unvisited_cities = [city for city in city_list
                        if city not in visited_cities]
    return sorted(
        unvisited_cities, key=lambda city: city.distance(current_city))


def rank_routes(routes):
    """Sort routes according to their fitness score"""
    return sorted(routes, key=lambda route: route.fitness, reverse=True)


def select_mating_pool(ranked_routes, elite_size=1):
    """Selects the mating pool of parents to be chosen to produce the next generation
    of routes. elite_size determines how many of the top scoring routes will be added
    off the bat. The best will be selected as a probability of their scores"""
    selection = []
    roulette = []
    # Select all of our elite routes right off the bat
    for i in range(0, elite_size):
        selection.append(ranked_routes[i])
    # Create a table of the routes so we can calculate the probability of their
    # being selected. This is our roulette wheel
    for i in range(elite_size, len(ranked_routes)):
        roulette.append((ranked_routes[i].id, ranked_routes[i].fitness))
    dataframe = pd.DataFrame(array(roulette), columns=["id", "fitness"])
    dataframe['running_total'] = dataframe.fitness.cumsum()
    dataframe['percent'] = 100 * (dataframe.fitness / dataframe.running_total)
    # Spin the roulette wheel
    for i in range(len(roulette)):
        pick = 100 * rand.random()
        if pick <= dataframe.iat[i, 3]:
            selection.append(ranked_routes[i])
    return selection


def breed_mating_pool(mating_pool, elite_size=1, crossover_point=1):
    children = []
    pool = rand.sample(mating_pool, len(mating_pool))
    # The elite group automatically makes it to the next generation
    for i in range(0, elite_size):
        children.append(mating_pool[i])

    # Everybody else has to breed new offspring
    for i in range(0, len(mating_pool) - elite_size):
        parent_1 = pool[i]
        parent_2 = pool[len(mating_pool) - i - 1]
        child = src.route.Route.breed(parent_1, parent_2, crossover_point)
        children.append(child)

    return children
