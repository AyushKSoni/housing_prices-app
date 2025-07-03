# 🏠 Housing Price Prediction App

A Machine Learning-powered web application that predicts housing prices based on user input features like area, bedrooms, bathrooms, and more.

## 🔍 Project Overview

This project:
- Uses a **Linear Regression** model trained on the [Housing.csv](Housing.csv) dataset.
- Takes user input through a **Streamlit web app**.
- Outputs predicted house price in ₹.

Live App: 👉 [Click here to try it](https://ayushksoni-housing-prices-app.streamlit.app)

---

## 📊 Features Used for Prediction

- Area (sq ft)
- Number of Bedrooms
- Bathrooms
- Stories
- Parking spaces
- Main road access
- Guestroom availability
- Basement
- Hot water heating
- Air conditioning
- Preferred location
- Furnishing status

---

## 🧠 ML Model

- **Algorithm**: Linear Regression
- **Libraries**: scikit-learn, pandas, numpy
- Trained in Google Colab and saved using `joblib`.

---

## ⚙️ Installation (Optional for Local Run)

```bash
git clone https://github.com/AyushKSoni/housing_prices-app.git
cd housing_prices-app
pip install -r requirements.txt
streamlit run app.py
