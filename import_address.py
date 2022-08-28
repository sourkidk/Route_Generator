import csv
from Package import Package
from HashMap import HashMap
from graphs import *


def import_addresses(file):
    with open(file, encoding='utf-8-sig') as package_file:
        readCSV = csv.reader(package_file, delimiter=',')
        paper = Graph()
        # names = [f'a{i}' for i in range(1, 25)]
        header = next(readCSV)
        print(header)
        row_count = 0
        table = []
        for row in readCSV:
            temp = row
            table.append(row)
            # print(row)
            paper.add_vertex(row_count)
            row_count += 1

        for r in range(0, len(table)):
            for i in range(2, len(table[r])):
                if table[r][i] != '':
                    paper.add_undirected_edge(int(r), int(i-2), float(table[r][i]))


        print(paper.adjacency_list)
        print(paper.edge_weights)


















