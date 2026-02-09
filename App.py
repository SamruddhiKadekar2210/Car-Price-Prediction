import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load('car_price_model.joblib')
st.success("Model loaded successfully!")

st.header("Car Price Prediction App")

# Numeric inputs
year = st.slider("Enter Car Year", 1990, 2026, 2015)
engine_size = st.slider("Enter Engine Size (in liters)", 1, 6, 2)
mileage = st.number_input("Enter Mileage (km)", min_value=0, max_value=500000, value=50000)

# Make input
make_options = ['BMW', 'Ford', 'Honda', 'Toyota']
make = st.selectbox("Select Car Make", make_options)

# Model input
model_options = ['Model B', 'Model C', 'Model D', 'Model E']
car_model = st.selectbox("Select Car Model", model_options)

# Fuel Type
fuel_options = ['Electric', 'Petrol']
fuel_type = st.selectbox("Select Fuel Type", fuel_options)

# Transmission
trans_options = ['Manual', 'Automatic']
transmission = st.selectbox("Select Transmission Type", trans_options)

# Prepare input array matching your CSV columns
input_data = [
    year,
    engine_size,
    mileage,
    1 if make == 'BMW' else 0,
    1 if make == 'Ford' else 0,
    1 if make == 'Honda' else 0,
    1 if make == 'Toyota' else 0,
    1 if car_model == 'Model B' else 0,
    1 if car_model == 'Model C' else 0,
    1 if car_model == 'Model D' else 0,
    1 if car_model == 'Model E' else 0,
    1 if fuel_type == 'Electric' else 0,
    1 if fuel_type == 'Petrol' else 0,
    1 if transmission == 'Manual' else 0
]

# Convert to NumPy array and reshape
input_data = np.asarray(input_data).reshape(1, -1)

# Predict
if st.button("Predict"):
    predicted_price = model.predict(input_data)
    st.success(f"Estimated Car Price: ₹ {round(predicted_price[0], 2)}")
