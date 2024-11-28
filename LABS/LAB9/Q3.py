import matplotlib.pyplot as plt

ice_cream_flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough']
sales_data = [150, 100, 80, 60, 90]

#pie chart
plt.figure(figsize=(8, 6))
plt.pie(sales_data, labels=ice_cream_flavors, autopct='%1.1f%%', startangle=120, colors=['#FFD700', '#8B4513', '#FF69B4', '#98FB98', '#D3D3D3']) 
plt.title('Ice Cream Sales Distribution')
plt.axis('equal') 
plt.show()
