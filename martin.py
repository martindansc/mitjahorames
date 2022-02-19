from input import ProblemInput
from solution import Solution
from graph import GraphIG, GraphPyVis
import utils
inputData = ProblemInput("input/d_difficult.in.txt")

# graph1 = GraphPyVis()
# graph1.gDict(inputData.clients_to_like, 'blue')
# graph1.gDict(inputData.clients_to_dislikes, 'red')
# graph1.plot()

# graph1 = GraphIG()
# graph1.gDict(inputData.clients_to_like, 'blue')
# graph1.gDict(inputData.clients_to_dislikes, 'red')
# graph1.plot()

# graph2 = GraphPyVis()
# graph2.gDic2(inputData.clients_to_like, inputData.like_to_clients, 'blue')
# graph2.gDic2(inputData.clients_to_dislikes, inputData.dislike_to_clients, 'red')
# graph2.plot()

# graph3 = GraphPyVis()
# graph3.gDict(inputData.incompatible_clients)
# graph3.plot()

(id, degree) = utils.get_max_from_dict_of_lists(inputData.incompatible_clients)
while degree > 0:
    utils.remove_from_dict(inputData.incompatible_clients, id)
    (id, degree) = utils.get_max_from_dict_of_lists(inputData.incompatible_clients)

solution = Solution(inputData)
for i in inputData.incompatible_clients:
    solution.add_customer(i)

print(solution.value())
print(solution.to_string())
solution.save()