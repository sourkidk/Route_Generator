from HashMap import HashMap
from util import *
import sys

# Truck class: Much of the program logic is housed in this class. The Nearest Neighbor Algorithm
# which is the solution used for the routing problem runs in the 'deliver_nearest_package' function.
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
        self.start_time = time_to_minutes(start_time)
        self.graph = graph
        self.master = master
        self.package_list = []
        self.current_time = self.start_time
        self.truck_times = []

        for i in packages:
            self.master.lookup(i).status = "En-route"
            self.master.lookup(i).loaded_time = self.current_time
            self.package_map.insert(i, self.master.lookup(i))

    # Method to assist with tracking time consumption throughout the route.
    def update_truck_time(self):
        temp = round((self.start_time + (self.miles_driven/18 * 60)),2)
        self.current_time = temp
        self.truck_times.append((temp, self.miles_driven))

    # Returns time in HH:mm format
    def get_current_time(self):
        return minutes_to_time(self.current_time)

    # This method is used to convert the package_list into a list of tuples with package id and address id.
    def get_vertices(self):
        for item in self.packages:
            self.package_list.append((self.package_map.lookup(item).id, self.graph.address_to_number_list[self.master.lookup(item).address]))

    # Displays stats for routes
    def display_route_stats(self):
        print(f'Truck {self.truck_id} - {round(self.miles_driven, 2)} miles driven')
        print(f'Route completed at {self.get_current_time()}')
        print("-------------------")

    # This method calls the various methods that move the truck through its route
    def dispatch_truck(self, priority_stops=None):
        self.get_vertices()
        if priority_stops != None:
            for item in priority_stops:
                self.deliver_specific_package(item)
        else:
            pass
        while len(self.package_list) > 0:
            self.deliver_nearest_package()

        self.return_to_hub()
        self.display_route_stats()


    # This method is used to calculate the miles traveled by a truck at a given input time.
    def get_mileage_at_time(self, time):
        minutes = time_to_minutes(time)
        # print(minutes)
        if minutes < self.start_time:
            return 0
        elif minutes > self.current_time:
            return self.miles_driven
        else:
            return ((minutes - self.start_time)/60 * 18)


    # This method is used to 'deliver' a high priority package.  It runs in O(n) as it much iterate through
    # the list of packages on the truck if the size increases.  If the size of the truck is fixed, then
    # it basically reduces to O(1)
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

        self.package_map.lookup(package).status = "Delivered"
        self.package_list.remove((package, stop_num))
        self.miles_driven += distance
        self.update_truck_time()
        self.package_map.lookup(package).delivery_time = self.current_time

        self.show_route_specs(distance, next_stop, package)

        self.current_stop = next_stop
        return


    # Nearest Neigbor algorithm: Runs in O(logn) as the number of comparison decreases as the list of edges is
    # reduced.  All functionality for updating the package and the truck are also housed in the 'deliver...' methods.
    # Could reduce repetitive code by aggregating those actions into an additional method and calling it in the
    # various places
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
        self.package_map.lookup(package).status = "Delivered"
        self.package_map.lookup(package).delivery_time = self.current_time

        self.package_list.pop(index)
        self.miles_driven += distance
        self.update_truck_time()

        self.show_route_specs(distance, next_stop, package)

        self.current_stop = next_stop
        return

    # Return to hub runs in O(1) as it just has to lookup the edge weight associated with
    # the last stop and then update the truck attributes.
    def return_to_hub(self):
        # print(self.current_stop)
        distance = self.graph.edge_weights[(self.current_stop, 0)]
        self.miles_driven += distance
        self.update_truck_time()
        self.show_route_specs(distance,'Hub')
        self.current_stop = 0

    # This was a helper method used to display additional information as the route progressed.
    def show_route_specs(self, distance, stop, package = None):
        # print(f'Truck #: {self.truck_id}')
        # print(f'Edge: {(self.current_stop,stop)}')
        # print(f'Distance: {distance}')
        # print(f'Next Stop: {stop}')
        # print(f'Package: {package}')
        # print(f'Total Miles Driven: {round(self.miles_driven, 1)}')
        # print(f'Time:  {minutes_to_time(self.current_time)}')
        # print("\n")
        return



