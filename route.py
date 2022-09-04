
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
        self.trucks = []
        
        import_addresses(self.address_file, self.location_graph)
        import_packages(self.package_file, self.package_hash)

    def get_status(self, time):
        mileage = 0
        for truck in self.trucks:
            mileage += truck.get_mileage_at_time(time)

        print(f'Total mileage by all trucks at {time} : {round(mileage,2)}\n')
        self.package_hash.status(time)
        print(f'Total mileage by all trucks at {time} : {round(mileage,2)}\n')

        return








    def start_route(self):


        package_hash = HashMap(40)
        import_packages('WGUPS Package File.csv', package_hash)
        # package_hash.print()
        # package_hash.get()


        # Truck 3 cannot leave until address is updated at 10:20 am
        package_hash.get(9).address = package_hash.get(5).address # address already in the system for another package

        truck1 = Truck(self.location_graph, self.package_hash, 1, '8:00', 'John', "HUB", [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40])
        truck2 = Truck(self.location_graph, self.package_hash, 2, '9:06', 'Peter', "HUB", [3, 6, 18, 25, 26, 27, 32, 33, 36, 35, 38, 39])
        truck3 = Truck(self.location_graph, self.package_hash, 3, '10:21', 'John', "HUB", [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 28])

        self.trucks.append(truck1)
        self.trucks.append(truck2)
        self.trucks.append(truck3)





        truck1.dispatch_truck([15])
        truck2.dispatch_truck([25,6])
        truck3.dispatch_truck()


        total = 0
        for truck in self.trucks:
            total += truck.miles_driven
        print('Route Results:')
        print('All Packages Delivered')
        print(f'Total Miles: {total}')
        print('-------------------------')

        # test = truck1.get_mileage_at_time('9:30')
        # print(f'Miles Driven: {test}')

        # print(truck1.truck_times)
        # print(truck1.get_mileage_at_time(540))
