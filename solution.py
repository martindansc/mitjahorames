
import fileinput
import json
import time

class SolutionInterface:
    
    def __init__(self, problem_input):
        self.problem_input = problem_input
        # init code
        return

    def value(self):
        # return the cost of the solution
        raise Exception('Solution value needs to be implemented')

    def to_string(self):
        # return the plain string representation of the solution
        return json.dumps(vars(self))

    def save(self):
        toSave = self.to_string()
        with open("./outputs/%s_%i" % (self.input_name, time.time()), "w") as text_file:
            text_file.write(toSave)


class Solution(SolutionInterface):

    def __init__(self, problem_input):
        super().__init__(problem_input)
        self.ingredients = set()

    def add(self, ingredients):
        self.ingredients.update(ingredients)

    def add_customer(self, customer_id):
        customer_ingredients = self.problem_input.clients_to_like[customer_id]
        self.add(customer_ingredients)

    def value(self):
        score = 0
        for client in range(self.problem_input.n):
            c = str(client)
            has_all = self.ingredients.issuperset(set(self.problem_input.clients_to_like[c]))
            has_none = set(self.problem_input.clients_to_dislikes[c]).isdisjoint(self.ingredients)
            if has_all and has_none:
                score += 1
        return score

    def isValid(self):
        return True

    def to_string(self):
        return str(len(self.ingredients)) + " " + " ".join(map(str, self.ingredients))

