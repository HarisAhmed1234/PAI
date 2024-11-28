import matplotlib.pyplot as plt

time_period = [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
sea_level_data = [0, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60]

plt.scatter(time_period, sea_level_data, color='darkcyan', label='Sea Level Increase')

plt.xlabel('Year')
plt.ylabel('Sea Level Rise (mm)')

plt.title('Rise in Sea Level Over 100 Years')

plt.legend()

plt.show()
