# mem = {
#     ("s","s") : 2,
#     ("d","d") : 3
# }
#
# print(mem[("d","d")])

# emission_table = {
#     'ZERO': [0.1, 0.01, 0.05, 0.3, 0.5, 0.0],
#     'AWARE': [0.1, 0.01, 0.15, 0.3, 0.4, 0.0],
#     'CONSIDERING': [0.2, 0.3, 0.05, 0.4, 0.4, 0.0],
#     'EXPERIENCING': [0.4, 0.6, 0.05, 0.3, 0.4, 0.0],
#     'READY': [0.05, 0.75, 0.35, 0.2, 0.4, 0.0],
#     'LOST': [0.01, 0.01, 0.03, 0.05, 0.2, 0.0],
#     'SATISFIED': [0.4, 0.4, 0.01, 0.05, 0.5, 1.0]
# }
# for i in emission_table:
#     s = sum(emission_table[i])
#     print(s,1-s)

#
# import heapq
# mem = {"c":2, "d":3}
# # heapq.heapify(mem)
# res = heapq.nlargest(1,mem)
# print(mem)
# print(res)

T2 = dict.fromkeys(range(40), {})
print (T2)
