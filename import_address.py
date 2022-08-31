import csv
from Package import Package
from HashMap import HashMap
from graphs import *


def import_addresses(file, graph) -> str:
    with open(file, encoding='utf-8-sig') as package_file:
        readCSV = csv.reader(package_file, delimiter=',')
        route_graph = graph
        header = next(readCSV)
        # print(header)
        row_count = 0
        table = []
        for row in readCSV:

            route_graph.address_list[row[1].strip()] = row_count
            table.append(row)
            # print(row)
            route_graph.add_vertex(row_count)
            row_count += 1

        for r in range(0, len(table)):
            for i in range(2, len(table[r])):
                if table[r][i] != '' and float(table[r][i]) != 0 :
                    route_graph.add_undirected_edge(int(r), int(i-2), float(table[r][i]))


        return table[0][1]



















