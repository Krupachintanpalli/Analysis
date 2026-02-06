import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the CSV file
data = pd.read_csv("Employee.csv")

# 2. Show the data
print("Data:\n", data)

# 3. Calculate average salary
print("\nAverage PaymentTier:", data["PaymentTier"].mean())

# 4. Bar chart: Average salary by department
data.groupby("Age")["PaymentTier"].mean().plot(kind="bar")
plt.title("Average PaymentTier by age")
plt.show()


# 5. Scatter plot: Age vs Salary
plt.scatter(data["Age"], data["PaymentTier"])
plt.title("Age vs PaymentTier")
plt.xlabel("Age")
plt.ylabel("PaymentTier")
plt.show()

# 6. Heatmap: Correlation between Age and Salary
sns.heatmap(data[["Age","PaymentTier"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()