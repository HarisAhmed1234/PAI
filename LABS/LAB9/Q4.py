import matplotlib.pyplot as plt

ages = [18, 27, 23, 30, 28, 19, 18, 31, 42, 21, 28, 27, 19, 39, 22, 21, 36, 37, 40, 19]

age_brackets = ['18-25', '26-30', '31-35', '36 and above']

count_18_25 = sum(1 for age in ages if 18 <= age <= 25)
count_26_30 = sum(1 for age in ages if 26 <= age <= 30)
count_31_35 = sum(1 for age in ages if 31 <= age <= 35)
count_36_plus = sum(1 for age in ages if age >= 36)

age_group_counts = [count_18_25, count_26_30, count_31_35, count_36_plus]

plt.figure(figsize=(8, 6))
plt.pie(
    age_group_counts,
    labels=age_brackets,
    autopct='%1.1f%%',
    startangle=130,
    colors=['#FAD7A0', '#F5B7B1', '#AED6F1', '#D5F5E3']
)
plt.title('Student Age Distribution')
plt.axis('equal') 
plt.show()
