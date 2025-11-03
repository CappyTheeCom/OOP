import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,4])
ypoints = np.array([4,10])

plt.plot(xpoints,ypoints)
plt.show()


xpoints = np.array([1,2,3,4,5,6])
ypoints = np.array([1,3,6,8,2,10])

plt.plot(xpoints,ypoints)
plt.show()

plt.plot(xpoints,ypoints,marker = 'o')
plt.show()


y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)


x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)

if __name__ == __main__:
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.show()

    
