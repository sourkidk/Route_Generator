# Vertex class: used to build Graph class
# Source: Zybooks: Graphs in Python
class Vertex:
    def __init__(self, label):
        self.label = label

# This is a graph data structure built using python's built-in
# dictionaries, which are essentially hashmaps.  Hashmaps insert and
# lookup in O(1) so they are very efficient.  Of course, in most case
# iteration is necessary to access multiple possibilities which will
# increase time complexity.
class Graph:
    def __init__(self):
        self.address_to_number_list = {}
        self.number_to_address_list = {}
        self.adjacent_vertices = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacent_vertices[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
        self.edge_weights[(from_vertex, to_vertex)]  = weight
        self.adjacent_vertices[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight = 1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

