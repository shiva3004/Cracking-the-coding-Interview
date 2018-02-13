from queue import Queue


class Graph:
    def __init__(self, val):
        self.nodes = [0] * val
        self.count = 0
        self.capacity = val

    def add_node(self, node):
        if self.capacity == self.count:
            raise Exception('Graph is full')
        self.nodes[self.count] = node
        self.count += 1

    def get_nodes(self):
        return self.nodes

    def __len__(self):
        return self.count + 1


class Node:
    def __init__(self, vertex, val):
        self.vertices_len = 0
        self.capacity = len
        self.vertices = [0] * val
        self.vertex = vertex
        self.is_visited = False

    def add_adjacency(self, node):
        if self.capacity == self.vertices_len:
            raise Exception('The node already has maximum elements')
        self.vertices[self.vertices_len] = node
        self.vertices_len += 1

    def get_vertex(self):
        return self.vertex

    def get_adjacency(self):
        return self.vertices

    def __len__(self):
        return self.vertices_len + 1


def create_graph():
    graph = Graph(6)
    graph_size = 6
    temp = [0] * graph_size  # create a list for nodes
    temp[0] = Node('A', 3)
    temp[1] = Node('B', 0)
    temp[2] = Node('C', 0)
    temp[3] = Node('D', 1)
    temp[4] = Node('E', 1)
    temp[5] = Node('F', 0)

    temp[0].add_adjacency(temp[1])  # connect the lists
    temp[0].add_adjacency(temp[2])
    temp[0].add_adjacency(temp[3])
    temp[3].add_adjacency(temp[4])
    temp[4].add_adjacency(temp[5])

    for each_node in temp:
        graph.add_node(each_node)

    return graph


def search_route(graph, start, end):
    if start is end:
        return True
    queue = Queue()
    queue.put(start)
    while queue.empty() is False:
        node = queue.get()
        if node.is_visited is not None:
            for each in node.get_adjacency():
                if each is end:
                    return True
                else:
                    queue.put(each)
            node.is_visited = True
    return False

# Create a graph


graph = create_graph()
nodes = graph.get_nodes()
start = nodes[4]
end = nodes[5]
print(search_route(graph, start, end))
