import matplotlib.pyplot as plt
import pandas as pd

# Load the data
df1 = pd.read_csv("acc_data_smoothen/site-1.csv")
df2 = pd.read_csv("acc_data_smoothen/site-2.csv")
df3 = pd.read_csv("acc_data_smoothen/site-3.csv")

# Group by Round
rounds = sorted(df1['Round'].unique())

# Set up 5 subplots side by side
fig, axes = plt.subplots(1, 5, figsize=(14, 5), sharey=True)

colors = {
    'client-1': '#1f77b4',
    'client-2': '#17becf',
    'client-3': '#e377c2',
}

for i, rnd in enumerate(rounds):
    ax = axes[i]
    # Filter data per round
    r_df1 = df1[df1['Round'] == rnd]
    r_df2 = df2[df2['Round'] == rnd]
    r_df3 = df3[df3['Round'] == rnd]

    # Plot each client
    ax.plot(r_df1['Epoch'], r_df1['Value'], color=colors['client-1'], label='client-1', linewidth=3.5)
    ax.plot(r_df2['Epoch'], r_df2['Value'], color=colors['client-2'], label='client-2', linewidth=3.5)
    ax.plot(r_df3['Epoch'], r_df3['Value'], color=colors['client-3'], label='client-3', linewidth=3.5)

    ax.set_title(f"Round {rnd}", fontsize=14, fontweight='bold')
    ax.set_xlabel("Epoch", fontsize=13)
    ax.set_xticks(range(1, 6))
    ax.tick_params(axis='both', labelsize=12)
    ax.grid(False)

    # Remove y-axis from all but first subplot
    if i > 0:
        ax.spines['left'].set_visible(False)
        ax.tick_params(left=False, labelleft=False)

# First subplot gets y-axis labels
axes[0].set_ylabel("Accuracy", fontsize=13)
axes[0].set_yticks([48, 52, 56, 60, 64])

# Clean up subplot styling
for ax in axes:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

# Show legend with increased font size
axes[-1].legend(loc='lower right', fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()


# import matplotlib.pyplot as plt
# import pandas as pd

# # Load the data
# df1 = pd.read_csv("acc_data_smoothen/site-1.csv")
# df2 = pd.read_csv("acc_data_smoothen/site-2.csv")
# df3 = pd.read_csv("acc_data_smoothen/site-3.csv")

# # Group by Round
# rounds = sorted(df1['Round'].unique())

# # Set up 5 subplots side by side
# fig, axes = plt.subplots(1, 5, figsize=(14, 5), sharey=True)

# colors = {
#     'client-1': '#1f77b4',
#     'client-2': '#17becf',
#     'client-3': '#e377c2',
# }

# for i, rnd in enumerate(rounds):
#     ax = axes[i]
#     # Filter data per round
#     r_df1 = df1[df1['Round'] == rnd]
#     r_df2 = df2[df2['Round'] == rnd]
#     r_df3 = df3[df3['Round'] == rnd]

#     # Plot each client
#     ax.plot(r_df1['Epoch'], r_df1['Value'], color=colors['client-1'], label='client-1', linewidth=3.5)
#     ax.plot(r_df2['Epoch'], r_df2['Value'], color=colors['client-2'], label='client-2', linewidth=3.5)
#     ax.plot(r_df3['Epoch'], r_df3['Value'], color=colors['client-3'], label='client-3', linewidth=3.5)

#     # ax.plot(r_df1['Epoch'], r_df1['Value'], color=colors['client-1'], label='client-1')
#     # ax.plot(r_df2['Epoch'], r_df2['Value'], color=colors['client-2'], label='client-2')
#     # ax.plot(r_df3['Epoch'], r_df3['Value'], color=colors['client-3'], label='client-3')

#     # Updated title styling
#     ax.set_title(f"Round {rnd}", fontsize=14, fontweight='bold')
#     ax.set_xlabel("Epoch")
#     ax.set_xticks(range(1, 6))
#     ax.grid(False)

#     # Remove y-axis from all but first subplot
#     if i > 0:
#         ax.spines['left'].set_visible(False)
#         ax.tick_params(left=False, labelleft=False)

# # First subplot gets y-axis labels
# axes[0].set_ylabel("Accuracy")
# axes[0].set_yticks([48, 52, 56, 60, 64])

# # Clean up subplot styling
# for ax in axes:
#     ax.spines['right'].set_visible(False)
#     ax.spines['top'].set_visible(False)

# plt.legend(loc='upper right')
# plt.tight_layout(rect=[0, 0, 1, 0.95])
# plt.show()



# import matplotlib.pyplot as plt
# import pandas as pd

# # Load the data
# df1 = pd.read_csv("acc_data_smoothen/site-1.csv")
# df2 = pd.read_csv("acc_data_smoothen/site-2.csv")
# df3 = pd.read_csv("acc_data_smoothen/site-3.csv")

# # Group by Round
# rounds = sorted(df1['Round'].unique())

# # Set up 3 subplots side by side (as in the image)
# fig, axes = plt.subplots(1, 5, figsize=(14, 5), sharey=True)

# colors = {
#     'client-1': '#1f77b4',  # yellow like in the sketch
#     'client-2': '#17becf',
#     'client-3': '#e377c2',
# }

# for i, rnd in enumerate(rounds):
#     ax = axes[i]
#     # Filter data per round
#     r_df1 = df1[df1['Round'] == rnd]
#     r_df2 = df2[df2['Round'] == rnd]
#     r_df3 = df3[df3['Round'] == rnd]

#     # Plot each client
#     ax.plot(r_df1['Epoch'], r_df1['Value'], color=colors['client-1'], label='client-1')
#     ax.plot(r_df2['Epoch'], r_df2['Value'], color=colors['client-2'], label='client-2')
#     ax.plot(r_df3['Epoch'], r_df3['Value'], color=colors['client-3'], label='client-3')

#     ax.set_title(f"Round {rnd}")
#     ax.set_xlabel("Epoch")
#     ax.set_xticks(range(1, 6))
#     ax.grid(False)

# axes[0].set_ylabel("Accuracy")
# axes[0].set_yticks([45, 50, 55, 60, 65])  # to match sketch style
# # axes[0].legend(loc='lower right')

# # Hide spines between subplots to mimic the vertical dividers in sketch
# for ax in axes:
#     ax.spines['right'].set_visible(False)
#     ax.spines['top'].set_visible(False)

# plt.suptitle("Accuracy over Rounds", fontsize=16)
# plt.tight_layout(rect=[0, 0, 1, 0.95])
# plt.show()



# import matplotlib.pyplot as plt
# import pandas as pd

# # Load the data
# df1 = pd.read_csv("acc_data_smoothen/site-1.csv")
# df2 = pd.read_csv("acc_data_smoothen/site-2.csv")
# df3 = pd.read_csv("acc_data_smoothen/site-3.csv")

# # Combine into one DataFrame with a "client" column
# df1['client'] = 'client-1'
# df2['client'] = 'client-2'
# df3['client'] = 'client-3'
# df_all = pd.concat([df1, df2, df3])

# # Compute shifted x-axis values for continuous plotting
# # Each round has 5 epochs, so shift x by (round_number - 1) * 5
# df_all['x'] = (df_all['Round'] - 1) * 5 + df_all['Epoch']

# # Set up the plot
# plt.figure(figsize=(14, 6))
# colors = {
#     'client-1': '#f1c40f',
#     'client-2': '#f39c12',
#     'client-3': '#e67e22',
# }

# # Plot each client's line
# for client in df_all['client'].unique():
#     client_df = df_all[df_all['client'] == client]
#     plt.plot(client_df['x'], client_df['Value'], label=client, color=colors[client])

# # Add vertical separators for round boundaries
# rounds = sorted(df_all['Round'].unique())
# for r in rounds[1:]:
#     plt.axvline(x=(r - 1) * 5 + 0.5, color='gold', linestyle='-', linewidth=1.5)



# # Format the plot
# plt.xticks([(r - 1) * 5 + i for r in rounds for i in range(1, 6)],
#            [str(i) for _ in rounds for i in range(1, 6)])
# plt.xlabel("Epoch")
# plt.ylabel("Accuracy")
# plt.title("Accuracy over Rounds (Continuous)")
# plt.legend()
# plt.grid(False)
# plt.tight_layout()
# plt.show()


import matplotlib.pyplot as plt
import pandas as pd

# Load the data
df1 = pd.read_csv("acc_data_smoothen/site-1.csv")
df2 = pd.read_csv("acc_data_smoothen/site-2.csv")
df3 = pd.read_csv("acc_data_smoothen/site-3.csv")

# Combine into one DataFrame with a "client" column
df1['client'] = 'client-1'
df2['client'] = 'client-2'
df3['client'] = 'client-3'
df_all = pd.concat([df1, df2, df3])

# Compute shifted x-axis values for continuous plotting
df_all['x'] = (df_all['Round'] - 1) * 5 + df_all['Epoch']

# Set up the plot
plt.figure(figsize=(14, 6))
colors = {
    'client-1': '#1f77b4',
    'client-2': '#17becf',
    'client-3': '#e377c2',
}

# Plot each client's line
for client in df_all['client'].unique():
    client_df = df_all[df_all['client'] == client]
    plt.plot(client_df['x'], client_df['Value'], label=client, color=colors[client])

# Add vertical separators for round boundaries
rounds = sorted(df_all['Round'].unique())
for r in rounds[1:]:
    plt.axvline(x=(r - 1) * 5 + 0.5, color='black', linestyle='-', linewidth=1.5)

# Add round titles above each section
for r in rounds:
    x_pos = (r - 1) * 5 + 2.5  # midpoint of each round
    plt.text(x_pos, plt.ylim()[1] + 1, f"Round {r}", ha='center', va='bottom', fontweight='bold',
             fontsize=14, color='black')

# Final formatting
plt.xticks([(r - 1) * 5 + i for r in rounds for i in range(1, 6)],
           [str(i) for _ in rounds for i in range(1, 6)])
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
# plt.title("Accuracy over Rounds (Continuous)")
plt.legend()
plt.grid(False)
plt.tight_layout()
plt.show()
