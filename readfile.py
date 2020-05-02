class Readfile:
    def __init__(self, file):
        self.file = open(file, "r", encoding = "utf-8")
        self.mem = []
        self.answer = []

        path = self.file.readline()
        while path[0:1] == "#":
            path = self.file.readline()
        while path[0:1] != "#":
            path = path.strip("\n")
            line_elements = path.split(",")
            self.mem.append(line_elements)
            path = self.file.readline()

        while path[0:1] == "#":
            path = self.file.readline()
        while path:
            path = path.strip("\n")
            # line_elements = path.split(",")
            self.answer.append(path)
            path = self.file.readline()

    def get_input(self):
        return self.mem

    def get_answer(self):
        return self.answer



def test():
    file = "/Users/han/Desktop/George Washington/6511/project4/program/input/hmm_customer_1586733275373.txt"
    test = Readfile(file)
    print(test.get_input())

# test()
