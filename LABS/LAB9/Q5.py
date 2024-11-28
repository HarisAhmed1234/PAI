import matplotlib.pyplot as plt

genders = ['Male', 'Female', 'Male', 'Female', 'Female', 'Male', 
           'Female', 'Male', 'Male', 'Female', 'Female', 'Male']

male_count = genders.count('Male')
female_count = genders.count('Female')

gender_distribution = [male_count, female_count]

#pie chart
plt.figure(figsize=(8, 6))
plt.pie(
    gender_distribution,
    labels=['Male', 'Female'],
    autopct='%1.1f%%',
    startangle=120,
    colors=['#5DADE2', '#F1948A']
)
plt.title('Student Gender Distribution')
plt.axis('equal') 
plt.show()
