# Employment Demand vs. Availability
#Description: Analyze the employment demand and availability across states.
#Objective: Compare employment demand and availability across states.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\suraj\Downloads\employment-generated.csv")

# Check if required columns exist
required_columns = {"state_name", "emp_demand_hh", "emp_avail_hh"}
if not required_columns.issubset(df.columns):
    print("Error: Required columns are missing in the dataset.")
else:
    # Aggregate data at the state level
    demand_vs_avail = df.groupby("state_name")[["emp_demand_hh", "emp_avail_hh"]].sum().reset_index()

    # Rename columns for better readability
    demand_vs_avail.rename(columns={"emp_demand_hh": "Employment Demand", "emp_avail_hh": "Employment Availability"}, inplace=True)

    # Melt data for visualization
    melted_data = demand_vs_avail.melt(id_vars="state_name", var_name="Category", value_name="Households")

    # Plot employment demand vs. availability
    plt.figure(figsize=(14, 6))
    sns.barplot(data=melted_data, x="state_name", y="Households", hue="Category", palette=["red", "green"])

    # Formatting the plot
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.title("Employment Demand vs. Employment Availability Across States", fontsize=14, fontweight="bold")
    plt.xlabel("State", fontsize=12)
    plt.ylabel("Number of Households", fontsize=12)
    plt.legend(title="Category")  # Ensures proper legend display
    plt.show()
