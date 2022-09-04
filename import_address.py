import csv
from Package import Package
from HashMap import HashMap
from graphs import *
from util import *

# function to import addresses
def import_addresses(file, graph):
    with open(file, encoding='utf-8-sig') as package_file:
        readCSV = csv.reader(package_file, delimiter=',')
        header = next(readCSV)
        row_count = 0
        table = []

        # This section adding the address to a dictionary runs in O(n)
        for row in readCSV:
            graph.address_to_number_list[harmonize_directions(row[1].strip())] = row_count
            graph.number_to_address_list[row_count] = harmonize_directions(row[1].strip())
            table.append(row)
            graph.add_vertex(row_count)
            row_count += 1

        # This portion adding the edges and their weights will run in O(n^2)
        for r in range(0, len(table)):
            for i in range(2, len(table[r])):
                if table[r][i] != '':
                    graph.add_undirected_edge(int(r), int(i-2), float(table[r][i]))



