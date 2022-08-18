import csv
from Package import Package
from HashMap import HashMap


def import_packages(file, map):
    with open(file) as package_file:
        readCSV = csv.reader(package_file, delimiter=',')
        next(readCSV)
        package_names = ['a{i}' for i in range(40)]
        for row in readCSV:
            if row[0] == "":
                break
            id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            deadline = row[5]
            mass = int(row[6])
            notes = row[7]

            map.add(id, Package(id, address, city, state, zip, deadline, mass, notes))




