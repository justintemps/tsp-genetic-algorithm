from utils import get_city_distance


class City:
    """
    Information and methods for city

    Args:
        - lat (float): latitude
        - long (float): longitude
    """

    def __init__(self, lat, long):
        assert isinstance(lat, float), 'lat must be an Integer'
        assert isinstance(long, float), 'long must be an Integer'
        self.__lat = lat
        self.__long = long

    @property
    def location(self):
        """Returns latlong tuple"""
        return self.__lat, self.__long

    def distance(self, city):
        """Returns distance in km to another City"""
        return get_city_distance(self, city)


if __name__ == "__main__":
    city_1 = City(46.204391, 6.143158)
    city_2 = City(41.902782, 12.496365)
    distance = city_1.distance(city_2)
    assert isinstance(distance, float)
