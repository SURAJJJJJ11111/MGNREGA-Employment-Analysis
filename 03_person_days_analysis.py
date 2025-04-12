# Title: Person-Days Analysis
# Description: Analyze the total person-days of employment and contributions from central and state governments.
# Objective: Compare total person-days of employment with central and state government contributions.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\suraj\Downloads\employment-generated.csv")

# Aggregate employment person-days at the state level
person_days = df.groupby("state_name")[["emp_avail_tot_persondays", "emp_avail_central_persondays", "emp_avail_states_persondays"]].sum().reset_index()

# Melt data for better visualization
melted_data = person_days.melt(id_vars="state_name", var_name="Category", value_name="Total Person-Days")

# Plot employment distribution across states
plt.figure(figsize=(16, 8))  # Increased figure size for better spacing
ax = sns.barplot(data=melted_data, x="state_name", y="Total Person-Days", hue="Category", 
                 palette={"emp_avail_tot_persondays": "blue", 
                          "emp_avail_central_persondays": "green", 
                          "emp_avail_states_persondays": "red"})

# Improve legend formatting
handles, labels = ax.get_legend_handles_labels()
plt.legend(handles, ["Total Person-Days", "Central Contribution", "State Contribution"], title="Category")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha="right", fontsize=10)  # Adjusted font size for clarity

# Improve title and labels
plt.title("Total Person-Days vs. Central and State Government Contribution", fontsize=14, fontweight="bold")
plt.xlabel("State", fontsize=12, labelpad=15)  # Increased label padding
plt.ylabel("Total Person-Days", fontsize=12)

# Show plot
plt.show()
