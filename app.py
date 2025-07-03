import streamlit as st
import numpy as np
import pickle

# Load the trained model using pickle
with open("fhousing_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# Set page title and layout
st.set_page_config(page_title="Housing Price Predictor", layout="centered")
st.title("🏠 Housing Price Predictor")
st.write("Enter property details to estimate its market price (in ₹).")

# Input features
area = st.number_input("Area (sq ft)", min_value=500, max_value=10000, step=50)
bedrooms = st.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Number of Bathrooms", [1, 2, 3, 4])
stories = st.selectbox("Number of Stories", [1, 2, 3, 4])
parking = st.selectbox("Parking Spaces", [0, 1, 2, 3, 4])

# Binary categorical features
mainroad = st.radio("Is it on the Main Road?", ['yes', 'no'])
guestroom = st.radio("Guestroom Available?", ['yes', 'no'])
basement = st.radio("Basement Available?", ['yes', 'no'])
hotwaterheating = st.radio("Hot Water Heating?", ['yes', 'no'])
airconditioning = st.radio("Air Conditioning?", ['yes', 'no'])
prefarea = st.radio("Preferred Area?", ['yes', 'no'])

# Furnishing status with one-hot encoding (drop 'furnished')
furnishing = st.selectbox("Furnishing Status", ['furnished', 'semi-furnished', 'unfurnished'])

# Convert all inputs into model format
input_data = [
    area,
    bedrooms,
    bathrooms,
    stories,
    parking,
    1 if mainroad == 'yes' else 0,
    1 if guestroom == 'yes' else 0,
    1 if basement == 'yes' else 0,
    1 if hotwaterheating == 'yes' else 0,
    1 if airconditioning == 'yes' else 0,
    1 if prefarea == 'yes' else 0,
    1 if furnishing == 'semi-furnished' else 0,  # drop_first=True in training
    1 if furnishing == 'unfurnished' else 0
]

# Prediction button
if st.button("Predict Price"):
    try:
        price = model.predict([input_data])[0]
        st.success(f"🏷️ Estimated House Price: ₹ {int(price):,}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
