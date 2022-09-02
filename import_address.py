import csv
from Package import Package
from HashMap import HashMap
from graphs import *


def import_addresses(file, graph):
    with open(file, encoding='utf-8-sig') as package_file:
        readCSV = csv.reader(package_file, delimiter=',')
        header = next(readCSV)
        row_count = 0
        table = []
        for row in readCSV:

            graph.address_list[harmonize_directions(row[1].strip())] = row_count
            table.append(row)
            # print(row)
            graph.add_vertex(row_count)
            row_count += 1

        for r in range(0, len(table)):
            for i in range(2, len(table[r])):
                if table[r][i] != '':
                    graph.add_undirected_edge(int(r), int(i-2), float(table[r][i]))


def harmonize_directions(address)->str:
    directions = ['north', 'east', 'south', 'west', 'North', 'East', 'South', 'West']
    abbrev = ['N', 'E', 'S', 'W']
    for d in range(0, len(directions)):
        if directions[d] in address:
            # print("What!")
            print(str.replace(address, directions[d], abbrev[d%4]))

    return address
