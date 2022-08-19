import csv
from Package import Package
from HashMap import HashMap


def import_addresses(file):
    with open(file) as package_file:
        readCSV = csv.reader(package_file, delimiter=',')
        next(readCSV)
        package_names = ['a{i}' for i in range(40)]
        matrix = []
        for row in readCSV:
            temp = []
            for i in range(0, len(row)):
                temp.append(row[i])
            matrix.append(temp)

        print(matrix)





            # package_names[row - 1] = Package(id, address, city, state, zip, deadline, mass, notes)
            # map.add(id, Package(id, address, city, state, zip, deadline, mass, notes))




