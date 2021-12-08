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
    between them in kilometers. First, convert degrees to radians so they
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
    """returns a tuple with random lat long pairs"""
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
    e.g. [[0,1,0,1][0,0,1,1]...]"""
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


def breed_generation(
        routes, elite_size=0, crossover_point=1, mutation_rate=0.1):
    """Takes a group of routes a breeds a new generation"""
    # The next generation
    children = []

    # Rank the routes in order of fitness
    ranked_routes = rank_routes(routes)

    # Promote elite routes to the next generation
    for i in range(elite_size):
        children.append(ranked_routes[i])

    # Get the fitness scores of all the routes
    fitness_scores = map(lambda route: route.fitness, ranked_routes)

    # Our roulette wheel is a dataframe. The last column has
    # rising percents based on the fitness scores of the matching route
    # To spin the wheel, we'll get a random number and then move up the table
    # until we find a parent
    roulette = pd.DataFrame(fitness_scores, columns=["fitness"])
    roulette['cum_sum'] = roulette.fitness.cumsum()
    roulette['percent'] = 100 * (
        roulette.cum_sum / roulette.fitness.sum())

    # Spin the wheel to get parents and create offspring until we have
    # a complete population
    for i in range(len(ranked_routes) - elite_size):
        parents = []
        # Select the two parents based on weighted probability
        while (len(parents) < 2):
            pick = 100 * rand.random()
            for j in range(0, len(ranked_routes)):
                if pick <= roulette.iat[j, 2]:
                    parents.append(ranked_routes[j])
                    break

        # crossover the two parents to create a child and add to new population
        parent_1, parent_2 = parents
        child = src.route.Route.breed(
            parent_1, parent_2, crossover_point, mutation_rate)
        children.append(child)

    return children
