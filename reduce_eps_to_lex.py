from lacava import *
import random
import itertools

def convert(population, e):
    n_cols = len(population)
    new_population = []
    # M
    for col in zip(*population):
        sorted_col = sorted(list(col), reverse=True)
        # N - 1
        for i in range(len(col)-1):
            curr = list(col)
            for j in range(len(curr)):
                if curr[j] >= sorted_col[i] - e:
                    curr[j] = 1
                else:
                    curr[j] = 0
            # groups = {}
            # groups["upper"] = []
            # groups["same"] = []
            # groups["lower"] = []
            # var_to_group = {}
            # curr_i = 0          
            # for val in sorted_col:
            #     if val <= sorted_col[i]:
            #         break
            #     groups["upper"].append(val)
            #     curr_i += 1

            # for val in sorted_col[curr_i:]:
            #     if val <= sorted_col[i] - e:
            #         break
            #     groups["same"].append(val)
            #     curr_i += 1

            # for val in sorted_col[curr_i:]:
            #     groups["lower"].append(val)
            #     curr_i += 1

            # if groups["upper"]:
            #     curr_val_id = len(groups["upper"]) + 1
            #     curr_val = max(groups["upper"])
            #     for val in sorted(groups["upper"], reverse=True):
            #         if val <= curr_val - e:
            #             curr_val_id -= 1
            #         curr_val = val
            #         var_to_group[val] = curr_val_id

            # if groups["same"]:
            #     for val in groups["same"]:
            #         var_to_group[val] = 1

            # if groups["lower"]:
            #     curr_val_id = 0
            #     curr_val = max(groups["lower"])
            #     for val in sorted(groups["lower"], reverse=True):
            #         if val <= curr_val - e:
            #             curr_val_id -= 1
            #         curr_val = val
            #         var_to_group[val] = curr_val_id

            # for j in range(len(curr)):
            #     curr[j] = var_to_group[curr[j]]

            new_population.append(curr)

    new_population = [list(i) for i in zip(*new_population)]
    # print(new_population)
    # Length N
    for ind in new_population[:]:
        #NM - M
        for i in range(len(ind)):
            ind_copy = ind[:]
            # print(ind_copy)
            chunk = i // (n_cols - 1)
            # print(chunk)
            for j in range(chunk * (n_cols-1), i):
                ind_copy[j] = 0
            for j in range(i + 1, (chunk+1)*(n_cols-1)):
                ind_copy[j] = 2
            ind_copy[i] = -1
            # print(ind_copy)
            # print()
            new_population.append(ind_copy)
    return new_population

# Truncated reduces to normal -> add N additional objectives and one new row - new row wins all new objectives. Only count cases new row didn't win
# wait no that doesn't work
# Normal reduces to truncated -> set truncation to 0
# Normal reduces to weighted -> set weights the same
# Normal reduces to epsilon -> set epsilon to 0
# But none of those help unless we prove normal is NP-Hard

e = .1

pop = [[random.random() for i in range(3)], [random.random() for i in range(3)], [random.random() for i in range(3)], [random.random() for i in range(3)]]
probs = []
for i in range(len(pop)):
    probs.append(ep_lex_prob(pop, list(range(len(pop[0]))), pop[i], [e for _ in range(len(pop[0]))], printing=False))
    print(pop[i], probs[i])

print()
converted_pop = convert(pop, e)
probs = []
for i in range(len(converted_pop)):
    probs.append(lex_prob(converted_pop, list(range(len(converted_pop[0]))), converted_pop[i]))
    print(converted_pop[i], probs[i])

# for i in range(len(converted_pop)):
#     print(converted_pop[i])