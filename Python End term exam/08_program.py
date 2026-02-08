# Using Matplotlib, write code to create a figure with 3 vertical subplots:
# Original (x, y) line plot
# Cumulative sum of y values plotted vs x
# Absolute difference between consecutive y values 

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
import matplotlib.pyplot as plt



fig, axs = plt.subplots(3, 1, figsize=(8, 12))
# Original (x, y) line plot
axs[0].plot(x, y, marker='o')
axs[0].set_title('Original (x, y) Line Plot')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')

# Cumulative sum of y values plotted vs x
cumulative_sum = [sum(y[:i+1]) for i in range(len(y))]
axs[1].plot(x, cumulative_sum, marker='o', color='orange')
axs[1].set_title('Cumulative Sum of y Values vs x')
axs[1].set_xlabel('x')
axs[1].set_ylabel('Cumulative Sum of y')


# Absolute difference between consecutive y values
absolute_diff = [abs(y[i] - y[i-1]) for i in range(1, len(y))]
axs[2].plot(x[1:], absolute_diff, marker='o', color='green')
axs[2].set_title('Absolute Difference Between Consecutive y Values')
axs[2].set_xlabel('x')
axs[2].set_ylabel('Absolute Difference of y')
plt.tight_layout()
plt.show()
