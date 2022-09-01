import math

from import_address import *
from import_packages import *
from Truck import Truck


def main():

    h = HashMap(64)
    import_packages('WGUPS Package File.csv', h)
    # h.print()

    p = [i for i in range(1,41)]

    truck1 = Truck(1, 0, 'John', "HUB", [1,2,3,4,5,6])


    print(truck1.packages)


    g = Graph()
    import_addresses('WGUPS Distance Table.csv', g)

    truck1.get_vertices(g, h)
    # print(truck1.stops)

    while len(truck1.stops) > 0:
        truck1.move_to_next_stop(g)

    truck1.return_to_hub(g)

    stuff = ((8*60) + (truck1.miles_driven/18 * 60))
    print(f'{math.floor(stuff/60)}:{round(stuff % 60)}')



















if __name__ == '__main__':
    main()


