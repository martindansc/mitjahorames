from tkinter import FALSE
from pyvis.network import Network
import igraph

class Graph:
    def __init__(self):
        pass

    def add_node(self, node, color):
        raise NotImplementedError

    def add_edge(self, node, color):
        raise NotImplementedError

    def plot(self):
        raise NotImplementedError

    def gDict(self, dictList, diff_color = False, color="blue"):
        for (key, l) in dictList.items():
            self.add_node(key, "blue")
            for value in l:
                self.add_node(value, 'red')
                self.add_edge(key, value, color)

    def gDic2(self, dictList, dictListSuport, color="blue"):
        for (key, l) in dictList.items():
            self.add_node(key, 'blue')
            print('1 - ' + str(key))
        
        for (key, l) in dictList.items():
            print('2 - ' + str(key))
            for bridge in l:
                for value in dictListSuport[bridge]:
                    if value != key: 
                        self.add_edge(key, value, color)

class GraphPyVis(Graph):
    def __init__(self, notebook=False):
        super().__init__()
        self.notebook = notebook
        self.net = Network(width="70vw", height="70vh", notebook=notebook)

    def add_node(self, node, group):
        self.net.add_node(node, group=group)


    def add_edge(self, node1, node2, color="blue"):
        self.net.add_edge(node1, node2, color=color)

    def plot(self):
        if(not self.notebook):
            self.net.show_buttons(filter_=['manipulation', 'physics', 'interaction', 'layout'])
        self.net.show('graph.html')

class GraphIG(Graph):
    def __init__(self):
        super().__init__()
        self.G = igraph.Graph()
        self.first = True

    def add_node(self, node, color):
        node = str(node)
        if self.first or len(self.G.vs.select(name=node)) == 0:
            self.first = False
            gNode = self.G.add_vertex(node)
            gNode["label"] = node
            gNode["color"] = color
            

    def add_edge(self, node1, node2, color="blue"):
        node1 = str(node1)
        node2 = str(node2)
        self.G.add_edges([(node1, node2)])

    def plot(self):
        igraph.summary(self.G)
        igraph.plot(self.G, bbox = (2000, 2000))

    def get_max_degree_vertex(self):
        print(self.G.maxdegree())
        return (0, 0)

    def remove_vertex(self, vertex):
        return 0