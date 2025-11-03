import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c', 'group_d']
values = [10, 50, 100, 70]

plt.subplot(2,2,1)
plt.bar(names, values)
plt.subplot(2,2,2)
plt.barh(names, values)
plt.subplot(2,2,3)
plt.bar(names, values, color='red', width=0.5)
plt.subplot(2,2,4)
plt.barh(names, values, color='blue', height=0.2)
plt.suptitle('Bars and H-Bars')
plt.show()
