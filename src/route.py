class Route:
    def __init__(self, cities):
        assert isinstance(cities, list)
        # Make sure the last city is the same as the first
        assert repr(
            cities[0]) == repr(
            cities[-1]), "First and last cities must be the same"
        self.cities = cities
        self.__distance = self.calc_distance()

    @property
    def distance(self):
        """Returns the total distance of the route"""
        return self.__distance

    def calc_distance(self):
        """Calculates the total distance of the route"""
        distance = 0
        # Skip the last city which is the same as the first
        for city in range(0, len(self.cities) - 1):
            distance += self.cities[city].distance(self.cities[city + 1])
        return distance
