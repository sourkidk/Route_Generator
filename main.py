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
        print('Menu:')
        print('Get the status of all packages >>> Type \'all\'')
        print('Get a single package status >>> Type \'any\'')
        menu_selection = input('To exit, enter \'x\'...\n')

        try:
            if menu_selection.lower() == 'x':
                state = False
                break

            elif menu_selection.lower() == 'all':
                try:
                    time_entry = input('To check the status of all packages at a given time, enter a time in format HH:MM (ie. 13:50 for 1:50 PM)\n')
                    # Runs in O(n) as it's just iterating through the list and doing a single comparison
                    today.get_status(time_entry)
                except:
                    print('The string you entered is not a valid time.  Please try again.')
            elif menu_selection.lower() == 'any':
                package_entry = int(input('Enter the integer id number for a package to view its status...(i.e. 5 for package 5 )\n'))
                try:
                    single_package_time = input('To check the status of this packages at a given time, enter a time in format HH:MM (ie. 13:50 for 1:50 PM)\n')
                    # Runs in 0(1) as it's effectively a lookup with function call.
                    today.package_hash.lookup(package_entry).get_status(single_package_time)
                except:
                    print('The string you entered is not a valid time.  Please try again.')
            else:
                print("Try Again")




        except:
            print('The string you entered is not a valid selection.  Please try again.')

    print("Exiting WGU-PS...")


if __name__ == '__main__':
    main()


