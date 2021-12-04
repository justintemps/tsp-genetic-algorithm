from src.utils import get_city_distance


class City:
    """
    Information and methods for city

    Args:
        - lat (float): latitude
        - long (float): longitude
    """

    def __init__(self, name, lat, long):
        assert isinstance(name, str), 'name must be a string'
        assert isinstance(lat, float), 'lat must be an float'
        assert isinstance(long, float), 'long must be an float'
        self.__name = name
        self.__lat = lat
        self.__long = long

    @property
    def name(self):
        """Returns the city name"""
        return self.__name

    @property
    def location(self):
        """Returns latlong tuple"""
        return self.__lat, self.__long

    def distance(self, city):
        """Returns distance in km to another City"""
        return get_city_distance(self, city)

    def __repr__(self):
        """print the city object"""
        lat, long = self.location
        return f'({self.name}, {lat}, {long})'


if __name__ == "__main__":
    city_1 = City(46.204391, 6.143158)
    city_2 = City(41.902782, 12.496365)
    distance = city_1.distance(city_2)
    assert isinstance(distance, float)
