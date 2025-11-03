import matplotlib.pyplot as plt
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', label = 'linear')
plt.plot(t, t**2, 'bs', label = 'quadratic')
plt.plot(t, t**3, 'g^', label = 'cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Simple plot')
plt.legend()
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()
