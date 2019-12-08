import matplotlib.pyplot as plt
import numpy as np 
f = np.linspace(0,99,100)
    
for i in range(0,100): 
    if f[i]<=9:
        f[i]=(f[i]**2)-7

    elif f[i]>=10:
        f[i]=f[i-10]

plt.stem(f, use_line_collection=True)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show