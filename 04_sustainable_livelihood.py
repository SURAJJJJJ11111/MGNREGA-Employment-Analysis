# 100 Days Job Completion & Benefits
'''Discription: The dataset contains information about the completion of 100 days of employment and additional benefits provided to households in different states.
 The dataset includes the number of households that completed 100 days of employment, the number of households benefiting from land reforms, and the'
  number of individuals receiving support for disabilities. The objective is to analyze the completion of 100 days of employment and additional'
   benefits provided to households in different states.'''
#Objective: Analyze the completion of 100 days employment and additional benefits provided.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\suraj\Downloads\employment-generated.csv")

# Aggregate data for 100 days completion and additional benefits
hundred_days = df.groupby("state_name")[["fam_completed_100_days", "land_reform_benef_hh", "disabled_benef_indiv"]].sum().reset_index()

# Melt data for better visualization
melted_data = hundred_days.melt(id_vars="state_name", var_name="Category", value_name="Number of Beneficiaries")

# Plot effectiveness in livelihood support
plt.figure(figsize=(14, 7))
ax = sns.barplot(data=melted_data, x="state_name", y="Number of Beneficiaries", hue="Category", 
                 palette={"fam_completed_100_days": "purple", "land_reform_benef_hh": "orange", "disabled_benef_indiv": "brown"})

# Improve legend formatting
handles, labels = ax.get_legend_handles_labels()
plt.legend(handles, ["100 Days Employment", "Land Reform Beneficiaries", "Disabled Support"], title="Category")

# Rotate x-axis labels for better readability
plt.xticks(rotation=90, ha="right")

# Improve title and labels
plt.title("100 Days Employment Completion and Additional Benefits", fontsize=14, fontweight="bold")
plt.xlabel("State", fontsize=12)
plt.ylabel("Number of Beneficiaries", fontsize=12)

# Show plot
plt.show()

