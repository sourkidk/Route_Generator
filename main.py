from import_address import *
from import_packages import *
from Truck import Truck


def main():

    h = HashMap(64)
    import_packages('WGUPS Package File.csv', h)
    h.print()

    truck1 = Truck(1, 0, 'John', 0, "HUB")
    truck1.packages.append(h.get('2010 W 500 S\n(84104)'))
    truck1.packages.append(h.get('4580 S 2300 E\n(84117)'))
    truck1.packages.append(h.get('3595 Main St\n(84115)'))
    truck1.packages.append(h.get('410 S State St\n(84111)'))
    print(truck1.packages)


    g = Graph()
    address_to_compare = import_addresses('WGUPS Distance Table.csv', g).strip()

    print(address_to_compare)
    print(h.get(address_to_compare))









if __name__ == '__main__':
    main()


