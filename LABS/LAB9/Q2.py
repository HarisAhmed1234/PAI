import matplotlib.pyplot as plt

city_names = ['Metropolis A', 'Metropolis B', 'Metropolis C', 'Metropolis D', 'Metropolis E']
city_populations = [1200000, 850000, 500000, 3000000, 1500000]

plt.figure(figsize=(10, 6))
plt.barh(city_names, city_populations, color='lightcoral')  
plt.title('City Populations')
plt.xlabel('Population Count')
plt.ylabel('City Names')
plt.grid(axis='x', linestyle='--')

plt.tight_layout()
plt.show()
