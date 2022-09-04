# WGU-PS C950 Project
# Keith Fletcher
# kflet87@wgu.edu
# ID: 009224586

from route import *
from util import *

def main():
    # displays header infomation
    print_introduction()

    # Instantiates a route object with the appropriate package files and distance table
    today = Route("Today", 'WGUPS Distance Table.csv', 'WGUPS Package File.csv')

    # Most of the program logic exist inside the start_route method
    today.start_route()

    # This while loop runs the user interface.  It prompts the user to enter a time as input to check package states
    # as well as total mileage driven at that time.  The user can enter 'x' to end the program.
    state = True
    while state:
        print('******************************************')
        print('To check the status of all packages at a given time, enter a time in format HH:MM (ie. 13:50 for 1:50 PM)')
        requested_time = input('To exit, enter \'x\'...\n')
        if requested_time == 'x':
            state = False
        else:
            try:
                # Runs in O(n) as it's just iterating through the list and doing a single comparison
                today.get_status(requested_time)
            except:
                print('The string you entered is not a valid time.  Please try again.')



    print("Exiting WGU-PS...")






if __name__ == '__main__':
    main()


