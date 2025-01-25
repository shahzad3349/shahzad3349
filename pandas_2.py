import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("E:/matplotlib/ecommerce_data.csv")

data = data.dropna(subset=['Product', 'Category', 'Sales', 'Rating'])

data['Revenue'] = data['Sales'] * data['Price']

best_sellers = data.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5)
print("Top 5 Best-Selling Products:")
print(best_sellers)

avg_rating = data.groupby('Category')['Rating'].mean()
print("Average Rating by Category:")
print(avg_rating)

best_sellers.plot(kind='pie', title='Top 5 Best-Selling Products',autopct='%1.2f%%' ,color='skyblue')
plt.show()

sns.heatmap(data[['Sales', 'Price', 'Rating', 'Revenue']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()