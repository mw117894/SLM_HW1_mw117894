import numpy as np
import time
import statistics as st
import matplotlib.pyplot as plt
from sklearn import linear_model

sizes = list(range(10,210,10))
reps = 10000
def sim_r_squared(n):
    x = np.random.normal(size=n)
    y = x+1+np.random.normal(size=n)
    lm = linear_model.LinearRegression()
    lm.fit(X=x.reshape(-1,1),y=y)
    return lm.score(X=x.reshape(-1,1),y=y)

r_squared_mean = []
r_squared_q95 = []
r_squared_q5 = []

start_time = time.time()

for size in sizes:
    print(size)
    result = []
    for i in range(reps):
        result.append(sim_r_squared(size))
    r_squared_mean.append(st.mean(result))
    r_squared_q95.append(np.quantile(result,0.95))
    r_squared_q5.append(np.quantile(result,0.05))

print("Excecution time: "+str(time.time()-start_time))
plt.scatter(sizes, r_squared_mean)
plt.plot(sizes,r_squared_q5)
plt.plot(sizes,r_squared_q95)
plt.ylim(min(r_squared_q5),max(r_squared_q95))
plt.xlabel("sample size")
plt.ylabel("$R^2$")
plt.show()