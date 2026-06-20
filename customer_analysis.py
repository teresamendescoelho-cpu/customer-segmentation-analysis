import pandas as pd

df = pd.read_csv("customers.csv")

print(df)

high_value = df[df["SpendingScore"] > 75]

print("\nHigh Value Customers")
print(high_value)

average_income = df["AnnualIncome"].mean()

print("\nAverage Income")
print(average_income)
