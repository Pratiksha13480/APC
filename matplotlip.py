
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

# Create 3 rows and 3 columns of subplots
plt.figure(figsize=(12, 10))

# 1. Line Graph
plt.subplot(3, 3, 1)
plt.plot(x, y, color="blue", marker="o")
plt.title("Line Graph")

# 2. Bar Graph
plt.subplot(3, 3, 2)
plt.bar(x, y, color="green")
plt.title("Bar Graph")

# 3. Scatter Plot
plt.subplot(3, 3, 3)
plt.scatter(x, y, color="red")
plt.title("Scatter Plot")

# 4. Histogram
plt.subplot(3, 3, 4)
plt.hist(y, bins=5, color="orange", edgecolor="black")
plt.title("Histogram")

# 5. Pie Chart
plt.subplot(3, 3, 5)
plt.pie(y, labels=x, autopct="%1.1f%%")
plt.title("Pie Chart")

# 6. Horizontal Bar Graph
plt.subplot(3, 3, 6)
plt.barh(x, y, color="purple")
plt.title("Horizontal Bar")

# 7. Area Graph
plt.subplot(3, 3, 7)
plt.fill_between(x, y, color="skyblue", alpha=0.7)
plt.plot(x, y, color="blue")
plt.title("Area Graph")

# 8. Step Graph
plt.subplot(3, 3, 8)
plt.step(x, y, color="brown", where="mid")
plt.title("Step Graph")

# 9. Box Plot
plt.subplot(3, 3, 9)
plt.boxplot(y)
plt.title("Box Plot")

# Adjust spacing
plt.tight_layout()

# Display all graphs
plt.show()