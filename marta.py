import pandas as pd

def choose_contrib(contributors,skill,level):
    #choose contributor with less skills and level that fulfills the job
    #dict of contributors, name skill, level skill (int)

    contributor_dict  = {'name':[],'skill':[],'level':[],'total_skills':[]}
    for contr in contributors.keys():
        if skill in contributors[contr].skills.keys():
            contributor_dict['name'].append(contributors[contr].name)
            contributor_dict['level'].append(eval(contributors[contr].skills[skill]))
            contributor_dict['skill'].append(skill)
            contributor_dict['total_skills'].append(len(contributors[contr].skills.keys()))
    df = pd.DataFrame(contributor_dict)
    df = df[df['level']>=level]
    df.sort_values(by= ['level','total_skills'],ascending=[True,True])
    if df.shape[0]>0:
        return df['name'].iloc[0]
    return None


def score_projects(dict_projects, list_projects, time):
    """
    dict of all projects, list of projects available (names), current
    """
    d = {'name': [], 'deadline': [], 'score': [], 'needed_contributors': []}

    for proj in list_projects:
        d['name'].append(dict_projects[proj].name)
        d['score'].append(dict_projects[proj].score)
        d['deadline'].append(eval(dict_projects[proj].deadline))
        d['needed_contributors'].append(dict_projects[proj].needed_contributors)
    df = pd.DataFrame(d)
    df['score_total'] = df.apply(
        lambda row: row['score'] - (time - row['deadline']) if time > row['deadline'] else row['score'], axis=1)
    df = df.sort_values(by=['score_total', 'needed_contributors'], ascending=[False, True])
    return list(df['name'])

