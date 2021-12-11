from src.algorithm import genetic_algorithm

# The number of cities in our route
NUMBER_CITIES = 25

# The number of routes in our initial population
INITIAL_POPULATION_SIZE = 100

# Rate at which we expect mutations
MUTATION_RATE = 0.01

# Number of generations to run our algorithm through
GENERATIONS = 250

# Number of top routes to conserve while breeding
ELITE_SIZE = 20

# Where in the route to dna to execute crossover
CROSSOVER_POINT = 10

# Number of steps away from closest city our route can move
# in a single leg. Example:
# 0 = closest city
# 1 = next closest city
# 2 = next closest city after that
# 3 ...
MAX_BASE = 4

if __name__ == "__main__":

    best_route_start, best_route_end = genetic_algorithm(
        GENERATIONS, INITIAL_POPULATION_SIZE, NUMBER_CITIES, max_base=MAX_BASE,
        crossover_point=CROSSOVER_POINT, mutation_rate=MUTATION_RATE,
        elite_size=ELITE_SIZE)

    print(best_route_start, best_route_end)
