import example
import random
import timeit

N = 10
M = 10

pop = [[random.randint(0,4) for i in range(M)] for j in range(N)]

def setup():
    global pop
    pop = [[random.randint(0,4) for i in range(M)] for j in range(N)]

def test():
    example.LexicaseFitness(pop)

print("N,M,time")

for N in range(1, 60):
    for M in range(1, 60):
        results = timeit.repeat(test, setup=setup, number=1, repeat=100)
        for res in results:
            print(",".join([str(i) for i in [N, M, res]]))