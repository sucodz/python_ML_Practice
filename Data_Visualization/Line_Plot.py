import numpy as np
import matplotlib.pyplot as plt

# Example data
x = np.linspace(0, 10, 100)   # 100 points from 0 to 10
y = np.sin(x)

# Line plot
plt.plot(x, y, label="sin(x)")
plt.title("Line Plot Example")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.show()
