from import_address import *
from import_packages import *
from Truck import Truck


def main():

    h = HashMap(64)
    import_packages('WGUPS Package File.csv', h)
    # h.print()

    truck1 = Truck(1, 0, 'John', "HUB", [1,2,3,4])


    print(truck1.packages)


    g = Graph()
    import_addresses('WGUPS Distance Table.csv', g)

    truck1.get_vertices(g, h)
    print(truck1.stops)

    s = truck1.stops
    coordinate_list = [(0, i) for i in s]
    print(coordinate_list)

    min_val, min_key = min((g.edge_weights[k], k) for k in coordinate_list)
    print(min_val)
    print(min_key)











if __name__ == '__main__':
    main()


