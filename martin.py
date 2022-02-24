from input import ProblemInput
from solution import Solution
from graph import GraphIG, GraphPyVis, GraphNx, GraphDot
import utils

inputData = ProblemInput("input/a_an_example.in.txt")

def make_assignation(projects_ordered):
    next_project = projects_ordered.pop(1)
    return inputData.assign_contributors(next_project) != None

while len(inputData.remaining_projects) > 0:
    projects_ordered = list(inputData.remaining_projects) #.sort(key=lambda p: inputData.projects[p].score_if_now(inputData.time))
    while make_assignation(projects_ordered):
        pass

    inputData.advance_time()
