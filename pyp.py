import matplotlib.pyplot as plt

color = '#fd79a8'

plt.figure(figsize=(20, 8))

# --------
# plt.subplot(2, 5, 1)
# plt.subplot(2, 5, 3)
# plt.subplot(2, 5, 5)

# -------C-------
plt.subplot(2, 7, 1)
circle1 = plt.Circle((0, 0), 0.2, color=color, fill=False, linewidth=30)
ax = plt.gca()
ax.add_patch(circle1)
# plt.axis('scaled')
plt.xlim(-0.25, 0.1)
plt.ylim(-0.25, 0.3)

# -------8-------
plt.subplot(2, 7, 2)
circle1 = plt.Circle((0.047, 0.1), 0.1, color='r', fill=False, linewidth=30)
ax = plt.gca()
ax.add_patch(circle1)
# plt.axis('scaled')
circle2 = plt.Circle((0.047, -0.1), 0.1, color='r', fill=False, linewidth=30)
ax = plt.gca()
ax.add_patch(circle2)
plt.xlim(-0.1, 0.2)
plt.ylim(-0.25, 0.25)

# -------M-------
plt.subplot(2, 7, 3)
x = [1, 1, 5, 9, 9]
y = [1, 8, 4, 8, 1]
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.plot(x, y, color=color, linewidth=30)

# -------A-------
plt.subplot(2, 7, 4)
x = [5, 3, 1, 5, 9, 7, 5]
y = [4.5, 4.5, 1, 8, 1, 4.5, 4.5]
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.plot(x, y, color=color, linewidth=30)

# -------P-------
plt.subplot(2, 7, 5)
circle1 = plt.Circle((0.047, 0.055), 0.1, color=color, fill=False, linewidth=30)
ax = plt.gca()
ax.add_patch(circle1)
# plt.axis('scaled')
plt.xlim(-0.1, 0.2)
plt.ylim(-0.25, 0.25)
plt.plot([-0.05, -0.05], [0.05, -0.2], linewidth=30, color=color)

# -------T-------
plt.subplot(2, 7, 6)
x = [1, 10, 5, 5]
y = [8, 8, 8, 1]

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.plot(x, y, linewidth=30, color=color)

# -------A-------
plt.subplot(2, 7, 7)
x = [5, 3, 1, 5, 9, 7, 5]
y = [4.5, 4.5, 1, 8, 1, 4.5, 4.5]
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.plot(x, y, color=color, linewidth=30)