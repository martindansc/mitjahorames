with open("input_data/a_an_example.in.txt") as fp:
    lines = fp.readlines()
    num_contributors, num_projects = lines[0].split(" ")
    line_number = 1
    for contributor in range(int(num_contributors)):
        name, num_skills = lines[line_number].split(" ")
        line_number +=1
        for i in range(int(num_skills)):
            skill, level = lines[line_number].split(" ")
            line_number +=1
    for i in range(int(num_projects)):
        project, duration, score, best_by, needed_contributors = lines[line_number].split(" ")
        line_number +=1
        for j in range(int(needed_contributors)):
            skill, level = lines[line_number].split(" ")
            line_number +=1

