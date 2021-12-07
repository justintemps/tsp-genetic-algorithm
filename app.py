from src.city import City
from src.route import Route
from src.utils import breed_generation, random_gene_pool, rank_routes

# The number of cities in our route
NUMBER_CITIES = 20

# The number of routes in our initial population
INITIAL_POPULATION_SIZE = 100

# Rate at which we expect mutations
MUTATION_RATE = 0.1

# Number of generations to run our algorithm through
GENERATIONS = 100

# Number of top routes to conserve while breeding
ELITE_SIZE = 10

# Where in the route to dna to execute crossover
CROSSOVER_POINT = 10

# Number of steps away from closest city our route can move
# in a single leg. Example:
# 0 = closest city
# 1 = next closest city
# 2 = next closest city after that
# 3 ...
MAX_BASE = 2

if __name__ == "__main__":

    # Generate a list of City objects with random names and lat/long coords
    city_list = City.random_cities(NUMBER_CITIES)

    # Generate a gene pool
    dna_length = len(city_list) - 2
    gene_pool = random_gene_pool(INITIAL_POPULATION_SIZE, dna_length, MAX_BASE)

    # Generate our initial population of Route objects from the city_list and gene_pool
    initial_population = list(map(lambda dna: Route(city_list, dna), gene_pool))

    # placeholder for the last generation
    last_generation = initial_population

    # Generate a new population
    for generation in range(GENERATIONS):
        new_generation = breed_generation(
            last_generation, ELITE_SIZE, CROSSOVER_POINT, MUTATION_RATE)
        last_generation = new_generation

    print(rank_routes(initial_population)[0].distance)
    print(rank_routes(last_generation)[0].distance)
