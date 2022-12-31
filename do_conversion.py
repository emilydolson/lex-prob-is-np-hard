from lacava import *

# def convert(variables, clauses):
#     var_to_num = {}
#     num_to_var = {}
#     population = []
#     section_2_start = len(clauses) * len(variables) * 2
#     vector_len = section_2_start + len(variables)*2  #+ len(clauses)
#     section_3_start = vector_len
#     # print(section_2_start, vector_len)
#     # section_3_start = (len(variables)*4) 

#     for i, var in enumerate(variables):
#         if (var.startswith("!")):
#             var = var.strip("!")
#         if var in var_to_num:
#             continue
#         index = i*2
#         var_to_num[var] = index
#         num_to_var[index] = var
#         var_to_num["!" + var] = index + 1
#         num_to_var[index + 1] = "!" + var

#     for ci,clause in enumerate(clauses):
#         solution = [0]*vector_len
#         # solution[section_3_start+ci] = 1
#         for i in range(section_2_start, section_3_start):
#             solution[i] = 1
#         start_point = len(variables) * 2 * ci
#         for var in clause:
#             var_ind = var_to_num[var]
#             solution[start_point + var_ind] = 1
#         for var in variables:
#             sub_solution = solution[:]
#             sub_solution[section_2_start + var_to_num[var]] = 0
#             population.append(sub_solution)
#             sub_solution = solution[:]
#             # print(len(sub_solution), section_2_start, var, var_to_num)
#             sub_solution[section_2_start + var_to_num["!" + var]] = 0
#             population.append(sub_solution)
#             # print(var, section_2_start + var_to_num[var], section_2_start + var_to_num["!" + var])

#     for var in variables:
#         solution = [0]*vector_len
#         var_ind = var_to_num[var]
#         if var.startswith("!"):
#             var = var.strip("!")
#         else:
#             var = "!" + var
#         opposite_ind = var_to_num[var]
#         for i in range(opposite_ind, section_2_start, len(variables)*2):
#             solution[i] = 2
#         for i in range(section_2_start, section_3_start):
#             solution[i] = 1
#         solution[section_2_start + opposite_ind] = 0
#         population.append(solution)

#         solution = [0]*vector_len
#         for i in range(var_ind, section_2_start, len(variables)*2):
#             solution[i] = 2

#         for i in range(section_2_start, section_3_start):
#             solution[i] = 1
#         solution[section_2_start + var_ind] = 0    
#         population.append(solution)
        
#         solution = [3]*vector_len
#         for i in range(section_2_start, section_3_start):
#             solution[i] = 1
#         solution[section_2_start + var_ind] = 0    
#         solution[section_2_start + opposite_ind] = 0   
#         population.append(solution)

    # for ci,clause in enumerate(clauses):
    #     solution = [0]*vector_len
    #     solution[section_3_start+ci] = 1
    #     for i in range(section_2_start, section_3_start):
    #         solution[i] = 1
    #     for i in range(section_3_start, vector_len):
    #         solution[i] = 3            
    #     for var in clause:
    #         var_ind = var_to_num[var]
    #         solution[var_ind] = 1
    #     for var in variables:
    #         sub_solution = solution[:]
    #         sub_solution[section_2_start + var_to_num[var]] = 0
    #         for var2 in variables:
    #             inner = sub_solution[:]
    #             inner[var_to_num[var2]] = -1
    #             population.append(inner)
    #             inner = sub_solution[:]
    #             inner[var_to_num["!" + var2]] = -1
    #             population.append(inner)
                
    #         sub_solution = solution[:]
    #         # print(len(sub_solution), section_2_start, var, var_to_num)
    #         sub_solution[section_2_start + var_to_num["!" + var]] = 0
    #         for var2 in variables:
    #             inner = sub_solution[:]
    #             inner[var_to_num[var2]] = -1
    #             population.append(inner)
    #             inner = sub_solution[:]
    #             inner[var_to_num["!" + var2]] = -1
    #             population.append(inner)

            # print(var, section_2_start + var_to_num[var], section_2_start + var_to_num["!" + var])

# def convert(variables, clauses):
#     var_to_num = {}
#     num_to_var = {}
#     population = []
#     section_2_start = len(clauses) * len(variables) * 2
#     vector_len = section_2_start + len(variables)*2  #+ len(clauses)
#     section_3_start = vector_len
#     # print(section_2_start, vector_len)
#     # section_3_start = (len(variables)*4) 

#     for i, var in enumerate(variables):
#         if (var.startswith("!")):
#             var = var.strip("!")
#         if var in var_to_num:
#             continue
#         index = i*2
#         var_to_num[var] = index
#         num_to_var[index] = var
#         var_to_num["!" + var] = index + 1
#         num_to_var[index + 1] = "!" + var

#     solution = [0]*vector_len
#     for ci,clause in enumerate(clauses):        
#         # solution[section_3_start+ci] = 1
#         for i in range(section_2_start, section_3_start):
#             solution[i] = 1
#         start_point = len(variables) * 2 * ci
#         for var in clause:
#             var_ind = var_to_num[var]
#             solution[start_point + var_ind] = 1
#     for var in variables:
#         sub_solution = solution[:]
#         sub_solution[section_2_start + var_to_num[var]] = 0
#         population.append(sub_solution)
#         sub_solution = solution[:]
#         # print(len(sub_solution), section_2_start, var, var_to_num)
#         sub_solution[section_2_start + var_to_num["!" + var]] = 0
#         population.append(sub_solution)
#         # print(var, section_2_start + var_to_num[var], section_2_start + var_to_num["!" + var])

#     for var in variables:
#         for ci in range(len(clauses)):
#             solution = population[0][:]
#             var_ind = var_to_num[var]
#             if var.startswith("!"):
#                 var = var.strip("!")
#             else:
#                 var = "!" + var
#             opposite_ind = var_to_num[var]
#             # for i in range(opposite_ind, section_2_start, len(variables)*2):
#             for i in range(ci*len(variables)*2,(ci+1)*len(variables)*2):
#                 solution[i] = 0
#             solution[(ci*len(variables)*2)+opposite_ind] = 2
#             for i in range(section_2_start, section_3_start):
#                 solution[i] = 1
#             solution[section_2_start + opposite_ind] = 0
#             population.append(solution)

#             solution = population[0][:]
#             # for i in range(var_ind, section_2_start, len(variables)*2):
#             for i in range(ci*len(variables)*2,(ci+1)*len(variables)*2):
#                 solution[i] = 0
#             solution[(ci*len(variables)*2)+var_ind] = 2
#             for i in range(section_2_start, section_3_start):
#                 solution[i] = 1
#             solution[section_2_start + var_ind] = 0    
#             population.append(solution)
        
#         solution = [3]*vector_len
#         for i in range(section_2_start, section_3_start):
#             solution[i] = 1
#         solution[section_2_start + var_ind] = 0    
#         solution[section_2_start + opposite_ind] = 0   
#         population.append(solution)

#     return population

def convert(variables, clauses):
    var_to_num = {}
    num_to_var = {}
    population = []
    section_2_start = len(clauses) * len(variables) * 2
    vector_len = section_2_start + len(variables)*2  #+ len(clauses)
    section_3_start = vector_len
    # print(section_2_start, vector_len)
    # section_3_start = (len(variables)*4) 

    for i, var in enumerate(variables):
        if (var.startswith("!")):
            var = var.strip("!")
        if var in var_to_num:
            continue
        index = i*2
        var_to_num[var] = index
        num_to_var[index] = var
        var_to_num["!" + var] = index + 1
        num_to_var[index + 1] = "!" + var

    solution = [0]*vector_len
    for i in range(section_2_start, section_3_start):
        solution[i] = .9

    for ci,clause in enumerate(clauses):        
        # solution[section_3_start+ci] = 1
        start_point = len(variables) * 2 * ci
        for var in clause:
            var_ind = var_to_num[var]
            solution[start_point + var_ind] = 1
    population.append(solution)

    for var in variables:
        for ci in range(len(clauses)):
            solution = population[0][:]
            var_ind = var_to_num[var]
            if var.startswith("!"):
                var = var.strip("!")
            else:
                var = "!" + var
            opposite_ind = var_to_num[var]
            # for i in range(opposite_ind, section_2_start, len(variables)*2):
            for i in range(ci*len(variables)*2,(ci+1)*len(variables)*2):
                solution[i] = 0
            solution[(ci*len(variables)*2)+opposite_ind] = 2
            for i in range(section_2_start, section_3_start):
                solution[i] = .9
            solution[section_2_start + opposite_ind] = .8
            solution[section_2_start + var_ind] = 1    
            population.append(solution)

            solution = population[0][:]
            # for i in range(var_ind, section_2_start, len(variables)*2):
            for i in range(ci*len(variables)*2,(ci+1)*len(variables)*2):
                solution[i] = 0
            solution[(ci*len(variables)*2)+var_ind] = 2
            for i in range(section_2_start, section_3_start):
                solution[i] = .9
            solution[section_2_start + var_ind] = .8    
            solution[section_2_start + opposite_ind] = 1
            population.append(solution)
        
        solution = [3]*vector_len
        for i in range(section_2_start, section_3_start):
            solution[i] = .9
        solution[section_2_start + var_ind] = 0    
        solution[section_2_start + opposite_ind] = 0   
        population.append(solution)

    return population


def verify(probs, variables, clauses):
    clause_vecs = len(variables) * 2 * len(clauses)
    okay = [True] * len(variables) * 2
    for clause in range(0, clause_vecs, len(variables) * 2):
        for var in range(len(variables)):
            if probs[clause+(var*2)] == 0:
                okay[var*2] = False
            # print(var, clause, probs)
            if probs[clause+(var*2)+1] == 0:
                okay[var*2+1] = False
                

    print(okay)


# variables = ["X1"]
# clauses = [["X1"], ["!X1"]]

if __name__ == "__main__":

    variables = ["X1", "X2"]
    clauses = [["X1"], ["X2"]]

    # variables = ["X1", "X2"]
    # clauses = [["X1"], ["!X1", "X2"], ["!X2"]]
    # variables = ["X1", "X2", "X3"]
    # clauses = [["X1", "X2"], ["!X1", "!X2"], ["X1"], ["X2"]]

    # variables = ["X1", "X2", "X3"]
    # clauses = [["X1", "X2", "X3"], ["!X1", "!X2", "X3"], 
    #            ["X1", "!X2", "!X3"], ["!X1", "X2", "!X3"]]

    # variables = ["X1", "X2", "X3"]
    # clauses = [["X1", "X2", "X3"], ["X1", "X2", "X3"], 
    #            ["X1", "X2"], ["X1"]]

    # variables = ["X1", "X2", "X3"]
    # clauses = [["X1", "X2", "X3"], 
    #            ["X1", "X2"]]

    # variables = ["X1", "X2"]
    # clauses = [["X1"], ["!X1", "X2"], ["!X2", "!X1"]]

    pop = convert(variables, clauses)
    probs = []
    # print(lex_prob(pop, list(range(len(pop[0]))), pop[4]))
    # print(pop[4])
    # ep_lex_prob(pop, list(range(len(pop[0]))), pop[0], [.11 for _ in range(len(pop[0]))], printing=True)
    for i in range(len(pop)):
        probs.append(ep_lex_prob(pop, list(range(len(pop[0]))), pop[i], [.11 for _ in range(len(pop[0]))], printing=False))
        print(pop[i], probs[i])

    # verify(probs, variables, clauses)
    # for i in range(len(pop)):
    #     print(pop[i])