from input import ProblemInput
from solution import Solution
from graph import GraphIG, GraphPyVis, GraphNx, GraphDot
import utils

inputData = ProblemInput("input/b_better_start_small.in.txt")


def make_assignation(projects_ordered):
    for project in projects_ordered:
        if inputData.assign_contributors(project) != None:
            return True
    return False

while len(inputData.remaining_projects) > 0:
    projects_ordered = list(inputData.remaining_projects) #.sort(key=lambda p: inputData.projects[p].score_if_now(inputData.time))
    while make_assignation(projects_ordered):
        pass

    if inputData.advance_time():
        break

inputData.save()
print(inputData.total_score)
