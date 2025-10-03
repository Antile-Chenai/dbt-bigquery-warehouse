# 5️⃣ dbt BigQuery Warehouse
print("Starting dbt BigQuery Warehouse Project...\n")

import time
import random

# Simulate a list of dbt models
models = [
    "stg_customers",
    "stg_orders",
    "stg_products",
    "fct_sales",
    "fct_customer_metrics",
    "dim_customers",
    "dim_products",
    "dim_regions",
    "fct_inventory",
    "fct_revenue"
]

# Simulate running each dbt model with validation checks
for i, model in enumerate(models):
    print(f"Running dbt model {i+1}: {model}...")
    
    # Simulate query execution time
    time.sleep(random.uniform(0.1, 0.3))
    
    # Simulate row count returned
    rows = random.randint(1000, 5000)
    print(f"{rows} rows processed for {model}")
    
    # Simulate data validation check
    nulls = random.randint(0, 5)
    if nulls > 0:
        print(f"Warning: {nulls} NULL values detected in {model}")
    else:
        print(f"No nulls detected in {model}")
    
    # Simulate table load
    print(f"Loading {model} into BigQuery table...")
    time.sleep(random.uniform(0.1, 0.2))
    print(f"{model} load completed.\n")

# Simulate generating dbt run summary
print("Generating dbt run summary...\n")
summary = {
    "models_run": len(models),
    "total_rows": sum([random.randint(1000, 5000) for _ in models]),
    "errors": random.randint(0, 2)
}

print(f"Models run: {summary['models_run']}")
print(f"Total rows processed: {summary['total_rows']}")
print(f"Total errors: {summary['errors']}")
if summary['errors'] > 0:
    print("Check logs for details on errors.")
else:
    print("All models ran successfully!")

# Simulate dbt test runs
print("\nRunning dbt tests...")
tests = ["unique_customer_id", "non_null_order_id", "referential_integrity_orders_customers"]
for test in tests:
    print(f"Running test: {test}...")
    time.sleep(random.uniform(0.1, 0.2))
    test_result = random.choice(["PASS", "PASS", "FAIL"])
    print(f"Test {test} result: {test_result}\n")

print("All dbt tests completed!")

# Final completion message
print("\ndbt BigQuery Warehouse Project Completed Successfully!")
