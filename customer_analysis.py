import pandas as pd

df = pd.read_csv("customers.csv")

print(df)

high_value = df[df["SpendingScore"] > 75]

print("\nHigh Value Customers")
print(high_value)

average_income = df["AnnualIncome"].mean()

print("\nAverage Income")
print(average_income)

def segment_customer(score):
    if score >= 80:
        return "Premium"
    elif score >= 60:
        return "Regular"
    else:
        return "Low Value"

df["Segment"] = df["SpendingScore"].apply(segment_customer)

print(df[["CustomerID", "Segment"]])
