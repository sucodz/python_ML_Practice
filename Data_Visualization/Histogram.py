# Histogram
data = np.random.randn(1000)  # 1000 random values from normal distribution
plt.hist(data, bins=30, color="skyblue", edgecolor="black")
plt.title("Histogram Example ")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
