from operator import attrgetter
from pathlib import Path
import pandas as pd
from solution import SolutionInterface

class Contributor:
    def __init__(self,name, num_skills):
        self.name = name
        self.num_skills = int(num_skills)
        self.skills = {}

    def add_skill(self, skillname, level):
        self.skills[skillname] = int(level)

    def increase_skill(self, skillname):
        self.skills[skillname] += 1

class Project: 
    def __init__(self, name, days, score, deadline, needed_contributors):
        self.name = name
        self.days = int(days)
        self.score = int(score)
        self.deadline = int(deadline)
        self.needed_contributors = int(needed_contributors)
        self.skills = {}
        self.role_skills = set()
        self.contributors = {}
        self.started = False

    def needed_skill(self, skillname, level):
        self.skills[skillname] = int(level)
        self.role_skills.add(skillname)

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
            if not skill_name in self.contributors:
                unfillfilled_roles[skill_name] = self.skills[skill_name]
        return unfillfilled_roles

    def has_all_roles_fullfilled(self): 
        return len(self.contributors) == len(self.skills)


    def score_if_now(self, time):
        end_time = time + self.days
        return self.score - max(0, end_time - self.deadline)

class ProblemInput(SolutionInterface):

    def __init__(self, filepath):
        super().__init__(Path(filepath).stem)
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
        if len(self.current_projects) == 0:
            print("You should add at least one project to advance the time")
            return False
            
        min_date = min(self.current_projects.values(), key=attrgetter('end_time')).end_time
        for (projectName, projectObj) in list(self.current_projects.items()).copy():
            if projectObj.end_time == min_date:
                self.remove_project(projectObj)
                del self.current_projects[projectName]
        
        self.time = min_date
        return True

    def add_project(self, project, skills_contributors):
        projectObj = self.projects[project]
        projectObj.start_project(self.time)
        for skill, contributor in skills_contributors.items():
            projectObj.add_contributor(skill, contributor)
            self.available_contributors.remove(contributor)

        self.current_projects[project] = projectObj
        self.remaining_projects.remove(project)

    def remove_project(self, project):
        for skill, contributor in project.contributors.items():
            contributorObj = self.contributors[contributor]
            if contributorObj.skills[skill] <= project.skills[skill]:
                contributorObj.skills[skill] += 1
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
            contribName = self.choose_contrib(role_skill, unfullfilled_roles[role_skill])

            if not contribName:
                return None

            contributors[role_skill] = contribName

        self.add_project(project, contributors)

    def choose_contrib(self, skill, level):
        #choose contributor with less skills and level that fulfills the job
        #dict of contributors, name skill, level skill (int)

        contributor_dict  = {'name':[],'skill':[],'level':[],'total_skills':[]}
        for name in self.available_contributors:
            contr = self.contributors[name]
            if skill in contr.skills.keys():
                contributor_dict['name'].append(contr.name)
                contributor_dict['level'].append(int(contr.skills[skill]))
                contributor_dict['skill'].append(skill)
                contributor_dict['total_skills'].append(len(contr.skills.keys()))
        df = pd.DataFrame(contributor_dict)
        df = df[df['level']>= int(level)]
        df.sort_values(by= ['level','total_skills'], ascending=[True,True])
        if df.shape[0]>0:
            return df['name'].iloc[0]
        return None

    def planned_projects_sorted_by_time(self):
        planned_projects = filter(lambda p: hasattr(p, 'start_time'), self.projects.values())

        return sorted(planned_projects, key=lambda p: p.start_time)


    def to_string(self):
        planned_projects = self.planned_projects_sorted_by_time()

        output = str(len(planned_projects))

        for project in planned_projects:
            output += "\n" + project.name + "\n"

            contributors = set()
            for skill_name in project.role_skills:
                contributors.add(project.contributors[skill_name])

            output += ' '.join(contributors)

        return output
