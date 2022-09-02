import math

from import_address import *
from import_packages import *
from Truck import Truck


def main():

    h = HashMap(64)
    import_packages('WGUPS Package File.csv', h)
    # h.print()
    # h.get()

    p = [i for i in range(1,41)]

    truck1 = Truck(1, 0, 8,  'John', "HUB", [1,6,13,14,15,16,20 ,29,30,31,34,37,40])
    truck2 = Truck(2, 0, 9, 'John', "HUB", [])
    truck3 = Truck(3, 0,10,  'John', "HUB", [])


    print(truck1.packages)


    g = Graph()
    import_addresses('WGUPS Distance Table.csv', g)

    print(g.address_list)

    # truck1.get_vertices(g, h)
    # # print(truck1.stops)
    #
    # while len(truck1.stops) > 0:
    #     truck1.move_to_next_stop(g)
    #
    # truck1.return_to_hub(g)
    #
    # stuff = ((truck1.start_time * 60) + (truck1.miles_driven/18 * 60))
    # print(f'{math.floor(stuff/60)}:{round(stuff % 60)}')



















if __name__ == '__main__':
    main()


