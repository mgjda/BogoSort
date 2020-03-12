import random
import Bogosort
import time
import numpy as npy

xyDic = {}

times = []
for v in range(20):
    j = 10
    start = time.time_ns()
    tab = [0] * j
    for i in range(len(tab)):
        tab[i] = random.randint(1, 9)
    print("Will sort array that contain:", *tab)
    print(Bogosort.bogosort(tab))
    end = time.time_ns()
    times.append((end - start))
print(times)
print("Avg. time =",npy.average(times),"ns")

