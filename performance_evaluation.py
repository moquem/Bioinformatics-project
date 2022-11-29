import numpy as np
import matplotlib.pyplot as plt
import time
from random_newick_tree import random_newick_tree
from minimal_crossing import OTCM


N_MAX = 11
N_AVG = 100
X = np.array([int(np.sqrt(10)**i) for i in range(N_MAX)])

avg_time = np.zeros(N_MAX)
worst_time = np.zeros(N_MAX)
avg_conflict = np.zeros(N_MAX)

for i in range(N_MAX):
    print("Executing on tree of size",int(np.sqrt(10)**i))
    avg_t = 0
    avg_c = 0
    worst_t = 0
    for j in range(1,N_AVG):
        nT = random_newick_tree(int(np.sqrt(10)**i))
        start = time.time()
        m,_ = OTCM(nT)
        end = time.time()
        worst_t = max(worst_t,end-start)
        avg_t = (avg_t*(j-1)+(end-start))/j
        avg_c = (avg_c*(j-1)+m)/j
    avg_time[i] = avg_t
    worst_time[i] = worst_t
    avg_conflict[i] = avg_c

plt.subplot(211)
plt.yscale('log')
plt.xscale('log')
plt.scatter(X,avg_time,s=2)
plt.ylabel("Time of execution")
plt.scatter(X,worst_time,color='orange',s=2)
plt.plot()


plt.subplot(212)
plt.plot(X,avg_conflict)
plt.xlabel("Size of the newick tree")
plt.ylabel("Number of conflicts")
plt.plot()

plt.savefig('perfomance_evaluation_2.png')


    