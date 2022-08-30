import csv
from Package import Package
from HashMap import HashMap
from graphs import *


def import_addresses(file, graph) -> str:
    with open(file, encoding='utf-8-sig') as package_file:
        readCSV = csv.reader(package_file, delimiter=',')
        route_graph = graph
        # names = [f'a{i}' for i in range(1, 25)]
        header = next(readCSV)
        # print(header)
        row_count = 0
        table = []
        for row in readCSV:
            table.append(row)
            # print(row)
            route_graph.add_vertex(row_count)
            row_count += 1

        for r in range(0, len(table)):
            for i in range(2, len(table[r])):
                if table[r][i] != '' and float(table[r][i]) != 0 :
                    route_graph.add_undirected_edge(int(r), int(i-2), float(table[r][i]))


        # for row in table:
        #     print(row)
        # print(route_graph.adjacency_list)
        # print(route_graph.edge_weights)
        print(table[0])
        print(table[6])
        print(table[17])
        print(table[21])



        # s = route_graph.adjacency_list[0]
        s = [6]
        print(s)
        coordinate_list = [(21, i) for i in s]
        print(coordinate_list)



        min_val, min_key = min((route_graph.edge_weights[k], k) for k in coordinate_list)
        print(min_val)
        print(min_key)

        return table[0][1]



















