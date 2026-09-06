
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('complete_lr_model.sav')

st.title('Linear Regression Model for Sales Prediction')
st.write('Enter the advertising spending to predict sales.')

# Input fields for features
tv = st.slider('TV Advertising Spending', 0.0, 300.0, 150.0)
radio = st.slider('Radio Advertising Spending', 0.0, 50.0, 25.0)
newspaper = st.slider('Newspaper Advertising Spending', 0.0, 115.0, 40.0)

# Create a DataFrame for prediction
input_data = pd.DataFrame([{
    'TV': tv,
    'Radio': radio,
    'Newspaper': newspaper
}])

# Make prediction
if st.button('Predict Sales'):
    prediction = model.predict(input_data)[0]
    st.success(f'Predicted Sales: {prediction:.2f} units')
