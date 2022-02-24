from operator import attrgetter
from pathlib import Path
import pandas as pd

class Contributor:
    def __init__(self,name, num_skills):
        self.name = name
        self.num_skills = int(num_skills)
        self.skills = {}

    def add_skill(self, skillname, level):
        self.skills[skillname] = level

    def increase_skill(self, skillname):
        self.skills[skillname] += 1

class Project: 
    def __init__(self, name, days, score, deadline, needed_contributors):
        self.name = name
        self.days = days
        self.score = score
        self.deadline = deadline
        self.needed_contributors = int(needed_contributors)
        self.skills = {}
        self.contributors = {}
        self.started = False

    def needed_skill(self, skillname, level):
        self.skills[skillname] = level

    def start_project(self, time):
        self.started = True
        self.start_time = time
        self.end_time = time + self.days
        self.final_score = self.score - max(0, self.end_time - self.deadline)

    def add_contributor(self, skill, contributor):
        self.contributors[skill] = contributor

    def unfullfilled_roles(self):
        unfillfilled_roles = {}
        for skill_name in self.skills:
            if not self.contributors[skill_name]:
                unfillfilled_roles[skill_name] = self.skills[skill_name]
        return unfillfilled_roles

    def has_all_roles_fullfilled(self): 
        return len(self.contributors) == len(self.skills)

class ProblemInput:
    def __init__(self, filepath):
        self.init_variables()
        self.simulation()


        self.input_name = Path(filepath).stem

        self.file = open(filepath, 'r')

        line = self.read_line()

        self.num_contributors = int(line[0])
        self.num_projects = int(line[1])

        for contributor in range(self.num_contributors):
            name, num_skills = self.read_line()
            self.contributors[name] = Contributor(name, num_skills)

            for i in range(int(num_skills)):
                skill, level = self.read_line()
                self.contributors[name].add_skill(skill, level)
                self.available_contributors.add(name)

        for i in range(self.num_projects):
            project, duration, score, best_by, needed_contributors =  self.read_line()
            self.remaining_projects.add(project)
            self.projects[project] = Project(project, duration, score, best_by, needed_contributors)
            #self.projects.add(project)

            for j in range(int(needed_contributors)):
                skill, level = self.read_line()
                self.projects[project].needed_skill(skill, level)



    def simulation(self):
        self.time = 0
        self.available_contributors = set()
        self.remaining_projects = set()

        self.current_projects = {}
        self.total_score = 0

    def full_remaining_projects(self):
        rp = set()
        for project in self.remaining_projects:
            rp.add(self.projects[project])
        return rp
    
    def advance_time(self):
        min_date = min(self.full_remaining_projects(), key=attrgetter('end_date')).end_date
        for (projectName, projectObj) in self.remaining_projects.items():
            if projectObj.end_date == min_date:
                self.remove_project(projectObj)
                self.remaining_projects.remove(projectName)
        
        self.time = min_date

    def add_project(self, project, skills_contributors):
        projectObj = self.projects[project]
        projectObj.start_project(self.time)
        for skill, contributor in skills_contributors.items():
            projectObj.add_contributor(skill, contributor)

        self.current_projects[project] = projectObj
        self.remaining_projects.remove(project)

    def remove_project(self, project):
        for contributor in project.contributors.values():
            self.available_contributors.add(contributor)

        self.total_score += project.final_score
        
            
    def init_variables(self):
        self.n_contributors = -1
        self.n_projects = -1
        self.contributors = {}
        self.projects = {}

    def read_line(self):
        myline = self.file.readline()
        line = myline.rstrip("\n").split(" ")
        return line

    def assign_contributors(self, project):
        unfullfilled_roles = self.projects[project].unfullfilled_roles()
        contributors = {}
        for role_skill in unfullfilled_roles:
            contribName = self.choose_contrib(self.full_available_contributors(), role_skill, unfullfilled_roles[role_skill])

            if not contribName:
                return None

            contributors[role_skill] = contribName

        self.add_project(project, contributors)

    def full_available_contributors(self):
        contributors = {}
        for contr in self.available_contributors:
            contributors[contr] = self.contributors[contr]

    def choose_contrib(self, contributors, skill, level):
        #choose contributor with less skills and level that fulfills the job
        #dict of contributors, name skill, level skill (int)

        contributor_dict  = {'name':[],'skill':[],'level':[],'total_skills':[]}
        for contr in contributors:
            if skill in contributors[contr].skills.keys():
                contributor_dict['name'].append(contr.name)
                contributor_dict['level'].append(eval(contributors[contr].skills[skill]))
                contributor_dict['skill'].append(skill)
                contributor_dict['total_skills'].append(len(contributors[contr].skills.keys()))
        df = pd.DataFrame(contributor_dict)
        df = df[df['level']>=level]
        df.sort_values(by= ['level','total_skills'],ascending=[True,True])
        if df.shape[0]>0:
            return df['name'].iloc[0]
        return None
