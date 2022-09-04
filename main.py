# WGU-PS C950 Project
# Keith Fletcher
# kflet87@wgu.edu
# ID: 009224586

from route import *
from util import *
# from sys

def main():
    print_introduction()

    today = Route("Today", 'WGUPS Distance Table.csv', 'WGUPS Package File.csv')
    today.start_route()

    state = True

    while state:
        print('******************************************')
        print('To check the status of all packages at a given time, enter a time in format HH:MM (ie. 13:50 for 1:50 PM)')
        requested_time = input('To exit, enter \'x\'...\n')
        if requested_time == 'x':
            state = False
        else:
            try:
                today.get_status(requested_time)
            except:
                print('The string you entered is not a valid time.  Please try again.')



    print("Exiting WGU-PS...")






if __name__ == '__main__':
    main()


