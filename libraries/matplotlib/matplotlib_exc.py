import matplotlib.pyplot as plt
import numpy as np

# a=np.array([1,2,3,4,5,6,7,12])
# b=plt.plot(a)
# plt.show()
# print(b)

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# X = np.arange(-5, 5, 0.15)
# Y = np.arange(-5, 5, 0.15)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)

r=ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
print(r)
plt.show()

# a=[10,20,30,15]
# b=plt.hist(a,bins=30, edgecolor='black')
# plt.title("Histogram")
# plt.xlabel("Value")
# plt.ylabel("Data")
# plt.show()

labels = ['Python', 'Java', 'C++']
sizes = [40, 35, 25]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart")
plt.show()




# Data
# x = [1, 2, 3, 4, 5]
# y1 = [1, 4, 9, 16, 25]
# y2 = [1, 2, 3, 4, 5]

# # Plotting with labels
# plt.plot(x, y1, label='Squares')
# plt.plot(x, y2, label='Linear')

# # Add legend
# plt.legend()

# # Title and axis labels
# plt.title("Line Comparison")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")

# plt.show()
