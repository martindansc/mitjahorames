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
