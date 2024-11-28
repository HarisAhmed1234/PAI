import matplotlib.pyplot as plt

math_scores = [85, 78, 91, 83, 76, 95, 89, 72, 91, 83]
science_scores = [80, 75, 90, 85, 70, 93, 88, 78, 94, 82]

plt.scatter(math_scores, science_scores, color='green', label='Scores')

plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')

plt.title('Comparison of Mathematics and Science Marks')

plt.legend()

plt.show()
