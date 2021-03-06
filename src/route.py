import random
import src.utils


class Route:
    def __init__(self, city_list, dna, mutation_rate=0.1):
        assert isinstance(dna, list), "dna must be a list of ints"
        assert isinstance(
            city_list, list), "city_list must be a list of City objects"
        self.__mutation_rate = mutation_rate
        self.__mutated = False
        self.__dna = self.__possibly_mutated(dna)
        self.__cities = self.__derive_cities(city_list, self.__dna)
        self.__distance = self.__calc_distance()
        self.__fitness = self.__calc_fitness()

    @property
    def mutated(self):
        """Tells us whether this Route mutated or not"""
        return self.__mutated

    @property
    def dna(self):
        """Returns a copy of the route's DNA (strategy)"""
        return self.__dna

    @property
    def fitness(self):
        """Returns the route's fitness score"""
        return self.__fitness

    @property
    def cities(self):
        """Returns the total list of cities"""
        return self.__cities

    @property
    def distance(self):
        """Returns the total distance of the route"""
        return self.__distance

    @classmethod
    def breed(self, route_1, route_2, crossover_point=1, mutation_rate=0.1):
        """Uses crossover to create a child route from two parent routes"""
        assert len(route_1.dna) == len(
            route_2.dna), "In crossover, parent DNA must have same length"
        assert len(
            route_1.dna) > crossover_point, "In crossover, crossover_point can't be greater that parents' length"
        assert set(route_1.cities) == set(
            route_2.cities), "You may not breed two routes with different cities"
        gene_1 = route_1.dna[:crossover_point]
        gene_2 = route_2.dna[crossover_point:]
        # The order of the cities isn't important, they'll just get sorted by distance
        # when the route derives cities from dna
        city_list = route_1.cities
        new_dna = gene_1 + gene_2
        return self(city_list, new_dna, mutation_rate)

    def __derive_cities(self, city_list, strategy):
        """Dervie a list of cities from the city_list according to a strategy
        defining which order to visit the cities in, assuming that all cities
        must be visited once"""
        cities = [city_list[0]]

        assert len(strategy) == len(
            city_list) - 2, "strategy should have two fewer elements than city_list"

        # Plus one to take into account the return trip
        for step in range(len(strategy) + 1):
            # Get the unvisited cities in order of distance to the current city
            unvisited_cities = src.utils.get_unvisited_cities(
                cities[step], city_list, cities)
            # If there's only one more city in the list, add it and be done
            if (len(unvisited_cities) == 1):
                cities.append(unvisited_cities[0])
                break
            # If the next step is out of range, use the last city in the list
            if (strategy[step] >= len(unvisited_cities)):
                cities.append(unvisited_cities[-1])
                continue
            # Otherwise, vove to the next city according to the step in our strategy
            next_move = strategy[step]
            next_city = unvisited_cities[next_move]
            cities.append(next_city)

        return cities

    def __possibly_mutated(self, dna):
        for swapped in range(len(dna)):
            if (random.random() < self.__mutation_rate):
                swapWith = int(random.random() * len(dna))

                gene_1 = dna[swapped]
                gene_2 = dna[swapWith]

                dna[swapped] = gene_2
                dna[swapWith] = gene_1

                self.__mutated = True
        return dna

    def __calc_distance(self):
        """Calculates the total distance of the route"""
        distance = 0
        # Find the distance between all the ciites in the list
        for city in range(0, len(self.__cities) - 1):
            distance += self.__cities[city].distance(self.__cities[city + 1])
        # Add the distance from the last city back to the first
        distance += self.__cities[-1].distance(self.__cities[0])
        return distance

    def __calc_fitness(self):
        """Assign a fitness score based on the distance of the route"""
        fitness = 10000 / self.__distance
        return fitness

    def __repr__(self):
        """print the route object"""
        city_names = list(map(lambda city: city.name, self.__cities))
        city_names.append(city_names[0])
        repr_str = f"{self.__mutated}  " f"{self.__dna}  " + " -> ".join(
            city_names) + f"  {round(self.distance):,}km" + f"  {round(self.fitness, 4)}"
        return repr_str
