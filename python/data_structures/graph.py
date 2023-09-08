class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            raise KeyError("One or both vertices not found in the graph")

        edge = Edge(end_vertex, weight)
        self.adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        return list(self.adjacency_list.keys())

    def get_neighbors(self, vertex):
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]
        else:
            return []

    def size(self):
        return len(self.adjacency_list)


class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight
