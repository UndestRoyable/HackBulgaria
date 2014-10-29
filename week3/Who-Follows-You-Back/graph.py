class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self,node_a, node_b):
        if node_a not in self.graph:
            self.graph[node_a] = [node_b]
        elif (node_a in self.graph) and (node_b not in self.graph[node_a]):
            self.graph[node_a].append(node_b)

    def get_neighbours_for(self, node):
        return self.graph[node]

    def path_between(self, node_a, node_b):
        for neighbours in self.graph[node_a]:
            if neighbours in self.graph:
                if node_b in self.graph[neighbours]:
                    return True
        return False

    def to_str(self):
        for item in self.graph:
            return "{} ---> {}".format(item, self.get_neighbours_for(item))


