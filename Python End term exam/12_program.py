# using matplotlib without numpy ,write a code
    # Generate 300 random(x,y) points
    # Divide the plot into four quadrants using line
    # Count the display number of points in each quadrant on the graph
    #reomve top and right borders

import  matplotlib.pyplot as plt
import random
# Generate 300 random (x, y) points
points = [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(300)]
# Separate points into quadrants
quadrant_counts = [0, 0, 0, 0]  # Q1, Q2, Q3, Q4
for x, y in points:
    if x > 0 and y > 0:
        quadrant_counts[0] += 1  # Q1
    elif x < 0 and y > 0:
        quadrant_counts[1] += 1  # Q2
    elif x < 0 and y < 0:
        quadrant_counts[2] += 1  # Q3
    elif x > 0 and y < 0:
        quadrant_counts[3] += 1  # Q4
# Plotting
plt.figure(figsize=(8, 8))
# Plot points
x_values, y_values = zip(*points)
plt.scatter(x_values, y_values, c='blue', alpha=0.5)
# Draw quadrant lines
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
# Remove top and right borders
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
# Display quadrant counts
for i, count in enumerate(quadrant_counts):
    plt.text(-8 + i * 4, 8, f"Q{i+1}: {count}", fontsize=12)
plt.title("Random Points in Quadrants")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid()
plt.show()


