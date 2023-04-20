from lacava import *
import random
import itertools
from copy import deepcopy
import example

# class set_info:
#     def __init__(self, i):
#         self.i = i
#         self.greater = set()
#         self.members = set()
#         self.less = set()


# def convert(population, e):
#     n_cols = len(population)
#     new_population = []
#     # M
#     for col in zip(*population):
#         # N - 1
#         groups = {}
#         for i in range(len(col)):
#             groups[i] = set_info(i)
#             for j in col:
#                 if j >
#                 if j > col[i] - e:
#             curr = list(col)
#             for j in range(len(curr)):
#                 if curr[j] 
#                 if curr[j] >= sorted_col[i] - e:
#                     groups.add(j)
#                 else:
#                     curr[j] = 0




#     new_population = [list(i) for i in zip(*new_population)]
#     # print(new_population)
#     # Length N
#     for ind in new_population[:]:
#         #NM - M
#         for i in range(len(ind)):
#             ind_copy = ind[:]
#             # print(ind_copy)
#             chunk = i // (n_cols - 1)
#             # print(chunk)
#             for j in range(chunk * (n_cols-1), i):
#                 ind_copy[j] = 0
#             for j in range(i + 1, (chunk+1)*(n_cols-1)):
#                 ind_copy[j] = 2
#             ind_copy[i] = -1
#             # print(ind_copy)
#             # print()
#             new_population.append(ind_copy)
#     return new_population

def convert2(population, e):
    n_cols = len(population[0])
    pop_size = len(population)
    new_population = []
    # M
    for col in zip(*population):
        sorted_col = sorted(list(col), reverse=True)
        # N - 1
        for i in range(len(col)):
            curr = list(col)
            for j in range(len(curr)):
                if curr[j] > sorted_col[i]:
                    curr[j] = 2
                elif curr[j] >= sorted_col[i] - e:
                    curr[j] = 1
                else:
                    curr[j] = 0
            new_population.append(curr)

    new_population = [list(i) for i in zip(*new_population)]
    final_pop = []
    focal_vectors = []
    for j, sol in enumerate(new_population):
        # print(j)
        if 2 in sol:
            focal = [i if i!= 2 else 1 for i in sol]
            for i in range(pop_size):
                # print("i ", i)
                if i == j:
                    focal.append(1)
                else:
                    focal.append(0)
                sol.append(0)

            final_pop.append(sol)
            final_pop.append(focal)
            focal_vectors.append(focal)
        else:
            for i in range(pop_size):
                # print("i ", i)                
                if i == j:
                    new_population[j].append(1)
                else:
                    new_population[j].append(0)
            final_pop.append(new_population[j])
            focal_vectors.append(new_population[j])
                

    for vec in focal_vectors:
        for obj in range(n_cols):
            timing_vec = vec[:]
            for i in range((pop_size)*obj, (pop_size)*(obj+1)):
                timing_vec[i] = 0
            for i in range((pop_size)*n_cols, (pop_size)*n_cols + pop_size):
                timing_vec[i] = 3
            final_pop.append(timing_vec)


            
    # print(new_population)
    # Length N

    return final_pop


# Truncated reduces to normal -> add N additional objectives and one new row - new row wins all new objectives. Only count cases new row didn't win
# wait no that doesn't work
# Normal reduces to truncated -> set truncation to 0
# Normal reduces to weighted -> set weights the same
# Normal reduces to epsilon -> set epsilon to 0
# But none of those help unless we prove normal is NP-Hard

e = .1
#pop = [[1,1,4,4],[0,3,3,3],[1,4,0,4],[0,3,1,2]]
#pop = [[random.randint(0,4) for i in range(4)] for j in range(4)]
#pop = [[random.random() for i in range(5)] for j in range(5)]
#pop = [[1, .9], [.9,1], [.8, 1.1]]
#pop = [[1, .9, .7], [.7, 1, 1], [.8,.8,.9]]
# pop = [[1, 1], [.9, .8]]
pop = [[3,1],[2,2],[1,2]]
# pop = [[1, .9,1.1], [.9,1.1, .9], [1.1,1,1]]
probs = []
for i in range(len(pop)):
    probs.append(ep_lex_prob(pop, list(range(len(pop[0]))), pop[i], [e for _ in range(len(pop[0]))], printing=False))
    print(pop[i], probs[i])

print()
converted_pop = convert2(pop, e)
# probs = []
# for i in range(len(converted_pop)):
#     probs.append(lex_prob(converted_pop, list(range(len(converted_pop[0]))), converted_pop[i]))
#     print(converted_pop[i], probs[i])

probs = example.LexicaseFitness(converted_pop)

for i in range(len(converted_pop)):
    if 1 in converted_pop[i][-1*len(pop):]:
        print(converted_pop[i], probs[i])

print()
for i in range(len(converted_pop)):
    print(converted_pop[i], probs[i])
