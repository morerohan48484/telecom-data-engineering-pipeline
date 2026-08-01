import pandas as pd
import random
from faker import Faker

fake = Faker("en_IN")
random.seed(42)

# Read customer dataset
customers_df = pd.read_csv("datasets/customers.csv")
customer_ids = customers_df["customer_id"].tolist()

# Define issue types and statuses
issue_types = [
    "Network Issue",
    "Call Drop",
    "Slow Internet",
    "Billing Issue",
    "Recharge Failed",
    "SIM Activation",
    "SMS Not Working"
]

statuses = [
    "Resolved",
    "Pending",
    "Open"
]

# Generate 200 complaints
complaints = []

for i in range(1, 201):
    complaint = {
        "complaint_id": f"C{i:04d}",
        "customer_id": random.choice(customer_ids),
        "complaint_date": fake.date_between("-1y", "today"),
        "issue_type": random.choice(issue_types),
        "status": random.choice(statuses),
        "resolution_days": random.randint(0, 15)
    }
    complaints.append(complaint)

# Convert list to DataFrame
complaints_df = pd.DataFrame(complaints)

# Save to CSV
complaints_df.to_csv("datasets/complaints.csv", index=False)

print("complaints.csv generated successfully!\n")
print(complaints_df.head())
print("\nTotal Complaint Records:", len(complaints_df))