# Employment Gap Analysis using MGNREGA Data

# Objective: Analyze state-wise employment demand and actual employment provided to identify gaps.
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\suraj\Downloads\employment-generated.csv")

# Group data by state and sum employment demand vs. provided
statewise_data = df.groupby('state_name')[['emp_demand_hh', 'emp_offer_hh']].sum().reset_index()

# Calculate gap percentage
statewise_data['gap_percentage'] = (
    (statewise_data['emp_demand_hh'] - statewise_data['emp_offer_hh']) / statewise_data['emp_demand_hh']
) * 100

# Sort states by highest employment gap
statewise_data = statewise_data.sort_values(by='gap_percentage', ascending=False)

# Plot the results
plt.figure(figsize=(12, 6))

plt.barh(statewise_data['state_name'], statewise_data['gap_percentage'], color='salmon')

# Labels and Titles
plt.xlabel('Employment Gap Percentage', fontsize=12, fontweight='bold')
plt.ylabel('State', fontsize=12, fontweight='bold')
plt.title('State-wise MGNREGA Employment Demand vs. Provided', fontsize=14, fontweight='bold', color='darkred')

# Invert Y-axis to show highest gaps at the top
plt.gca().invert_yaxis()

# Add Grid for better readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
