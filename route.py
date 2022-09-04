
from import_address import *
from import_packages import *
from Truck import Truck

class Route:
    def __init__(self, name, address_file, package_file):
        self.name = name
        self.location_graph = Graph()
        self.address_file = address_file
        self.package_file = package_file
        self.package_hash = HashMap(40)
        
        import_addresses(self.address_file, self.location_graph)
        import_packages(self.package_file, self.package_hash)





    def start_route(self):


        package_hash = HashMap(40)
        import_packages('WGUPS Package File.csv', package_hash)
        # package_hash.print()
        # package_hash.get()


        # Truck 3 cannot leave until address is updated at 10:20 am
        package_hash.get(9).address = package_hash.get(5).address # address already in the system for another package
        # print(package_hash.get(9).address)
        truck1 = Truck(self.location_graph, package_hash, 1, '8:00', 'John', "HUB", [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40])
        truck2 = Truck(self.location_graph, package_hash, 2, '9:06', 'Peter', "HUB", [3, 6, 18, 25, 26, 27, 32, 33, 36, 35, 38, 39])
        truck3 = Truck(self.location_graph, package_hash, 3, '10:3', 'John', "HUB", [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 28])

        truck1.get_vertices(self.location_graph, package_hash)
        truck2.get_vertices(self.location_graph, package_hash)
        truck3.get_vertices(self.location_graph, package_hash)


        truck1.deliver_specific_package(15)

        while len(truck1.package_list) > 0:
            truck1.deliver_nearest_package()

        truck1.return_to_hub()







        truck2.deliver_specific_package(25)
        truck2.deliver_specific_package(6)

        while len(truck2.package_list) > 0:
            truck2.deliver_nearest_package()

        truck2.return_to_hub()


        while len(truck3.package_list) > 0:
            truck3.deliver_nearest_package()

        truck3.return_to_hub()

        print(truck1.miles_driven)
        print(truck1.get_current_time())
        print("-------------------")


        print(truck2.miles_driven)
        print(truck2.get_current_time())
        print("-------------------")


        print(round(truck3.miles_driven, 2))
        print(truck3.get_current_time())
        print('\n')

        print(f'Total Miles: {truck1.miles_driven + truck2.miles_driven + truck3.miles_driven}')

        # print(truck1.truck_times)
        # print(truck1.get_mileage_at_time(540))
        # package_hash.status(510)
        # package_hash.print()