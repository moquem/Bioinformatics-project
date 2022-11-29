import numpy as np
import matplotlib.pyplot as plt
import time
from random_newick_tree import random_newick_tree
from minimal_crossing import OTCM


N_MAX = 100
N_AVG = 10
X = np.array(range(N_MAX))

avg_time = np.zeros(N_MAX)
worst_time = np.zeros(N_MAX)
avg_conflict = np.zeros(N_MAX)

for i in range(1,N_MAX):
    print("Executing on tree of size",i)
    avg_t = 0
    avg_c = 0
    worst_t = 0
    for j in range(N_AVG):
        nT = random_newick_tree(i)
        start = time.time()
        m,_ = OTCM(nT)
        end = time.time()
        worst_t = max(worst_t,end-start)
        avg_t = (avg_t*(i-1)+(end-start))/i
        avg_c = (avg_c*(i-1)+m)/i
    avg_time[i] = avg_t
    worst_time[i] = worst_t
    avg_conflict[i] = avg_c

plt.subplot(211)
plt.yscale('log')
plt.xscale('log')
plt.bar(X,avg_time)
plt.ylabel("Time of execution")
plt.scatter(X,worst_time,color='orange',s=2)
plt.plot()


plt.subplot(212)
plt.bar(X,avg_conflict)
plt.xlabel("Size of the newick tree")
plt.ylabel("Number of conflicts")
plt.plot()

plt.show()


    