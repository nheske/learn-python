import matplotlib.pyplot as plt
import numpy as np

# sample data
x = np.linspace(0.0, 100, 50)
y = np.random.uniform(low=0, high=10, size=50)

# create figure and axes
fig, axes = plt.subplots(1, 2, gridspec_kw={'width_ratios': [3, 4]})

ax1 = axes[0]
ax2 = axes[1]

ax1.set_xlabel('x1')
ax1.set_ylabel('y1')
ax2.set_xlabel('x2')
ax2.set_ylabel('y2')

ax1.set_title('box')
ax2.set_title('bouncing ball')
# just plot things on each individual axes
ax1.scatter(x, y, c='red', marker='+')
ax2.bar(x, y)

plt.show()
