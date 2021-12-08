import matplotlib.pyplot as plt
from src.city import City
from src.route import Route
from src.utils import breed_generation, random_gene_pool, rank_routes


def genetic_algorithm(
        generations, initial_population_size, number_cities=10, cities=None,
        max_base=1, crossover_point=1, mutation_rate=0.1, elite_size=1):

    # Our list of cities
    city_list = []

    # If no cities are provided, generate a random list of cities
    if (cities is None):
        city_list = City.random_cities(number_cities)

    # If a list of cities is provided, just use that
    if (cities is not None):
        city_list = cities

    # Generate a gene pool
    dna_length = len(city_list) - 2
    gene_pool = random_gene_pool(initial_population_size, dna_length, max_base)

    # Generate our initial population of Route objects from the city_list and gene_pool
    initial_population = list(map(lambda dna: Route(city_list, dna), gene_pool))

    # placeholder for the last generation
    last_generation = initial_population

    # This will hold our shortest distances from each generation
    progress = []
    progress.append(rank_routes(initial_population)[0].distance)

    # This will hold the shortest routes from the initial pop and last generation
    shortest_routes = []
    shortest_routes.append(rank_routes(initial_population)[0])

    # Generate a new population
    for generation in range(generations):
        new_generation = breed_generation(
            last_generation, elite_size, crossover_point, mutation_rate)
        shortest_distance = rank_routes(new_generation)[0].distance
        progress.append(shortest_distance)

        if (generation == generations - 1):
            shortest_routes.append(new_generation[0])

        last_generation = new_generation

    # Create a chart showing the performance of the algorithm
    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()

    # Return the best routes from the first and last generations
    return shortest_routes
