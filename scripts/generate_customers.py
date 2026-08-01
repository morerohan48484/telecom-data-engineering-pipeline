import pandas as pd
import random
from faker import Faker

# Create Faker object
fake = Faker("en_IN")

# Generate same random data every time
random.seed(42)

# Lists
cities = [
    "Mumbai",
    "Pune",
    "Delhi",
    "Hyderabad",
    "Bangalore",
    "Chennai",
    "Ahmedabad",
    "Nagpur"
]

plans = ["Prepaid", "Postpaid"]

statuses = ["Active", "Inactive"]

states = {
    "Mumbai": "Maharashtra",
    "Pune": "Maharashtra",
    "Delhi": "Delhi",
    "Hyderabad": "Telangana",
    "Bangalore": "Karnataka",
    "Chennai": "Tamil Nadu",
    "Ahmedabad": "Gujarat",
    "Nagpur": "Maharashtra"
}

# Empty list
customers = []

# Generate 100 customers
for i in range(1, 101):

    city = random.choice(cities)

    customer = {
        "customer_id": 1000 + i,
        "customer_name": fake.name(),
        "city": city,
        "state": states[city],
        "plan": random.choice(plans),
        "join_date": fake.date_between("-2y", "today"),
        "status": random.choice(statuses)
    }

    customers.append(customer)

# Convert list to DataFrame
customers_df = pd.DataFrame(customers)

# Save CSV
customers_df.to_csv("datasets/customers.csv", index=False)

print("customers.csv generated successfully!")
print(customers_df.head())
# Data Verification
print("\nDataset Information")
print("---------------------")
print("Total Customers :", len(customers_df))
print("Columns :", customers_df.columns.tolist())
print("\nData Types")
print(customers_df.dtypes)