import matplotlib.pyplot as plt
import numpy as np

student_names = ['Pupil ' + str(i) for i in range(1, 21)]
student_heights = [150, 160, 165, 170, 155, 180, 175, 160, 168, 158,
                   162, 170, 172, 158, 165, 174, 160, 159, 167, 173]

bar_colors = np.random.rand(len(student_names), 3)

# Bar chart
plt.figure(figsize=(12, 6))
plt.bar(student_names, student_heights, color=bar_colors)
plt.title('Heights of Students - Bar Chart')
plt.xlabel('Student Names')
plt.ylabel('Height (cm)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pie chart
plt.figure(figsize=(9, 9))
plt.pie(student_heights, labels=student_names, autopct='%1.1f%%')
plt.title('Heights of Students - Pie Chart')
plt.axis('equal')
plt.show()
