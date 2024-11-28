import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [3, 4, 7, 10, 12, 18, 24, 32, 40, 50]
y2 = [2, 3, 5, 8, 10, 14, 20, 28, 35, 45]

plt.plot(x, y1, color='pink', marker='o', label='First Line')

plt.plot(x, y2, color='gray', marker='o', label='Second Line')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')

plt.title('Two Lines on One Graph')
plt.legend(loc='lower right')

plt.show()
