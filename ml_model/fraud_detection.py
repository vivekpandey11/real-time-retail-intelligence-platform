import pandas as pd

data = {
    "transaction_id": [1, 2, 3, 4, 5],
    "amount": [100, 5000, 250, 12000, 300],
    "fraud": [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

print(df)

print("\nFraud Transactions:")
print(df[df["fraud"] == 1])