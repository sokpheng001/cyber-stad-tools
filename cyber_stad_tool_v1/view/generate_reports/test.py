import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 40, 15, 20]

# Custom colors for each bar
colors = ['blue', 'green', 'orange', 'red']

# Create a bar chart with custom colors
plt.bar(categories, values, color=colors)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart with Custom Colors')

# Show the plot
plt.show()
