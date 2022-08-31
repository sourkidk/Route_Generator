from HashMap import HashMap
from graphs import *
class Truck:
    def __init__(self, truck_id, weight, driver, location, packages):
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

    def get_vertices(self, graph, map):
        for item in self.packages:
            self.stops.append(graph.address_list[map.get(item).address])
    #
    # def move_to_next_stop(self, current_stop):
    #     s = self.stops
    #
    #     coordinate_list = [(0, i) for i in s]
    #     print(coordinate_list)
    #
    #     min_val, min_key = min((g.edge_weights[k], k) for k in coordinate_list)
    #     print(min_val)
    #     print(min_key)


