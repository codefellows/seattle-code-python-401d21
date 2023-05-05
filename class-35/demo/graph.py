class Graph:

    def _init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        """
        add vertex
        Arguments: value
        Add a vertx to the graph
        :return: added vertex
        """
        new_vertex = Vertex(value)
        pass

    def add_edge(self, vertex1, vertex2):
        """
        add edge
        Arguments: 2 vertex to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two vertex in the graph
        If specified, assign a weight to the edge
        Both vertex should already be in the Graph
        :return:
        """
        pass

    def get_node(self):
        pass

    def get_neighbor(self):
        pass

    def size(self):
        pass

class Vertex:
    def __init(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight
