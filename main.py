
from import_address import *
from import_packages import *
from Truck import Truck
from route import *


def main():
    today = Route("Today", 'WGUPS Distance Table.csv', 'WGUPS Package File.csv')
    today.start_route()



if __name__ == '__main__':
    main()


