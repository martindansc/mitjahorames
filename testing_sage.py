from input import ProblemInput
from solution import Solution
import utils
import json
inputData = ProblemInput("input/e_elaborate.in.txt")
#create graph

# nodes =  # number
# edges = # (i,j) pairs
# g = Graph(nodes)
# g.add_edges(edges)

#

d = inputData.incompatible_clients
with open('graph.json','w') as f:
    json.dump(d,f)

