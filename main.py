
from HashMap import HashMap
from Package import Package
from import_packages import *
from import_address import *
from Truck import Truck

def main():

    h = HashMap(64)
    import_packages('WGUPS Package File.csv', h)
    # h.print()
    # print(h.get(1))




    # print(h.get(1).address)

    # print(hash(h.get(1).address))

    # print(h.get(2).address)
    # print(h.get(3).address)
    # print(h.get(4).address)
    # print(h.get(5).address)
    # print(h.get(6).address)

    # truck1 = Truck(1, 0, 'John', 0, "HUB")

    address_to_compare = import_addresses('WGUPS Distance Table.csv').strip()

    print(address_to_compare)
    print(h.get(address_to_compare))
    # print(hash(address_to_compare))
    # concat_address = h.get(1).address + "\n(" + str(h.get(1).zip) + ")"
    concat_address = h.get(address_to_compare)

    # print(concat_address)
    # print(hash(concat_address))

    # Compare strings char by char
    # for i in range(0, len(concat_address)):
    #     print(concat_address[i] + " ")
    #     print(hex(id(concat_address[i])))
    #     print(address_to_compare[i] + " ")
    #     print(hex(id(address_to_compare[i])))
    #     print("\n")


    # print(address_to_compare is concat_address)
    # print(address_to_compare.__eq__(concat_address))
    # print(address_to_compare == concat_address)








if __name__ == '__main__':
    main()


