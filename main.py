import math

from import_address import *
from import_packages import *
from Truck import Truck
from datetime import *


def main():
    g = Graph()
    import_addresses('WGUPS Distance Table.csv', g)

    h = HashMap(40)
    import_packages('WGUPS Package File.csv', h)
    # h.print()
    # h.get()

    print(time_to_minutes('9:30'))
    print('>>>>>>>')




    # Truck 3 cannot leave until address is updated at 10:20 am
    h.get(9).address = h.get(5).address # address already in the system for another package
    # print(h.get(9).address)
    truck1 = Truck(g, h ,1 , 8,  'John', "HUB", [1,13,14,15,16,19,20,29,30,31,34,37,40])
    # h.print()
    # truck1.paesckage_map.print()
    truck2 = Truck(g, h ,2 , 9.1, 'Peter', "HUB", [3,6,18,25,26,27,32,33,36,35,38,39])
    truck3 = Truck(g, h ,3 , 10.5,  'John', "HUB", [2,4,5,7,8,9,10,11,12,17,21,22,23,24,28])

    # print(g.number_to_address_list)



    truck1.get_vertices(g, h)
    truck2.get_vertices(g,h)
    truck3.get_vertices(g,h)


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
    print(truck1.truck_time)
    print("-------------------")


    print(truck2.miles_driven)
    print(truck2.truck_time)
    print("-------------------")


    print(round(truck3.miles_driven, 2))
    print(truck3.truck_time)
    print('\n')




    print(f'Total Miles: {truck1.miles_driven + truck2.miles_driven + truck3.miles_driven}')

    # h.status(510)
    # h.print()

if __name__ == '__main__':
    main()


