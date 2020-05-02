from readfile import Readfile
import heapq

class Customer:
    def __init__(self):
        self.stage = ''

class Hmm:
    def __init__(self):
        self.state_table = {
            "ZERO" : ["AWARE", "ZERO"],
            ('ZERO', 'AWARE') : 0.4,
            ('ZERO', 'ZERO')  : 0.6,
            "AWARE" : ["CONSIDERING", "READY", "LOST", "AWARE"],
            ('AWARE', 'CONSIDERING') : 0.3,
            ('AWARE', 'READY')       : 0.01,
            ('AWARE', 'LOST')        : 0.2,
            ('AWARE', 'AWARE')       : 0.49,
            "CONSIDERING" : ["EXPERIENCING", "READY", "LOST", "CONSIDERING"],
            ('CONSIDERING', 'EXPERIENCING') : 0.2,
            ('CONSIDERING', 'READY')        : 0.02,
            ('CONSIDERING', 'LOST')         : 0.3,
            ('CONSIDERING', 'CONSIDERING')  : 0.48,
            "EXPERIENCING" : ["READY", "LOST", "EXPERIENCING"],
            ('EXPERIENCING', 'READY')        : 0.3,
            ('EXPERIENCING', 'LOST')         : 0.3,
            ('EXPERIENCING', 'EXPERIENCING') : 0.4,
            "READY" : ["LOST", "READY"],
            ('READY', 'LOST')      : 0.2,
            ('READY', 'READY') : 0.8,
            "LOST" : ["LOST"],
            ('LOST', 'LOST') : 1.0,
            "SATISFIED" : ["SATISFIED"],
            ('SATISFIED', 'SATISFIED') : 1.0,
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

    def find_hmm(self, start_state, observes):
        last_s = {start_state : 1.0}
        hmm_list = []
        mem = {}
        total = 0

        for emissions in observes:
            path = {}
            for current_s,current_p in last_s.items():
                candidate_s = self.state_table[current_s]
                for possible_n_s in candidate_s:
                    possible_p = current_p
                    possible_p *= self.state_table[(current_s,possible_n_s)]

                    for obs,index in self.emission_index.items():
                        if obs in emissions:
                            possible_p *= self.emission_table[possible_n_s][index]
                        else:
                            possible_p *= (1-self.emission_table[possible_n_s][index])


                    if possible_p > 0:
                        if possible_n_s not in path:
                            path[possible_n_s] = possible_p
                        elif possible_p > path[possible_n_s]:
                            path[possible_n_s] = possible_p
            last_s = path
            total += 1
            mem[total] = path
            print(last_s)
        last_res = heapq.nlargest(1,mem[total])
        n = total -1
        last_res = last_res[0]
        hmm_list.append(last_res)
        for j in range(n,0,-1):
            max_kp = 0
            max_k = ""
            for k,e in mem[j].items():
                if last_res in self.state_table[k]:
                    tem = e * self.state_table[(k,last_res)]
                    if tem > max_kp:
                        max_kp = tem
                        max_k = k
            if max_k == "":
                print("********************BUG********************")
            hmm_list.append(max_k)
            last_res = max_k
        hmm_list = hmm_list[::-1]
        return hmm_list




test_file = "/Users/han/Desktop/George Washington/6511/project4/program/input/hmm_customer_1586733275338.txt"
test = Readfile(test_file)
observe_list = test.get_input()
answer = test.get_answer()
for item in observe_list:
    s = ",".join(item)
    print(s)
print("Step")

test = Hmm()
res = test.find_hmm("ZERO", observe_list)
print(len(answer), len(res))
for i in range(min(len(answer),len(res))):
    space = [" " for _ in range(15 - len(answer[i]))]
    print(answer[i]+"".join(space)+res[i])
if len(answer) > len(res):
    print(answer[-1])