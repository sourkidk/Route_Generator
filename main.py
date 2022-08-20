
from HashMap import HashMap
from Package import Package
from import_packages import *
from import_address import *
from Truck import Truck

def main():

    h = HashMap(64)
    import_packages('WGUPS Package File.csv', h)
    # h.print()

    # print(h.get(1).address)
    # print(h.get(2).address)
    # print(h.get(3).address)
    # print(h.get(4).address)
    # print(h.get(5).address)
    # print(h.get(6).address)

    truck1 = Truck(1, 0, 0, 'John', 0)

    import_addresses('WGUPS Distance Table.csv')






if __name__ == '__main__':
    main()


