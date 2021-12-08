from src.city import City
from src.route import Route

# City will calculate the distance itself, so we give it
# lat/long coordinates instead
boston = City("Boston", 42.361145, -71.057083)
london = City("London", 51.5072, 0.1276)
mumbai = City("Mumbai", 19.076090, 72.877426)
shanghai = City("Shanghai", 31.224361, 121.469170)

city_list = [boston, shanghai, mumbai, london]
dna = [0, 0]
route = Route(city_list, dna)

print(route)
