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
            self.answer.append(path)
            path = self.file.readline()
    def get_input(self):
        return self.mem

    def get_answer(self):
        return self.answer


class Hmm:
    def __init__(self):
        self.state_table = {
            "ZERO" : {
                "AWARE" : 0.4,
                "ZERO" : 0.6},
            "AWARE" : {
                "CONSIDERING" : 0.3,
                "READY" : 0.01,
                "LOST" : 0.2,
                "AWARE" : 0.49},
            "CONSIDERING" : {
                "EXPERIENCING" : 0.2,
                "READY" : 0.02,
                "LOST" : 0.3,
                "CONSIDERING" : 0.48},
            "EXPERIENCING" : {
                "READY" : 0.3,
                "LOST" : 0.3,
                "EXPERIENCING" : 0.4},
            "READY" : {
                "LOST" : 0.2,
                "READY" : 0.8},
            "LOST" : {
                "LOST" : 1.0},
            "SATISFIED" : {
                "SATISFIED" : 1.0}
        }

        self.emission_list = ["DEMO", "VIDEO", "TESTIMONIAL", "PRICING", "BLOG", "PAYMENT"]

        self.emission_index = {
            'DEMO'       : 0,
            'VIDEO'      : 1,
            'TESTIMONIAL': 2,
            'PRICING'    : 3,
            'BLOG'       : 4,
            'PAYMENT'    : 5
        }

        self.emission_table = {
            'ZERO' : [0.1, 0.01, 0.05, 0.3, 0.5, 0.0],
            'AWARE' : [0.1, 0.01, 0.15, 0.3, 0.4, 0.0],
            'CONSIDERING' : [0.2, 0.3, 0.05, 0.4, 0.4, 0.0],
            'EXPERIENCING' : [0.4, 0.6, 0.05, 0.3, 0.4, 0.0],
            'READY' : [0.05, 0.75, 0.35, 0.2, 0.4, 0.0],
            'LOST' : [0.01, 0.01, 0.03, 0.05, 0.2, 0.0],
            'SATISFIED' : [0.4, 0.4, 0.01, 0.05, 0.5, 1.0]
        }

    def find_hmm(self, start_state, observes,count):
        T1 = {start_state : 1.0}
        T2 = {}
        for i in range(count):
            T2[i] = {}
        hmm_list = []
        i = 0

        for emissions in observes:
            i += 1
            path = {}
            if "PAYMENT" in emissions:
                temp = "SATISFIED"
                temp2 = "READY"
                T2[i][temp] = temp2
                path = {temp : 1.0}
            else:
                for key, value in self.state_table.items():
                    max_p = 0
                    T2_key = ""
                    for previous_s, previous_p in T1.items():
                        if key in self.state_table[previous_s]:
                            possible_p = previous_p
                            possible_p *= self.state_table[previous_s][key]
                            for obs,index in self.emission_index.items():
                                if obs in emissions:
                                    possible_p *= self.emission_table[key][index]
                                else:
                                    possible_p *= (1 - self.emission_table[key][index])
                            if possible_p > max_p:
                                max_p = possible_p
                                T2_key = previous_s
                    if max_p > 0:
                        path[key] = max_p
                        T2[i][key] = T2_key
            T1 = path
            print(T1)
        last_s = ""
        temp = 0
        for s,p in T1.items():
            if p > temp:
                temp = p
                last_s = s

        for j in range(i,0,-1):
            hmm_list.append(last_s)
            last_s = T2[j][last_s]
        hmm_list = hmm_list[::-1]

        for y,u in T2.items():
            print (y, u)

        return hmm_list




test_file = "/Users/han/Desktop/George Washington/6511/project4/program/input/hmm_customer_1586733277462.txt"
# test_file = "/Users/han/Desktop/George Washington/6511/project4/program/input/hmm_customer_1586733275396.txt"

test = Readfile(test_file)
observe_list = test.get_input()
answer = test.get_answer()
print("Step:------------------------------------")
test = Hmm()
res = test.find_hmm("ZERO", observe_list,len(observe_list)+1)
print("\n\n------------------------Input:")
for item in observe_list:
    s = ",".join(item)
    print(s)
print("---------------------------Output:")
if not answer:
    print("\n".join(res))
else:
    if len(answer) > len(res):
        answer = answer[1:]
    print(len(answer), len(res))
    print("Answer         My Output ")
    for i in range(min(len(answer),len(res))):
        space = [" " for _ in range(15 - len(answer[i]))]
        print(answer[i]+"".join(space)+res[i])