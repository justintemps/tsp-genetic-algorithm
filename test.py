from src.route import Route
from src.city import City

if __name__ == "__main__":

    boston = City("Boston", 42.361145, -71.057083)
    london = City("London", 51.5072, 0.1276)
    mumbai = City("Mumbai", 19.076090, 72.877426)
    shanghai = City("Shanghai", 31.224361, 121.469170)

    # Our list of cities
    city_list = [boston, london, mumbai, shanghai]

    print("Mutated route: {route.mutated}")
    print(route.dna)
