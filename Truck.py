from HashMap import HashMap
from graphs import *
from datetime import *
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
        self.pack_map = HashMap(16)
        self.location = location
        self.current_stop = 0
        self.start_time = start_time
        self.graph = graph
        self.master = master
        self.map = []

        for i in packages:
            self.pack_map.add(i, self.master.get(i))

        # self.pack_map.print()



    def get_vertices(self, graph, map):
        for item in self.packages:
            self.stops.append(graph.address_to_number_list[map.get(item).address])
            self.map.append((self.pack_map.get(item).id, graph.address_to_number_list[map.get(item).address]))
        print(self.map)
        print(self.stops)




    def deliver_specific_package(self, package):
        stop_num = None
        for i in range(0, len(self.map)):
            if self.map[i][0] == package:
                stop_num = self.map[i][1]
            else:
                continue


        coordinate = (self.current_stop, stop_num )
        distance = self.graph.edge_weights[coordinate]


        index = stop_num

        print(coordinate)
        print(distance)
        next_stop = stop_num

        print(f'Package: {package}')
        self.pack_map.get(package).status = "Delivered"
        self.map.remove((package,stop_num))
        self.miles_driven += distance
        self.current_stop = next_stop

        self.show_route_specs(distance, next_stop)
        return





    def deliver_nearest_package(self):
        coordinate_list = [(self.current_stop, i[1]) for i in self.map]
        # print(coordinate_list)

        index = None
        distance = sys.maxsize
        for n in range(0,len(coordinate_list)):
            if self.graph.edge_weights[coordinate_list[n]] < distance:
                index = n
                distance = self.graph.edge_weights[coordinate_list[n]]
        print(coordinate_list[index])
        print(distance)
        next_stop = self.map[index][1]

        print(f'Package: {self.map[index][0]}')
        self.pack_map.get(self.map[index][0]).status = "Delivered"
        self.map.pop(index)
        self.miles_driven += distance
        self.current_stop = next_stop

        self.show_route_specs(distance, next_stop)
        return









    def return_to_hub(self):
        # print(self.current_stop)
        distance = self.graph.edge_weights[(self.current_stop, 0)]
        self.miles_driven += distance
        self.current_stop = 0

        self.show_route_specs(distance,'Hub')


    def show_route_specs(self, distance, stop):
        print(f'Distance: {distance}')
        print(f'Next Stop: {stop}')
        print(f'Total Miles Driven: {round(self.miles_driven, 1)}')
        print("\n")
        return



