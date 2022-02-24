from pathlib import Path

class Person:
    def __init__(self,name):
        self.name = name
        self.skills = {}

    def add_skill(self, skillanme, level):
        self.skills[skillanme] = level

    def increase_skill(self, skillname):
        self.skills[skillname] += 1

class Project: 
    def __init__(self, name, days, score, deadline):
        self.name = name
        self.days = days
        self.score = score
        self.deadline = deadline
        self.skills = {}

    def needed_skill(self, skillname, level):
        self.skills[skillname] = level

class ProblemInput:
    def __init__(self, filepath):
        self.init_variables()
        self.input_name = Path(filepath).stem

        self.file = open(filepath, 'r')

        line = self.read_line()

        self.num_contributors = int(line[0])
        self.num_projects = int(line[1])

        for contributor in range(int(self.num_contributors)):
            name, num_skills = self.read_line()

            for i in range(int(num_skills)):
                skill, level = self.read_line()

        for i in range(int(self.num_projects)):
            project, duration, score, best_by, needed_contributors =  self.read_line()

            for j in range(int(needed_contributors)):
                skill, level = self.read_line()

            
    def init_variables(self):
        self.n_contributors = -1
        self.n_projects = -1
        self.contributors = {}
        self.projects = {}

    def read_line(self):
        myline = self.file.readline()
        line = myline.split(" ")
        return line
