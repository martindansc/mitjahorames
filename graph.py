from tkinter import FALSE
from pyvis.network import Network
import matplotlib.pyplot as plt
import networkx as nx
import igraph

class Graph:
    def __init__(self):
        self.nodes = set()

    def _add_node(self, node):
        self.nodes.add(node)

    def _node_exists(self, node):
        return node in self.nodes

    def add_node(self, node, color):
        raise NotImplementedError

    def add_edge(self, node, color):
        raise NotImplementedError

    def plot(self):
        raise NotImplementedError

    def gDict(self, dictList, color="blue"):
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
        super()._add_node(node)
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
        self._add_node(node)
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
        layout = self.G.layout("lgl")
        igraph.plot(self.G, layout=layout)


class GraphPyVis(Graph):
    def __init__(self, notebook=False):
        super().__init__()
        self.notebook = notebook
        self.net = Network(width="70vw", height="70vh", notebook=notebook)

    def add_node(self, node, group):
        self.net.add_node(node, group=group)
        self._add_node(node)

    def add_edge(self, node1, node2, color="blue"):
        self.net.add_edge(node1, node2, color=color)

    def plot(self):
        if(not self.notebook):
            self.net.show_buttons(filter_=['manipulation', 'physics', 'interaction', 'layout'])
        self.net.show('graph.html')

class GraphNx(Graph):
    def __init__(self):
        super().__init__()
        self.G = nx.Graph()
        self.first = True

    def add_node(self, node, color):
        node = str(node)
        if not self._node_exists(node):
            self.G.add_node(node, color=color)
            self._add_node(node)
            
    def add_edge(self, node1, node2, color="blue"):
        node1 = str(node1)
        node2 = str(node2)
        self.G.add_edge(node1, node2, color=color)

    def plot(self):
        nx.draw(self.G, with_labels=True, font_weight='bold')
        plt.show()

    def toGephi(self):
        nx.write_gexf(self.G, "./outputs/graph.gexf")


class GraphDot(GraphNx):
    
    def plot(self):
        graph = nx.drawing.nx_pydot.to_pydot(self.G)
        graph.write_svg('./outputs/graph.svg')
