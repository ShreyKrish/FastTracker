import matplotlib.pyplot as plt

# Define your data
node_expansions = {
    'Repeated Forward A*': [1, 2, 3, 4, 5],
    'Repeated Backwards A*': [2, 3, 4, 5, 6],
    'Adaptive A*': [3, 4, 5, 6, 7]
}

time_taken = {
    'Repeated Forward A*': [10, 20, 30, 40, 50],
    'Repeated Backwards A*': [20, 30, 40, 50, 60],
    'Adaptive A*': [30, 40, 50, 60, 70]
}

# Creating box plots
fig, axs = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Box Plots for Algorithms\' Metrics')

# Labels for subplots
labels = list(node_expansions.keys())

# Generate box plots for Node Expansions
for i, key in enumerate(node_expansions):
    axs[0, i].boxplot(node_expansions[key], patch_artist=True)
    axs[0, i].set_title(f'{labels[i]} - Node Expansions')
    axs[0, i].set_xticklabels([labels[i]])
    axs[0, i].set_ylabel('Node Expansions')

# Generate box plots for Time Taken
for i, key in enumerate(time_taken):
    axs[1, i].boxplot(time_taken[key], patch_artist=True)
    axs[1, i].set_title(f'{labels[i]} - Time Taken')
    axs[1, i].set_xticklabels([labels[i]])
    axs[1, i].set_ylabel('Time Taken (seconds)')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()