class Route:
    def __init__(self, cities):
        assert isinstance(cities, list)
        # Make sure the last city is the same as the first
        assert repr(
            cities[0]) == repr(
            cities[-1]), "First and last cities must be the same"
        self.__cities = cities
        self.__distance = self.calc_distance()
        self.__fitness = self.calc_fitness()

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

    def calc_distance(self):
        """Calculates the total distance of the route"""
        distance = 0
        # Skip the last city which is the same as the first
        for city in range(0, len(self.__cities) - 1):
            distance += self.__cities[city].distance(self.__cities[city + 1])
        return distance

    def calc_fitness(self):
        """Assign a fitness score based on the distance of the route"""
        fitness = 10000 / self.__distance
        return fitness

    def __repr__(self):
        """print the route object"""
        city_names = map(lambda city: city.name, self.__cities)
        repr_str = ",".join(
            city_names) + f",{round(self.distance)}" + f",{self.fitness}"
        return repr_str
