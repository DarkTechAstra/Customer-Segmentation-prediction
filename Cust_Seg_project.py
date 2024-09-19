import streamlit as st
import joblib

# Load the trained model
model = joblib.load('customer_segmentation_model2.pkl')

# Create a Streamlit app
st.title('Customer Segmentation Prediction')

# Create form for user inputconda activate myenv

age = st.number_input('Age', min_value=18, max_value=100, value=25)
gender = st.selectbox('Gender', ('Male', 'Female'))
annual_income = st.number_input('Annual Income', min_value=10000, max_value=1000000, value=50000)
spending_score = st.number_input('Spending Score', min_value=0, max_value=100, value=50)

# Gender to numeric value
gender = 0 if gender == 'Male' else 1

# Prepare input data
input_data = [[age, gender, annual_income, spending_score]]

# Button to predict
if st.button('Predict Customer Segment'):
    prediction = model.predict(input_data)[0]
    st.write(f'Predicted Customer Segment: {prediction}')
