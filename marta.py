from input import ProblemInput
import pandas as pd

# def choose_contrib(contributors,skill,level):
#     #choose contributor with less skills and level that fulfills the job
#     #dict of contributors, name skill, level skill (int)
#
#     contributor_dict  = {'name':[],'skill':[],'level':[],'total_skills':[]}
#     for contr in contributors.keys():
#         if skill in contributors[contr].skills.keys():
#             contributor_dict['name'].append(contributors[contr].name)
#             contributor_dict['level'].append(eval(contributors[contr].skills[skill]))
#             contributor_dict['skill'].append(skill)
#             contributor_dict['total_skills'].append(len(contributors[contr].skills.keys()))
#     df = pd.DataFrame(contributor_dict)
#     df = df[df['level']>=level]
#     df.sort_values(by= ['level','total_skills'],ascending=[True,True])
#     if df.shape[0]>0:
#         return df['name'].iloc[0]
#     return None


def score_projects(dict_projects, list_projects, time):
    """
    dict of all projects, list of projects available (names), current"""
    d = {'name': [], 'deadline': [], 'score': [], 'needed_contributors': []}

    for proj in list_projects:
        d['name'].append(dict_projects[proj].name)
        d['score'].append(dict_projects[proj].score)
        d['deadline'].append(int(dict_projects[proj].deadline))
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



# inputData = ProblemInput("input/a_an_example.in.txt")
# inputData = ProblemInput("input/b_better_start_small.in.txt")
# inputData = ProblemInput("input/c_collaboration.in.txt")
inputData = ProblemInput("input/d_dense_schedule.in.txt")

# inputData = ProblemInput("input/e_exceptional_skills.in.txt")
# inputData = ProblemInput("input/f_find_great_mentors.in.txt")



list_projects = score_projects(inputData.projects, list(inputData.projects.keys()), inputData.time)
while len(list_projects):
    remaining_projects = []
    for i in range(len(list_projects)):
        inputData.assign_contributors(list_projects[i])

    if inputData.advance_time() is False:
        break
    if len(inputData.remaining_projects) == 0:
        break
    list_projects = score_projects(inputData.projects, inputData.remaining_projects, inputData.time)
print(inputData.total_score)

#WRITE OUTPUT
with open('test_d_hash.txt','w') as f:
    f.write(str(len(inputData.final_order_2))+'\n')
    for project in inputData.final_order_2:
        s =' '.join(inputData.projects[project].contributors.values())
        f.write(project+'\n')
        f.write(s+'\n')
# inputData.save()