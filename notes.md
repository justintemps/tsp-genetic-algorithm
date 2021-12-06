geneva, rome, vienna, boston, shanghai, sydney

step: 0
route: geneva
unvisited_cities: rome, vienna, boston, shanghai
strategy: 1
next_city: vienna

step: 1
route: geneva, vienna
unvisited_cities: rome, boston, shanghai
strategy: 1
next_city: rome

step: 2
route: geneva, vienna, boston
unvisited_cities: rome, shanghai
strategy: 0
next_city: rome

step: 3
route: geneva, vienna, boston, rome
unvisited_cities: shanghai
strategy: 1
next_city: shanghai

// if the next step is greater or equal to the length of unvisited_cities, then go to the last one

step: 4
route: geneva, vienna, boston, rome, shanghai
unvisited_cities: None
