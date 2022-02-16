class ProblemInput:
    def __init__(self, filepath):
        self.init_variables()

        with open(filepath) as fp:
            for cnt, line in enumerate(fp):
                self.read_line(cnt, line)

    def init_variables(self):
        self.like_to_clients = {}
        self.clients_to_like = {}
        self.dislike_to_clients = {}
        self.clients_to_dislikes = {}

    def read_line(self, cnt, line):
        line = line.split(" ")
        if cnt == 0:
            self.n = int(line[0])
        elif cnt%2 == 1:
            id = (cnt - 1)%2
            line.pop()
            self.clients_to_like[id] = line
            for i in line:
                self.like_to_clients[i] = self.like_to_clients.get(i, []) + [id]

        else:
            id = (cnt - 1)%2
            line.pop()
            self.clients_to_dislikes[id] = line
            for i in line:
                self.dislike_to_clients[i] = self.dislike_to_clients.get(i, []) + [id]
