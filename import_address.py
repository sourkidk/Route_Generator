import csv
from Package import Package
from HashMap import HashMap
from Graph import *


def import_addresses(file):
    with open(file, encoding='utf-8-sig') as package_file:
        readCSV = csv.reader(package_file, delimiter=',')
        graph = Graph()
        # names = [f'a{i}' for i in range(1, 25)]
        # row_count = 0
        header = next(readCSV)
        # print(header)
        row_count = 0
        table = []
        for row in readCSV:
            temp = row
            table.append(row)
            # print(row)
            graph.add_vertex(Vertex(str(row_count)))
            row_count += 1


        print(graph.adjacency_list)
        print(graph.adjacency_list.keys())


        # for r in range(0, len(table)):
        #     for i in range(2, len(table[r])):
        #         if table[r][i] != '':
        #             graph.add_undirected_edge(str(r), str(i-2), table[r][i])

        print(graph.adjacency_list)


















