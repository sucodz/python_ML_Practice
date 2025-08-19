# Scatter plot
x_scatter = np.random.rand(50)  # 50 random x values
y_scatter = np.random.rand(50)  # 50 random y values
plt.scatter(x_scatter, y_scatter, color="red", marker="o")
plt.title("Scatter Plot Example")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
