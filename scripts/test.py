import reduce_sat_to_eps as sat_to_eps
import reduce_eps_to_lex as eps_to_lex
import ec_ecology_toolbox as eco
import random
from pysat.solvers import Solver


def random_eps_to_lex(e):
    pop = [[random.random() for i in range(5)] for j in range(5)]

    probs = eco.LexicaseFitness(pop, e)
    converted_pop, focal_vectors = eps_to_lex.convert(pop, e)
    converted_probs = eco.LexicaseFitness(converted_pop)

    for i in range(len(pop)):
        converted_p = converted_probs[converted_pop.index(focal_vectors[i])]
        assert ((probs[i] == 0) and (converted_p == 0)) or ((probs[i] > 0) and (converted_p > 0))


def test_eps_to_lex():
    random_eps_to_lex(.1)
    random_eps_to_lex(.2)
    random_eps_to_lex(.3)
    random_eps_to_lex(.4)
    random_eps_to_lex(.5)


def test_sat_to_eps_simple_true():
    variables = ["X1", "X2"]
    clauses = [["X1"], ["!X1", "X2"]]

    pop = sat_to_eps.convert(variables, clauses)
    probs = eco.LexicaseFitness(pop, .1)

    assert probs[0] > 0


def test_sat_to_eps_simple_false():
    variables = ["X1", "X2"]
    clauses = [["X1"], ["!X1", "X2"], ["!X2"]]

    pop = sat_to_eps.convert(variables, clauses)
    probs = eco.LexicaseFitness(pop, .1)

    assert probs[0] == 0


def test_sat_to_eps_random():

    s = Solver()

    variables = []
    clauses = []

    for i in range(random.randint(1, 8)):
        c = []
        for j in range(random.randint(1, 3)):
            n = random.randint(1, 4)
            if random.random() < .5:
                n *= -1
            c.append(n)
        print(c)
        s.add_clause(c)
        clause = []
        for num in c:
            if num < 0:
                num *= -1
                clause.append(f"!X{num}")
            else:
                clause.append(f"X{num}")
        clauses.append(clause)
        variables += clause

    variables = list(set(variables))
    print(clauses, variables)

    pop = sat_to_eps.convert(variables, clauses)
    print(pop)
    prob = eco.LexicaseFitness(pop, .1)
    print(prob[0], s.solve())
    assert (prob[0] != 0) == s.solve()
