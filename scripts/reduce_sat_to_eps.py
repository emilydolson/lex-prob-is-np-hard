import ec_ecology_toolbox as eco
from copy import deepcopy


def invert_var_ind(n):
    if n % 2 == 0:
        return n + 1
    else:
        return n - 1


def make_var_dict(variables):
    var_to_num = {}
    for i, var in enumerate(variables):
        if (var.startswith("!")):
            var = var.strip("!")
        if var in var_to_num:
            continue
        index = i*2
        var_to_num[var] = index
        var_to_num["!" + var] = index + 1
    return var_to_num


def convert_to_indices(variables, clauses):
    var_to_num = make_var_dict(variables)

    new_clauses = deepcopy(clauses)
    for i, clause in enumerate(clauses):
        for j, var in enumerate(clause):
            new_clauses[i][j] = var_to_num[var]

    new_variables = deepcopy(variables)
    for i, var in enumerate(new_variables):
        new_variables[i] = var_to_num[var]

    return new_variables, new_clauses


def convert(variables, clauses):
    variables, clauses = convert_to_indices(variables, clauses)
    return do_conversion(variables, clauses)


def do_conversion(variables, clauses):
    population = []
    section_2_start = len(clauses) * len(variables) * 2
    vector_len = section_2_start + len(variables)*2  #+ len(clauses)
    section_3_start = vector_len

    # Make focal vector
    focal = [0 if i < section_2_start else .9 for i in range(vector_len)]
    for ci, clause in enumerate(clauses):        
        # Set up Cxixj criteria
        start_point = len(variables) * 2 * ci
        for var in clause:
            focal[start_point + var] = 1
    population.append(focal)

    # Make variable vecotrs
    for var in variables:
        for ci in range(len(clauses)):
            solution = focal[:]
            var_ind = var
            opposite_ind = invert_var_ind(var)

            # Set Cxixj value for focal clause
            for i in range(ci*len(variables)*2,(ci+1)*len(variables)*2):
                solution[i] = 0
            # Set Cxixj value for oppositie of focal variable in focal clause
            solution[(ci*len(variables)*2)+opposite_ind] = 2
            # Set Dxi criteria
            for i in range(section_2_start, section_3_start):
                solution[i] = .9
            solution[section_2_start + opposite_ind] = .8
            solution[section_2_start + var_ind] = 1    
            population.append(solution)

            # Create opposite variable vector
            solution = focal[:]
            for i in range(ci*len(variables)*2,(ci+1)*len(variables)*2):
                solution[i] = 0
            solution[(ci*len(variables)*2)+var_ind] = 2
            for i in range(section_2_start, section_3_start):
                solution[i] = .9
            solution[section_2_start + var_ind] = .8    
            solution[section_2_start + opposite_ind] = 1
            population.append(solution)

        # Add timing vectors        
        solution = [3 if i < section_2_start else .9 for i in range(vector_len)]
        solution[section_2_start + var_ind] = 0 
        solution[section_2_start + opposite_ind] = 0 
        population.append(solution)

    return population


if __name__ == "__main__":

    variables = ["X1", "X2"]
    clauses = [["X1"], ["!X1", "X2"]]

    pop = convert(variables, clauses)
    probs = eco.LexicaseFitness(pop, .1)

    for i in range(len(pop)):
        print(pop[i], probs[i])

    assert probs[0] > 0

    variables = ["X1", "X2"]
    clauses = [["X1"], ["!X1", "X2"], ["!X2"]]

    pop = convert(variables, clauses)
    probs = eco.LexicaseFitness(pop, .1)

    for i in range(len(pop)):
        print(pop[i], probs[i])

    assert probs[0] == 0