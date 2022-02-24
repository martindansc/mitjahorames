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

        self.simulation()

    def simulation(self):
        self.time = 0
        self.available_contributors = set()
        self.remaining_projects = set()

        self.current_projects = {}
        self.total_score = 0

    
    def advance_time(self):
        # avançar el temps directament a la següent remove
        # treure els current que acabin en aquest
        next = self.current_projects.pop()
        self.time = next.end_time
        while(self.current_projects.next().time == next)
        self
        pass

    def add_project(self, project, skills_contributors):
        projectObj = self.projects[project]
        projectObj.start_project(self.time)
        for skill, contributor in skills_contributors.items():
            projectObj.add_contributor(skill, contributor)


        self.current_projects[project] = projectObj

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
