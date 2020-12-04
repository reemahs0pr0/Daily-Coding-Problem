# The area of a circle is defined as πr^2. Estimate π to 3 decimal 
# places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.

import numpy as np
import matplotlib.pyplot as plt

N = np.arange(0, 500)
pi = []

for n in N:
    x_arr = np.random.random(n)
    y_arr = np.random.random(n)
    
    r_square_in_quadrant = []
    
    for i in range(n):
        val = x_arr[i] ** 2 + y_arr[i] ** 2
        if val <= 1:
            r_square_in_quadrant.append(val)
    pi.append(len(r_square_in_quadrant) * 4 / n)
    
fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)
ax.plot(N, pi, color='red', linewidth=1)
ax.set(title='Pi vs SampleNo', ylabel='Pi', xlabel='SamplesNo')
plt.show()

print(pi)