import pandas as pd
import random
from faker import Faker

# Faker instance setup
fake = Faker("en_IN")
random.seed(42)

# Load existing customers to get valid customer_ids
customers_df = pd.read_csv("datasets/customers.csv")
customer_ids = customers_df["customer_id"].tolist()

# Define options for recharge
amounts = [199, 299, 499, 699, 999]
payment_modes = ["UPI", "Credit Card", "Debit Card", "Net Banking"]

# Step 2: Generate 500 recharge records
recharges = []

for i in range(1, 501):
    recharge = {
        "recharge_id": f"R{i:04d}",
        "customer_id": random.choice(customer_ids),
        "recharge_date": fake.date_between("-1y", "today"),
        "amount": random.choice(amounts),
        "payment_mode": random.choice(payment_modes)
    }
    recharges.append(recharge)

# Step 3: Convert list to DataFrame
recharge_df = pd.DataFrame(recharges)

# Step 4: Save to CSV
recharge_df.to_csv("datasets/recharge.csv", index=False)

# Step 5: Print output & details
print("Recharge dataset generated successfully!\n")
print(recharge_df.head())
print("\nTotal Recharge Records:", len(recharge_df))