from import_address import *
from import_packages import *
from Truck import Truck


def main():

    h = HashMap(64)
    import_packages('WGUPS Package File.csv', h)
    # h.print()

    truck1 = Truck(1, 0, 'John', "HUB", [1,2,3,4,5,6,7,8,9,10])


    print(truck1.packages)


    g = Graph()
    import_addresses('WGUPS Distance Table.csv', g)

    truck1.get_vertices(g, h)
    # print(truck1.stops)

    while len(truck1.stops) > 0:
        truck1.move_to_next_stop(g)

    truck1.return_to_hub(g)

















if __name__ == '__main__':
    main()


