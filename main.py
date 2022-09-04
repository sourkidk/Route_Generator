# WGU-PS C950 Project
# Keith Fletcher
# kflet87@wgu.edu
# ID: 009224586

from route import *

def main():
    today = Route("Today", 'WGUPS Distance Table.csv', 'WGUPS Package File.csv')
    today.start_route()

    # today.package_hash.status(540)
    # today.package_hash.print()



if __name__ == '__main__':
    main()


