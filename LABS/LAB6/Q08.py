import pandas as pd

#part A
products_df = pd.read_csv('products.csv')
orders_df = pd.read_csv('orders.csv')

#part B
print("First 5 rows of products_df:")
print(products_df.head())
print("\nLast 10 rows of products_df:")
print(products_df.tail(10))

print("\nFirst 5 rows of orders_df:")
print(orders_df.head())
print("\nLast 10 rows of orders_df:")
print(orders_df.tail(10))

#part C
merged_df = pd.merge(orders_df, products_df, on='ProductID')
merged_df['Revenue'] = merged_df['Quantity'] * merged_df['Price']
total_revenue = merged_df['Revenue'].sum()
print(f"\nTotal revenue generated: {total_revenue}")

#part D
product_sales = merged_df.groupby('ProductID').agg(Total_Quantity=('Quantity', 'sum')).reset_index()
top_5_best_selling = product_sales.sort_values(by='Total_Quantity', ascending=False).head(5)
top_5_low_selling = product_sales.sort_values(by='Total_Quantity', ascending=True).head(5)
print("\nTop 5 best-selling products:")
print(top_5_best_selling)

print("\nTop 5 low-selling products:")
print(top_5_low_selling)

#part E
best_selling_products = pd.merge(top_5_best_selling, products_df, on='ProductID')
most_common_category = best_selling_products['Category'].mode()[0]
print(f"\nMost common product category among the top 5 best-selling products: {most_common_category}")

#part F
average_price_per_category = products_df.groupby('Category')['Price'].mean().reset_index()
print("\nAverage price of products in each category:")
print(average_price_per_category)

#part G
merged_df['OrderDate'] = pd.to_datetime(merged_df['OrderDate'])
merged_df['Year'] = merged_df['OrderDate'].dt.year
merged_df['Month'] = merged_df['OrderDate'].dt.month
merged_df['Day'] = merged_df['OrderDate'].dt.day

revenue_by_day = merged_df.groupby(['Year', 'Month', 'Day'])['Revenue'].sum().reset_index()
max_revenue_day = revenue_by_day.sort_values(by='Revenue', ascending=False).iloc[0]
print(f"\nDay with the highest total revenue: {max_revenue_day['Day']}")
print(f"Month with the highest total revenue: {max_revenue_day['Month']}")
print(f"Year with the highest total revenue: {max_revenue_day['Year']}")

#part H
monthly_revenue = merged_df.groupby(['Year', 'Month'])['Revenue'].sum().reset_index()
print("\nMonthly total revenue:")
print(monthly_revenue)

#part I
print("\nChecking for null values:")
print("Products DataFrame:\n", products_df.isnull().sum())
print("Orders DataFrame:\n", orders_df.isnull().sum())

# Drop rows if nill
products_df_clean = products_df.dropna()
orders_df_clean = orders_df.dropna()
