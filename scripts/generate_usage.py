import pandas as pd
import random
from faker import Faker

fake = Faker("en_IN")
random.seed(42)

# Read customer dataset
customers_df = pd.read_csv("datasets/customers.csv")

# Get customer IDs
customer_ids = customers_df["customer_id"].tolist()

# Generate 1000 usage records
usages = []

for i in range(1, 1001):
    usage = {
        "usage_id": f"U{i:04d}",
        "customer_id": random.choice(customer_ids),
        "usage_date": fake.date_between("-1y", "today"),
        "data_used_gb": round(random.uniform(0.5, 10.0), 2),
        "call_minutes": random.randint(10, 500),
        "sms_count": random.randint(0, 200)
    }
    usages.append(usage)

# Convert to DataFrame
usage_df = pd.DataFrame(usages)

# Save to CSV
usage_df.to_csv("datasets/usage.csv", index=False)

print("usage.csv generated successfully!\n")
print(usage_df.head())
print("\nTotal Usage Records:", len(usage_df))