import joblib
import pandas as pd

# Load Saved Model

model = joblib.load("ml_model/fraud_model.pkl")

print("Model Loaded Successfully")

# Test Transaction

test_data = pd.DataFrame({
    "amount": [7000]
})

prediction = model.predict(test_data)

print("Prediction Result:")
print(prediction)

if prediction[0] == 1:
    print("Fraud Transaction Detected")
else:
    print("Normal Transaction")