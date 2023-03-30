import numpy as np 
import pandas as pd
import streamlit as st
import pickle
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
loaded_model = pickle.load(open("model.pkl","rb"))
#creating afunction for prediction
def worker_prediction(input_data):
    
    input_data_as_numpy_array=scaler.fit_transform(input_data)
    inputdata_reshaped=input_data_as_numpy_array.reshape(1,-1)
    output=loaded_model.predict(inputdata_reshaped)
    print(output)
    if(output[0]==0):
        return 'This transaction is legit'
    else:
        return 'The transaction is fraud'
    
def main():
    st.title("Money Laundering Detection")
    step                               = st.text_input("Enter Maps of unit time in real world")   
    type                 = st.text_input("Enter type of money transfer")  
    amount               = st.text_input("Enter : Amount of transaction in local currency. ") 
    oldbalanceOrg                = st.text_input("Enter Initial balance before the transaction ")  
    newbalanceOrig    = st.text_input("Enter  Customer's balance after the transaction. ")  
    oldbalanceDest          = st.text_input("Enter Initial recipient balance before the transaction. ")  
    newbalanceDest         = st.text_input("Enter Recipient's balance after the transaction.")  
    isFlaggedFraud                   = st.text_input("Enter Money laundering or not according our heuristics")
    

    
    #code for prediction
    p= ""
    if st.button("Result"):
        p=worker_prediction([step,type,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,isFlaggedFraud])
    st.success(p)
    
if __name__ == '__main__':
    main()
   
