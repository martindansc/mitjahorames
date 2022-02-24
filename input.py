from pathlib import Path

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

    def needed_skill(self, skillname, level):
        self.skills[skillname] = level

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

        for i in range(self.num_projects):
            project, duration, score, best_by, needed_contributors =  self.read_line()
            self.projects[project] = Project(project, duration, score, best_by, needed_contributors)

            for j in range(int(needed_contributors)):
                skill, level = self.read_line()
                self.projects[project].needed_skill(skill, level)

            
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
        unfullfilled_roles = project.unfullfilled_roles()
        for role_skill in unfullfilled_roles:
            contribName = self.choose_contrib(project, role_skill, unfullfilled_roles[role_skill])
            project.add_contributor(contribName)

    def choose_contrib(self, project): 
        return self.contributors[0];