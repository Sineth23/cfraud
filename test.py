
import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import json
from sklearn.ensemble import RandomForestClassifier



# loading the trained model
pickle_in = open('rf_model.pkl', 'rb') 
classifier = pickle.load(pickle_in)


with open('deviceinfo.json') as f:
    device = json.load(f)

@st.cache()
  
def prediction(id_02, id_17, id_19, id_20, DeviceInfo, TransactionAmt, card1, card2, card3, addr1, C1, D4, D15, V23, V44, V86):
    
    x = [[id_02, id_17, id_19, id_20, DeviceInfo, TransactionAmt, card1, card2, card3, addr1, C1, D4, D15, V23, V44, V86]]
    prediction = classifier.predict(x)
     
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Credit Card Fraud Prediction</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 

    id_02 = st.selectbox('id_02',(device['id_02']))
    id_17 = st.selectbox('id_17',(device['id_17']))

    id_19 = st.selectbox('id_19',(device['id_19']))
    id_20 = st.selectbox('id_20',(device['id_20']))
    DeviceInfo = st.selectbox('DeviceInfo',(device['DeviceInfo']))
    DeviceInfo = device['device'][DeviceInfo]

    TransactionAmt = st.number_input("TransactionAmt") 

    card1 = st.selectbox('card1',(device['card1']))
    card2 = st.selectbox('card2',(device['card2']))
    card3 = st.selectbox('card3',(device['card3']))
    addr1 = st.selectbox('addr1',(device['addr1']))
    C1 = st.selectbox('C1',(device['C1']))
    D4 = st.selectbox('D4',(device['D4']))
    D15 = st.selectbox('D15',(device['D15']))
    V23 = st.selectbox('V23',(device['V23']))
    V44 = st.selectbox('V44',(device['V44']))
    V86 = st.selectbox('V86',(device['V86']))

    
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"):
        
        result = prediction(id_02, id_17, id_19, id_20, DeviceInfo, TransactionAmt, card1, card2, card3, addr1, C1, D4, D15, V23, V44, V86)
        if result == 0:
            pred = "Fraud"
            st.write('{}'.format(pred))
        else:
            pred = "Not Fraud"
            st.write('{}'.format(pred))

print('hello world')
print('hello world')
     
if __name__=='__main__': 
    main()

