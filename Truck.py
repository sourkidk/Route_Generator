from HashMap import HashMap
from graphs import *
from datetime import *
from util import *
import sys

class Timer:
    def __init__(self):
        self.time = 0

class Truck:
    def __init__(self, graph, master,  truck_id, start_time, driver, location, packages):
        self.truck_id = truck_id
        self.packages = packages
        self.stops = []
        self.driver = driver
        self.miles_driven = 0
        self._speed = 18
        self.package_map = HashMap(40)
        self.location = location
        self.current_stop = 0
        self.start_time = start_time
        self.graph = graph
        self.master = master
        self.package_list = []
        self.truck_time = self.start_time * 60

        for i in packages:
            self.master.get(i).status = "En-route"
            self.master.get(i).loaded_time = self.truck_time
            self.package_map.add(i, self.master.get(i))

        # self.package_map.print()

    def update_truck_time(self):
        self.truck_time = (self.start_time * 60) + (self.miles_driven/18 * 60)

    def get_vertices(self, graph, map):
        for item in self.packages:
            self.package_list.append((self.package_map.get(item).id, graph.address_to_number_list[map.get(item).address]))





    def deliver_specific_package(self, package):
        stop_num = None
        for i in range(0, len(self.package_list)):
            if self.package_list[i][0] == package:
                stop_num = self.package_list[i][1]
            else:
                continue


        coordinate = (self.current_stop, stop_num )
        distance = self.graph.edge_weights[coordinate]

        next_stop = stop_num

        self.package_map.get(package).status = "Delivered"
        self.package_list.remove((package, stop_num))
        self.miles_driven += distance
        self.update_truck_time()
        self.package_map.get(package).delivery_time = self.truck_time



        self.show_route_specs(distance, next_stop, package)

        self.current_stop = next_stop
        return

    def deliver_nearest_package(self):
        coordinate_list = [(self.current_stop, i[1]) for i in self.package_list]

        index = None
        distance = sys.maxsize
        for n in range(0,len(coordinate_list)):
            if self.graph.edge_weights[coordinate_list[n]] < distance:
                index = n
                distance = self.graph.edge_weights[coordinate_list[n]]
        next_stop = self.package_list[index][1]
        package = self.package_list[index][0]
        self.package_map.get(package).status = "Delivered"
        self.package_map.get(package).delivery_time = self.truck_time

        self.package_list.pop(index)
        self.miles_driven += distance
        self.update_truck_time()

        self.show_route_specs(distance, next_stop, package)

        self.current_stop = next_stop
        return


    def return_to_hub(self):
        # print(self.current_stop)
        distance = self.graph.edge_weights[(self.current_stop, 0)]
        self.miles_driven += distance
        self.update_truck_time()

        self.show_route_specs(distance,'Hub')

        self.current_stop = 0

    def show_route_specs(self, distance, stop, package = None):

        # print(f'Edge: {(self.current_stop,stop)}')
        # print(f'Distance: {distance}')
        # print(f'Next Stop: {stop}')
        # print(f'Package: {package}')
        # print(f'Total Miles Driven: {round(self.miles_driven, 1)}')
        # print("\n")
        return



