from HashMap import HashMap
from graphs import *
class Truck:
    def __init__(self, truck_id, weight, driver, miles_driven, location):
        self.truck_id = truck_id
        self.weight = weight,
        self.packages = []
        self.stops = []
        self.driver = driver
        self.miles_driven = miles_driven
        self._speed = 18
        self.route = []
        self.pack_map = HashMap(16)
        self.location = location

    def get_vertices(self, graph):
        for item in self.packages:
            self.stops.append(graph.address_list[item.address])


