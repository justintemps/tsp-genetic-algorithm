class Route:
    def __init__(self, cities):
        assert isinstance(cities, list)
        # Make sure duplicate cities aren't supplied to Route
        assert len(set(cities)) == len(
            cities), "Duplicate city provided to Route"
        self.__cities = cities
        self.__distance = self.calc_distance()
        self.__legs = self.calc_legs()
        self.__fitness = self.calc_fitness()

    @property
    def legs(self):
        """Returns a list of the routes legs"""
        return self.__legs

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
        # Find the distance between all the ciites in the list
        for city in range(0, len(self.__cities) - 1):
            distance += self.__cities[city].distance(self.__cities[city + 1])
        # Add the distance from the last city back to the first
        distance += self.__cities[-1].distance(self.__cities[0])
        return distance

    def calc_legs(self):
        """Returns a list of each leg in the route"""
        legs = []

        # Get all of the legs of the trip up until the trip home
        for city in range(0, len(self.__cities) - 1):
            current_city = self.__cities[city]
            next_city = self.__cities[city + 1]
            distance = current_city.distance(next_city)
            legs.append((current_city, next_city, distance))

        # Add the trip home at the end
        last_stop = self.__cities[-1]
        departure_city = self.__cities[0]
        last_leg = (last_stop, departure_city,
                    last_stop.distance(departure_city))
        legs.append(last_leg)

        return legs

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
