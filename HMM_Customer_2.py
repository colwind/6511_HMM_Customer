class Hmm:
    def __init__(self):
        self.state_table = {
            "ZERO" : {
                "ZERO" : 0.6},
            "AWARE" : {
                "ZERO" : 0.3,
                "AWARE" : 0.49},
            "CONSIDERING" : {
                "AWARE" : 0.3,
                "CONSIDERING" : 0.48},
            "EXPERIENCING" : {
                "CONSIDERING" : 0.2,
                "EXPERIENCING" : 0.4},
            "READY" : {
                "AWARE" : 0.2,
                "CONSIDERING" : 0.02,
                "EXPERIENCING" : 0.3,
                "READY" : 0.8},
            "LOST" : {
                "AWARE" : 0.2,
                "CONSIDERING" : 0.3,
                "EXPERIENCING" : 0.3,
                "READY" : 0.2,
                "LOST" : 1.0},
        }

        self.emission_table = {
            'ZERO' : {
                'DEMO'       : 0.1,
                'VIDEO'      : 0.01,
                'TESTIMONIAL': 0.05,
                'PRICING'    : 0.3,
                'BLOG'       : 0.5,
                'PAYMENT'    : 0.0},
            'AWARE': {
                'DEMO'       : 0.1,
                'VIDEO'      : 0.01,
                'TESTIMONIAL': 0.15,
                'PRICING'    : 0.3,
                'BLOG'       : 0.4,
                'PAYMENT'    : 0.0},
            'CONSIDERING': {
                'DEMO'       : 0.2,
                'VIDEO'      : 0.3,
                'TESTIMONIAL': 0.05,
                'PRICING'    : 0.4,
                'BLOG'       : 0.4,
                'PAYMENT'    : 0.0},
            'EXPERIENCING': {
                'DEMO'       : 0.4,
                'VIDEO'      : 0.6,
                'TESTIMONIAL': 0.05,
                'PRICING'    : 0.3,
                'BLOG'       : 0.4,
                'PAYMENT'    : 0.0},
            'READY': {
                'DEMO'       : 0.05,
                'VIDEO'      : 0.75,
                'TESTIMONIAL': 0.35,
                'PRICING'    : 0.2,
                'BLOG'       : 0.4,
                'PAYMENT'    : 0.0},
            'LOST': {
                'DEMO'       : 0.01,
                'VIDEO'      : 0.01,
                'TESTIMONIAL': 0.03,
                'PRICING'    : 0.05,
                'BLOG'       : 0.2,
                'PAYMENT'    : 0.0},
            'SATISFIED': {
                'DEMO'       : 0.4,
                'VIDEO'      : 0.4,
                'TESTIMONIAL': 0.01,
                'PRICING'    : 0.05,
                'BLOG'       : 0.5,
                'PAYMENT'    : 1.0},
        }

    def get_input(self, dir):
        file = open(dir, "r", encoding="utf-8")
        data = []
        path = file.readline()
        while path[0:1] == "#":
            path = file.readline()
        while path[0:1] != "#":
            path = path.strip("\n")
            line_elements = path.split(",")
            data.append(line_elements)
            path = file.readline()
        return data

    def find_hmm(self, observes,number):
        T1 = {"ZERO" : 1.0}
        T2 = {}
        for i in range(number):
            T2[i] = {}
        res = []
        mem = {}
        i = 0
        total = 0

        for emissions in observes:
            path = {}
            if "PAYMENT" in emissions:
                T2[i]["SATISFIED"] = "READY"
                path["SATISFIED"] = 1.0
            for key, value in self.state_table.items():
                max_p = 0
                T2_key = ""
                for previous_s, previous_p in value.items():
                    if previous_s in T1:
                        possible_p = T1[previous_s]
                        possible_p *= self.state_table[key][previous_s]
                        for emi in self.emission_table["ZERO"]:
                            if emi in emissions:
                                possible_p *= self.emission_table[key][emi]
                            else:
                                possible_p *= (1 - self.emission_table[key][emi])
                        if possible_p > max_p:
                            max_p = possible_p
                            T2_key = previous_s
                if max_p > 0:
                    path[key] = max_p
                    T2[i][key] = T2_key
            T1 = path
            i += 1
        i -= 1
        fnial_state = ""
        final_prop = 0
        for s,p in T1.items():
            if p > final_prop:
                final_prop = p
                fnial_state = s
        res.append(fnial_state)
        for j in range(i,-1,-1):
            res.append(T2[j][fnial_state])
            fnial_state = T2[j][fnial_state]
        res = res[1:][::-1]
        return res
file = "/Users/han/Desktop/George Washington/6511/project4/program/input/hmm_customer_1586733275396.txt"
customer = Hmm()
emissions = customer.get_input(file)
res = customer.find_hmm(emissions,len(emissions))
for ele in res:
    print(ele)