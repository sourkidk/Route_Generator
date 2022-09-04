import csv
from Package import Package
from util import *

# function to import packages into HashMap.  Runs in 0(n)
def import_packages(file, map):
    with open(file) as package_file:
        readCSV = csv.reader(package_file, delimiter=',')
        next(readCSV)
        for row in readCSV:
            if row[0] == "":
                break
            id = int(row[0])
            # address is concatenated with zip in the same format as the address file to aid with searching
            address = harmonize_directions(row[1]) + "\n(" + row[4] + ")"
            city = row[2]
            state = row[3]
            zip = row[4]
            deadline = row[5]
            mass = int(row[6])
            notes = row[7]

            map.add(id, Package(id, address, city, state, zip, deadline, mass, notes))




