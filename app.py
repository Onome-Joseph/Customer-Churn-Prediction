import streamlit as st
import numpy as np
import pickle

# Load the model
scaler = pickle.load(open('scaler2.pkl', 'rb'))    #path to directory
model = pickle.load(open('XGB_model.pkl', 'rb'))   #path to dorectory

# App title and description
st.title('Customer Churn Prediction')
st.markdown("""This app predicts whether a customer is likely to churn based on their details. Please fill in the information at the left hand side.""")

# Sidebar inputs
st.sidebar.header("Customer Details")
CreditScore = st.sidebar.slider("Credit Score", min_value=300, max_value=900, value=650, help="Enter the customer's credit score (300-900).")
Geography = st.sidebar.selectbox("Geography", options=["France", "Spain", "Germany"], index=0, help="Select the customer's country.")
Gender = st.sidebar.selectbox("Gender", options=["Male", "Female"], index=0, help="Select the customer's gender.")
Age = st.sidebar.slider("Age", min_value=16, max_value=95, value=30, help="Enter the customer's age.")
Tenure = st.sidebar.slider("Tenure", min_value=0, max_value=10, value=5, help="Enter the customer's tenure in years.")
Balance = st.sidebar.slider("Balance", min_value=0, max_value=300000, value=50000, step=1000, help="Enter the customer's bank balance.")
NumOfProducts = st.sidebar.slider("Number of Products", min_value=1, max_value=4, value=2, help="Enter the number of products the customer is subscribed to.")
HasCrCard = st.sidebar.selectbox("Has Credit Card?", options=["No", "Yes"], index=1, help="Indicate whether the customer has a credit card.")
IsActiveMember = st.sidebar.selectbox("Is Active Member?", options=["No", "Yes"], index=1, help="Indicate whether the customer is an active member.")
EstimatedSalary = st.sidebar.slider("Estimated Salary", min_value=10000, max_value=220000, value=100000, step=1000, help="Enter the customer's estimated annual salary.")

# For categorical inputs
Geography_mapping = {"France": 0, "Spain": 2, "Germany": 1}
Gender_mapping = {"Male": 1, "Female": 0}
HasCrCard_mapping = {"No": 0, "Yes": 1}
IsActiveMember_mapping = {"No": 0, "Yes": 1}

Geography = Geography_mapping[Geography]
Gender = Gender_mapping[Gender]
HasCrCard = HasCrCard_mapping[HasCrCard]
IsActiveMember = IsActiveMember_mapping[IsActiveMember]

# Prepare input data
input_data = np.array([[CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]])

# Predict churn
scaled_data = scaler.transform(input_data)
prediction = model.predict(scaled_data)[0]
predicted_churn = "Exit" if prediction == 1 else "Not Exit"

# Display result
st.subheader("Prediction Result")
if predicted_churn == "Exit":
    st.error(f"The customer is predicted to **{predicted_churn}**.")
else:
    st.success(f"The customer is predicted to **{predicted_churn}**.")

# Footer
st.markdown("---")
st.markdown("Made using Streamlit.")
