import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Sample Data

data = {
    "amount": [100, 5000, 250, 12000, 300, 8000, 150, 9000],
    "fraud":  [0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Features and Target

X = df[["amount"]]
y = df["fraud"]

# Model

model = DecisionTreeClassifier()

model.fit(X, y)

print("Model Trained Successfully")

# Test Prediction

prediction = model.predict([[7000]])

print("Prediction for Amount 7000:")
print(prediction)