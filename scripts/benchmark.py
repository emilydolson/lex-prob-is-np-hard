import ec_ecology_toolbox as eco
import random
import timeit
import sys

N = int(sys.argv[1])
M = int(sys.argv[2])

pop = [[random.randint(0,4) for i in range(M)] for j in range(N)]

def setup():
    global pop
    pop = [[random.randint(0,4) for i in range(M)] for j in range(N)]

def test():
    eco.LexicaseFitness(pop)

# print("N,M,time")

results = timeit.repeat(test, setup=setup, number=1, repeat=100)
for res in results:
    print(",".join([str(i) for i in [N, M, res]]))