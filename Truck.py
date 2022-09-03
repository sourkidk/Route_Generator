from HashMap import HashMap
from graphs import *

class Timer:
    def __init__(self):
        self.time = 0



class Truck:
    def __init__(self, truck_id, weight, start_time, driver, location, packages):
        self.truck_id = truck_id
        self.weight = weight,
        self.packages = packages
        self.stops = []
        self.driver = driver
        self.miles_driven = 0
        self._speed = 18
        self.route = []
        self.pack_map = HashMap(16)
        self.location = location
        self.current_stop = 0
        self.start_time = start_time

    def get_vertices(self, graph, map):
        for item in self.packages:
            self.stops.append(graph.address_list[map.get(item).address])

    def move_to_specific_stop(self, graph, stop):
        coordinate = (self.current_stop, stop)
        print(coordinate)
        next_stop = stop
        distance = graph.edge_weights[coordinate]
        print(f'Distance: {distance}')
        print(f'Next Stop: {next_stop}')
        self.miles_driven += distance
        self.stops.remove(stop)
        self.current_stop = stop

        print(f'Total Miles Driven: {round(self.miles_driven, 1)}')
        print("\n")


    def move_to_nearest_stop(self, graph):
        coordinate_list = [(self.current_stop, i) for i in self.stops]
        print(coordinate_list)

        distance, next_stop = min((graph.edge_weights[k], k) for k in coordinate_list)
        print(f'Distance: {distance}')
        print(f'Next Stop: {next_stop}')
        self.miles_driven += distance
        self.stops.remove(next_stop[1])
        self.current_stop = next_stop[1]

        print(f'Total Miles Driven: {round(self.miles_driven, 1)}')
        print("\n")

    def return_to_hub(self, graph):
        print(self.current_stop)
        distance = graph.edge_weights[(self.current_stop, 0)]
        print(f'Distance: {distance}')
        print('Next Stop: Hub')


        self.miles_driven += distance
        self.current_stop = 0

        print(f'Total Miles Driven: {round(self.miles_driven, 1)}')
        print("\n")

