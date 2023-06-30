import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Setting a seed for reproducibility
np.random.seed(0)

# Number of customers
n_customers = 1000

# Generate synthetic data
data = {
    'customer_id': [fake.unique.random_number(digits=5) for _ in range(n_customers)],
    'age': [fake.random_int(min=18, max=70) for _ in range(n_customers)],
    'income': [fake.random_int(min=30000, max=100000) for _ in range(n_customers)],
    'product_owned': [fake.random_element(elements=('Product A', 'Product B', 'Product C', None)) for _ in range(n_customers)],
    'competitor_product_owned': [fake.random_element(elements=('Competitor Product A', 'Competitor Product B', None)) for _ in range(n_customers)],
    'last_purchase': [fake.random_int(min=1, max=365) for _ in range(n_customers)],
    'churned': [fake.random_element(elements=(0, 1)) for _ in range(n_customers)],
    'product_knowledge': [fake.random_int(min=1, max=10) for _ in range(n_customers)],
}

df = pd.DataFrame(data)

# Save as CSV
df.to_csv('synthetic_customer_data.csv', index=False)