import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler

# Load the model
model = joblib.load('model.joblib')

# Initialize MinMaxScaler
minmax = MinMaxScaler(feature_range=(0, 1))  # Adjust feature_range if needed

# Define the application
def main():
    # Create a title and a subheader
    st.title('Status Prediction App')
    st.subheader('This app predicts the status of a child based on their age, gender, and body height.')

    # Get the input data from the user
    age = st.number_input('Age (months)', min_value=0, max_value=60)
    gender = st.selectbox('Gender', ['Female', 'Male'])
    body_height = st.number_input('Body height (cm)', min_value=0, max_value=100)

    # Encode the gender
    gender_encoded = 0 if gender == 'Female' else 1

    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'Age (Month)': [age],
        'Gender': [gender_encoded],
        'Body height': [body_height]
    })

    # Normalize the input data
    input_data['Body height'] = minmax.fit_transform(input_data[['Body height']])

    # Predict the status
    prediction = model.predict(input_data)[0]

    # Display the prediction
    st.write('Predicted status:', prediction)

# Run the application
if __name__ == '__main__':
    main()
