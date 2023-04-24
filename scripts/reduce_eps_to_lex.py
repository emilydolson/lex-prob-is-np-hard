import ec_ecology_toolbox as eco
import random


def convert(population, e):
    """
    Convert an instance of epsilon lexicase selection to
    an instance of traditional lexicase selection. For each
    member of the original population, there will be a
    corresponding focal vector in the new population. If and only if
    the member of the original population had a non-zero probability
    (P_lex) of being selected by epsilon lexicase selection, the
    corresponding focal vector will have a non-zero probability of
    selection under standard lexicase selection.

    Parameters:
    - Population: a list of lists of float indicating the input
        population's scores on each fitness criterion.
    - Epsilon: the value of epsilon being used by epsilon lexicase

    Returns:
    1. The population to use as as input to lexicase selection
    2. The list of focal vectors (which are each also in the
       population being returned)
    """
    n_cols = len(population[0])
    pop_size = len(population)
    new_population = []
    # O(M) time
    # Step through each fitness criterion
    for col in zip(*population):
        # Get scores on this criterion in order
        sorted_col = sorted(list(col), reverse=True)
        # O(N - 1) time
        # Make N-1 new columns to record all possible ties
        for i in range(len(col)):
            curr = list(col)
            # Scores indicate ties
            for j in range(len(curr)):
                if curr[j] > sorted_col[i]:
                    curr[j] = 2
                elif curr[j] >= sorted_col[i] - e:
                    curr[j] = 1
                else:
                    curr[j] = 0
            new_population.append(curr)

    new_population = [list(i) for i in zip(*new_population)]
    # Start assembling new population in final_pop
    final_pop = []
    # Keep track of which population members are focal vectors
    # (i.e. directly correspond to members of original population)
    focal_vectors = []
    for j, sol in enumerate(new_population):
        # If sol has a 2 in it, we need a presence
        # vector and a focal vector
        if 2 in sol:
            # The focal vector shouldn't have any 2s in it
            focal = [i if i!= 2 else 1 for i in sol]

            # Add end criteria
            for i in range(pop_size):
                # print("i ", i)
                if i == j:
                    focal.append(1)
                else:
                    focal.append(0)
                # Sol will become presence vector
                # so its end criteria are all 0s
                sol.append(0)

            # Add a presence vector and a focal vector
            # for this member of the population
            final_pop.append(sol)
            final_pop.append(focal)
            focal_vectors.append(focal)
        else:
            # No presence vector needed - this vector
            # can be treated as a focal vector

            # Add end criteria
            for i in range(pop_size):
                # print("i ", i)                
                if i == j:
                    new_population[j].append(1)
                else:
                    new_population[j].append(0)
            final_pop.append(new_population[j])
            focal_vectors.append(new_population[j])
                
    # Add timing vectors
    for vec in focal_vectors:
        for obj in range(n_cols):
            timing_vec = vec[:]
            for i in range((pop_size)*obj, (pop_size)*(obj+1)):
                timing_vec[i] = 0
            for i in range((pop_size)*n_cols, (pop_size)*n_cols + pop_size):
                timing_vec[i] = 3
            final_pop.append(timing_vec)

    return final_pop, focal_vectors


if __name__ == "__main__":
    e = .1
    #pop = [[1,1,4,4],[0,3,3,3],[1,4,0,4],[0,3,1,2]]
    #pop = [[random.randint(0,4) for i in range(4)] for j in range(4)]
    pop = [[random.random() for i in range(5)] for j in range(5)]
    #pop = [[1, .9], [.9,1], [.8, 1.1]]
    #pop = [[1, .9, .7], [.7, 1, 1], [.8,.8,.9]]
    # pop = [[1, 1], [.9, .8]]
    # pop = [[3,1],[2,2],[1,2]]
    # pop = [[1, .9,1.1], [.9,1.1, .9], [1.1,1,1]]
    probs = eco.LexicaseFitness(pop, e)
    for i in range(len(pop)):
        print(pop[i], probs[i])

    print()
    converted_pop, focal_vectors = convert(pop, e)

    converted_probs = eco.LexicaseFitness(converted_pop)

    for i in range(len(pop)):
        converted_p = converted_probs[converted_pop.index(focal_vectors[i])]
        print(probs[i], converted_p, pop[i], focal_vectors[i])
        assert (probs[i] == 0 and converted_p == 0) or (probs[i] > 0 and converted_p > 0)

    print()
    for i in range(len(converted_pop)):
        print(converted_pop[i], converted_probs[i])
