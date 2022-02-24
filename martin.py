from input import ProblemInput
from solution import Solution
from graph import GraphIG, GraphPyVis, GraphNx, GraphDot
import pandas as pd
import utils

inputData = ProblemInput("input/a_an_examplein.txt")

def score_projects(dict_projects, list_projects, time):
    """
    dict of all projects, list of projects available (names), current"""
    d = {'name': [], 'deadline': [], 'score': [], 'needed_contributors': []}

    for proj in list_projects:
        d['name'].append(dict_projects[proj].name)
        d['score'].append(dict_projects[proj].score)
        d['deadline'].append(dict_projects[proj].deadline)
        d['needed_contributors'].append(dict_projects[proj].needed_contributors)
    df = pd.DataFrame(d)
    #     df = df.sort_values(by=['best_before','points','duration'], ascending= [True,False,True])
    df['score_total'] = df.apply(
        lambda row: row['score'] - (time - row['deadline']) if time > row['deadline'] else row['score'], axis=1)
    df = df.sort_values(by=['score_total', 'needed_contributors'], ascending=[False, True])
    df = df[df['score_total'] > 0]
    if df.shape[0] > 0:
        return list(df['name'])

    return []


def make_assignation(projects_ordered):
    for project in projects_ordered:
        if inputData.assign_contributors(project) != None:
            return True
    return False

while len(inputData.remaining_projects) > 0:
    #  projects_ordered = list(inputData.remaining_projects) #.sort(key=lambda p: inputData.projects[p].score_if_now(inputData.time))
    projects_ordered = score_projects(inputData.projects, list(inputData.remaining_projects), inputData.time)
    while make_assignation(projects_ordered):
        pass

    if inputData.advance_time():
        break

inputData.save()
print(inputData.total_score)
