import csv
from Package import Package
from HashMap import HashMap
from graphs import *


def import_addresses(file, graph) -> str:
    with open(file, encoding='utf-8-sig') as package_file:
        readCSV = csv.reader(package_file, delimiter=',')
        header = next(readCSV)
        row_count = 0
        table = []
        for row in readCSV:

            graph.address_list[row[1].strip()] = row_count
            table.append(row)
            # print(row)
            graph.add_vertex(row_count)
            row_count += 1

        for r in range(0, len(table)):
            for i in range(2, len(table[r])):
                if table[r][i] != '':
                    graph.add_undirected_edge(int(r), int(i-2), float(table[r][i]))

        # for r in range(0, len(table)):
        #     for i in range(2, len(table[r])):
        #         if table[r][i] != '' and float(table[r][i]) != 0 :
        #             graph.add_undirected_edge(int(r), int(i-2), float(table[r][i]))


        return table[0][1]



















