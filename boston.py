from src.algorithm import genetic_algorithm
from src.city import City

INITIAL_POPULATION_SIZE = 4
MAX_BASE = 2
GENERATIONS = 20
CROSSOVER_POINT = 1
MUTATION_RATE = 0.1
ELITE_SIZE = 2

if __name__ == "__main__":

    # The cities to calcualte distances for
    boston = City("Boston", 42.361145, -71.057083)
    london = City("London", 51.5072, 0.1276)
    mumbai = City("Mumbai", 19.076090, 72.877426)
    shanghai = City("Shanghai", 31.224361, 121.469170)

    # Our list of cities
    city_list = [boston, london, mumbai, shanghai]

    best_route_start, best_route_end = genetic_algorithm(
        GENERATIONS, INITIAL_POPULATION_SIZE, cities=city_list,
        max_base=MAX_BASE, crossover_point=CROSSOVER_POINT,
        mutation_rate=MUTATION_RATE, elite_size=ELITE_SIZE)

    print(best_route_start, best_route_end)
