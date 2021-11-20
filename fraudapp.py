import streamlit as st 
import numpy as np
import pandas as pd
st.title('Credit Card Fraud Prediction')

st.write("""
#Predict whether the data has fraud applications.
""")

dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('Test Data1', 'Test Data2')
)

classifier_name = st.sidebar.selectbox(
    'Select classifier',
    ('Logistic Regression', 'Decision Trees', 'Random Forest')
)


def get_dataset(name):
    data = None
    if name == 'Test Data1':
        data = pd.read_csv('train_identity.csv')
    else:
        data = data = pd.read_csv('train_transaction.csv')
    X = data.drop('isFraud', axis=1)
    y = data.isFraud
    return X, y

