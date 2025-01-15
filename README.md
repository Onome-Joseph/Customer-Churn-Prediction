# Customer Churn Prediction Model  
This project predicts whether a customer is likely to stop patronizing a business. Using historical customer data, the model analyzes patterns and behaviors to provide accurate predictions, enabling businesses to take proactive measures to retain customers.    

## Applications    
1. **Telecommunications**: Predicts customer churn based on usage patterns and complaints.  
2. **E-Commerce**: Identifies at-risk customers based on purchase frequency, reviews, and interactions.  
3. **Banking and Finance**: Anticipates churn for services like credit cards or loans.   
---
4. **Enhanced Customer Retention**: Allows targeted retention strategies for at-risk customers.  
5. **Increased Revenue**: Prevents revenue loss by reducing churn.  
6. **Improved Customer Relationships**: Enables businesses to personalize interventions for better engagement.   

# Customer Churn Prediction App
This is a **Streamlit web application** that predicts whether a customer is likely to churn based on various input features such as credit score, geography, age, and more. The app uses a pre-trained machine learning model.

## Features
- Intuitive UI for inputting customer details.
- Provides predictions on customer churn status.
- Clean and interactive interface built using Streamlit.
---
## Prerequisites
Ensure you have the following installed:
- Python 3.7 or higher
- Streamlit library
- Necessary dependencies listed in `requirements.txt`
---
## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Onome-Joseph/Customer-Churn-Prediction.git
   cd Customer-Churn-Prediction
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
---
## Running the App

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Open the app in your browser. The default URL is:
   ```
   http://localhost:8501
   ```
---
## File Descriptions
- **`Customer Churn Model`**: Jupyter Notebook containing the trained model 
- **`app.py`**: The main Streamlit application script.
- **`scaler2.pkl`**: Pre-trained scaler used for normalizing input data.
- **`XGB_model.pkl`**: Pre-trained XGBoost model for churn prediction.
- **`requirements.txt`**: Lists the dependencies required to run the application.
---

## Contributions  
Contributions are welcome! Feel free to fork the repository or report issues.  
