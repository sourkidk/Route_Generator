import csv
from Package import Package
from HashMap import HashMap


def import_packages(file, map):
    with open(file) as package_file:
        readCSV = csv.reader(package_file, delimiter=',')
        next(readCSV)
        package_names = ['a{i}' for i in range(40)]
        for row in readCSV:
            temp = []
            for i in range(0, len(row)):
                temp.append(row[i])


            # package_names[row - 1] = Package(id, address, city, state, zip, deadline, mass, notes)
            # map.add(id, Package(id, address, city, state, zip, deadline, mass, notes))




