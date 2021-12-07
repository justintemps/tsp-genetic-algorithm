from src.utils import get_city_distance, random_lat_long, random_city_name


class City:
    """
    Information and methods for city

    Args:
        - name (string): City name
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

    @classmethod
    def random_cities(self, size):
        """Returns a list of cities with random names
        and locations"""
        city_list = []
        for i in range(size):
            city_name = random_city_name()
            lat, long = random_lat_long()
            city = self(city_name, lat, long)
            city_list.append(city)
        return city_list

    def distance(self, city):
        """Returns distance in km to another City"""
        return get_city_distance(self, city)

    def __repr__(self):
        """print the city object"""
        lat, long = self.location
        return f'({self.name}, {lat}, {long})'


if __name__ == "__main__":
    city_1 = City("city_1", 46.204391, 6.143158)
    city_2 = City("city_2", 41.902782, 12.496365)
    distance = city_1.distance(city_2)
    assert isinstance(distance, float)
