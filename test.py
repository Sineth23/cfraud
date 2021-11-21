
import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import json
import helper as hp



# loading the trained model
pickle_in = open('rf_model.pkl', 'rb') 
classifier = pickle.load(pickle_in)

tr = pd.read_csv('uni.csv')

hp.label_enc(tr, 'DeviceInfo')

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

    id_02 = st.selectbox('id_02',(tr.id_02.unique()))
    id_17 = st.selectbox('id_17',(tr.id_17.unique()))

    id_19 = st.selectbox('id_19',(tr.id_19.unique()))
    id_20 = st.selectbox('id_20',(tr.id_20.unique()))
    DeviceInfo = st.selectbox('DeviceInfo',(tr.DeviceInfo.unique()))
    DeviceInfo = device[DeviceInfo]

    TransactionAmt = st.number_input("TransactionAmt") 

    card1 = st.selectbox('card1',(tr.card1.unique()))
    card2 = st.selectbox('card2',(tr.card2.unique()))
    card3 = st.selectbox('card3',(tr.card3.unique()))
    addr1 = st.selectbox('addr1',(tr.addr1.unique()))
    C1 = st.selectbox('C1',(tr.C1.unique()))
    D4 = st.selectbox('D4',(tr.D4.unique()))
    D15 = st.selectbox('D15',(tr.D15.unique()))
    V23 = st.selectbox('V23',(tr.V23.unique()))
    V44 = st.selectbox('V44',(tr.V44.unique()))
    V86 = st.selectbox('V86',(tr.V86.unique()))

    
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"):
        
        result = prediction(id_02, id_17, id_19, id_20, DeviceInfo, TransactionAmt, card1, card2, card3, addr1, C1, D4, D15, V23, V44, V86)
        if result == 0:
            pred = "Fraud"
            st.write('{}'.format(pred))
        else:
            pred = "Not Fraud"
            st.write('{}'.format(pred))


     
if __name__=='__main__': 
    main()

