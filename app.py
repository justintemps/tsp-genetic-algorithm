from numpy.random.mtrand import normal
from src.city import City
from src.route import Route
from src.utils import breed_mating_pool, random_gene_pool, rank_routes, select_mating_pool

NUMBER_CITIES = 8
INITIAL_POPULATION_SIZE = 200
DNA_LENGTH = NUMBER_CITIES - 2
ELITE_SIZE = 10
CROSSOVER_POINT = 2

if __name__ == "__main__":

    # Generate a list of City objects with random names and lat/long coords
    city_list = City.random_cities(NUMBER_CITIES)

    # Generate a gene pool
    gene_pool = random_gene_pool(INITIAL_POPULATION_SIZE, DNA_LENGTH)

    # Generate Route objects from the city_list and gene_pool
    initial_population = list(map(lambda dna: Route(city_list, dna), gene_pool))

    # Rank routes in order of their fitness score
    ranked_population = rank_routes(initial_population)

    # Select the parents for our first generation
    mating_pool = select_mating_pool(ranked_population, ELITE_SIZE)

    # Breed population to get a new generation
    next_generation = breed_mating_pool(
        mating_pool, ELITE_SIZE, CROSSOVER_POINT)

    for route in next_generation:
        print(route)
