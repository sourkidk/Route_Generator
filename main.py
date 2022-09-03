import math

from import_address import *
from import_packages import *
from Truck import Truck
from datetime import *


def main():
    g = Graph()
    import_addresses('WGUPS Distance Table.csv', g)

    h = HashMap(64)
    import_packages('WGUPS Package File.csv', h)
    # h.print()
    # h.get()



    # Truck 3 cannot leave until address is updated at 10:20 am
    h.get(9).address = h.get(5).address # address already in the system for another package
    # print(h.get(9).address)
    truck1 = Truck(g, h ,1 , 8,  'John', "HUB", [1,13,14,15,16,19,20,29,30,31,34,37,40])
    # truck2 = Truck(g, h ,2 , 9.1, 'Peter', "HUB", [3,6,18,25,26,27,32,33,36,35,38,39])
    # truck3 = Truck(g, h ,3 , 10.5,  'John', "HUB", [2,4,5,7,8,9,10,11,12,17,21,22,23,24,28])

    # print(g.address_list)



    truck1.get_vertices(g, h)
    # truck2.get_vertices(g,h)
    # truck3.get_vertices(g,h)

    while len(truck1.map) > 0:
        truck1.find_next_package()



    # truck1.move_to_nearest_stop(g)

    # truck1.move_to_specific_stop(g, 21)

    # while len(truck1.stops) > 0:
    #     truck1.move_to_nearest_stop(g)
    #
    # truck1.return_to_hub(g)



    # truck2.move_to_specific_stop(g, 24)
    # truck2.move_to_specific_stop(g, 13)
    #
    # while len(truck2.stops) > 0:
    #     truck2.move_to_nearest_stop(g)
    #
    # truck2.return_to_hub(g)
    #
    #
    # # truck3.move_to_specific_stop(g, 13)
    #
    # while len(truck3.stops) > 0:
    #     truck3.move_to_nearest_stop(g)
    #
    # truck3.return_to_hub(g)
    #
    #
    #
    truck1_endtime = ((truck1.start_time * 60) + (truck1.miles_driven/18 * 60))
    print(time_formatting(truck1_endtime))
    #
    # truck2_endtime = ((truck2.start_time * 60) + (truck2.miles_driven/18 * 60))
    # print(time_formatting(truck2_endtime))
    #
    # truck3_endtime = ((truck3.start_time * 60) + (truck3.miles_driven/18 * 60))
    # print(time_formatting(truck3_endtime))
    # print('\n')
    #
    # print(f'Total Miles: {truck1.miles_driven + truck2.miles_driven + truck3.miles_driven}')
    # minutes = 645
    # print(f'{int(minutes / 60)}:{(int(minutes) % 60):02}')

if __name__ == '__main__':
    main()


