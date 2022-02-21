from pathlib import Path  

class ProblemInput:
    def __init__(self, filepath):
        self.init_variables()
        self.input_name = Path(filepath).stem

        with open(filepath) as fp:
            for cnt, line in enumerate(fp):
                self.read_line(cnt, line)

        for i in range(self.n):
            c = str(i)
            for dislike in self.clients_to_dislikes[c]:
                if dislike in self.like_to_clients:
                    for c2 in self.like_to_clients[dislike]:
                        self.incompatible_clients[c] = list(set(self.incompatible_clients.get(c, []) + [c2]))
                        self.incompatible_clients[c2] = list(set(self.incompatible_clients.get(c2, []) + [c]))

    def init_variables(self):
        self.like_to_clients = {}
        self.clients_to_like = {}
        self.dislike_to_clients = {}
        self.clients_to_dislikes = {}
        self.incompatible_clients = {}

    def read_line(self, cnt, line):
        line = line.split(" ")
        if cnt == 0:
            self.n = int(line[0])
        elif cnt%2 == 1:
            id = str((cnt - 1)//2)
            line.pop(0)
            self.clients_to_like[id] = list(map(lambda x: x.strip(), line))
            for i in self.clients_to_like[id]:
                self.like_to_clients[i] = self.like_to_clients.get(i, []) + [id]
            self.incompatible_clients[id] = []
        else:
            id = str((cnt - 1)//2)
            line.pop(0)
            self.clients_to_dislikes[id] = list(map(lambda x: x.strip(), line))
            for i in self.clients_to_dislikes[id]:
                self.dislike_to_clients[i] = self.dislike_to_clients.get(i, []) + [id]