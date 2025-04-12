# Socio-Economic Impact
#Discription: The dataset contains the number of job cards issued to households in a region. The job cards are issued to households belonging to different social categories such as Scheduled Castes (SC), Scheduled Tribes (ST), and others. The dataset also contains the total number of job cards issued to each social category. The objective is to analyze the distribution of job cards by social category using a pie chart.
#Objective: To analyze the distribution of job cards by social category
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
# df = pd.read_csv("your_dataset.csv")
df = pd.read_csv(r"C:\Users\suraj\Downloads\employment-generated.csv")
# Total job cards for each social category
social_category = df[["cumul_hh_jobcards_sc", "cumul_hh_jobcards_sts", "cumul_hh_jobcards_others"]].sum()

# Pie chart for distribution
plt.figure(figsize=(6,6))
labels = ["SC Households", "ST Households", "Other Households"]
colors = ["purple", "orange", "green"]

plt.pie(social_category, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140)
plt.title("Distribution of Job Cards by Social Category")
plt.show()
